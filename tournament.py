#!/usr/bin/env python
#
# tournament.py -- implementation of a Swiss-system tournament
#

import psycopg2
import bleach


def connect(someFunction):
    "Connects to the PostgreSQL database.  Returns a database connection."
    db = psycopg2.connect("dbname=tournament")
    cursor = db.cursor()
    needCommit = someFunction(cursor)
    if (needCommit):
        db.commit()
    db.close()


def deleteMatches():
    "Removes all the match records from the database."
    connect(
        lambda cursor:
            cursor.execute("DELETE FROM matches;")
            is True     # commit required
    )


def deletePlayers():
    "Removes all the player records from the database."
    db, cursor = connect()
    cursor.execute("DELETE FROM players;")
    db.commit()
    db.close()


def countPlayers():
    "Returns the number of players currently registered."
    db, cursor = connect()
    cursor.execute("SELECT count(player_id) from players;")
    num = cursor.fetchone()[0]
    db.close()
    return num


def registerPlayer(name):
    clean_name = bleach.clean(name)      # Strips unsafe <script> tags etc
    db, cursor = connect()
    cursor.execute("""INSERT INTO players (name, wins, matches)
        VALUES(%s,0,0)""", (clean_name,))
    db.commit()
    db.close()


def playerStandings():
    """Returns a list of the players and their win records, sorted by wins.

    The first entry in the list should be the player in first place,
    or a player tied for first place if there is currently a tie.

      A list of tuples, each of which contains (id, name, wins, matches):
        id: the player's unique id (assigned by the database)
        name: the player's full name (as registered)
        wins: the number of matches the player has won
        matches: the number of matches the player has played
    """
    db, cursor = connect()
    cursor.execute("SELECT * from players ORDER BY wins DESC;")
    wins_tbl = cursor.fetchall()
    db.close()
    return wins_tbl


def reportMatch(winner, loser):
    """Records the outcome of a single match between two players.

    Args:
      winner:  the id number of the player who won
      loser:  the id number of the player who lost
    """
    db, cursor = connect()
    cursor.execute("""UPDATE players
        SET wins= wins+1, matches = matches+1
        WHERE player_id=%d""" % (winner,))
    cursor.execute("""UPDATE players
        SET matches = matches+1
        WHERE player_id=%d""" % (loser, ))
    cursor.execute("""INSERT INTO matches (winner, loser)
        VALUES(%d,%d);""" % (winner, loser, ))
    db.commit()
    db.close()


def swissPairings():
    """Returns a list of pairs of players for the next round of a match.

    Assuming that there are an even number of players registered, each player
    appears exactly once in the pairings.  Each player is paired with another
    player with an equal or nearly-equal win record, that is, a player adjacent
    to him or her in the standings.

    Returns:
      A list of tuples, each of which contains (id1, name1, id2, name2)
        id1: the first player's unique id
        name1: the first player's name
        id2: the second player's unique id
        name2: the second player's name
    """
    db, cursor = connect()
    cursor.execute("""SELECT *
        FROM players
        ORDER BY wins DESC""")
    playerAr = cursor.fetchall()
    numOfPlayers = len(playerAr)
    print numOfPlayers
    matchAr = [
        (playerAr[0][0], playerAr[0][1], playerAr[1][0], playerAr[1][1]),
        (playerAr[2][0], playerAr[2][1], playerAr[3][0], playerAr[3][1])
    ]
    return matchAr
    # DB.commit()
    db.close()
