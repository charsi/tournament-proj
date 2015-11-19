#!/usr/bin/env python
#
# tournament.py -- implementation of a Swiss-system tournament
#

import psycopg2
import bleach


def connect(workOnDb, commitReqd):
    """Connects to the PostgreSQL database.  Runs process specific function
    Commits changes if required, then diconnects from the database."""
    db = psycopg2.connect("dbname=tournament")
    cursor = db.cursor()
    # Perform the unique process
    # involving db queries
    returnVal = workOnDb(cursor)
    if commitReqd:
        db.commit()
    db.close()
    return returnVal


def deleteMatches():
    def dbWorker(c):
        c.execute("DELETE FROM matches;")
    return connect(dbWorker, True)


def deletePlayers():
    "Removes all the player records from the database."
    def dbWorker(c):
        c.execute("DELETE FROM players;")
    return connect(dbWorker, True)


def countPlayers():
    "Returns the number of players currently registered."
    def dbWorker(c):
        c.execute("SELECT count(player_id) from players;")
        num = c.fetchone()[0]
        return num
    return connect(dbWorker, False)


def registerPlayer(name):
    def dbWorker(c):
        clean_name = bleach.clean(name)      # Strips unsafe <script> tags etc
        c.execute("""INSERT INTO players (name, wins, matches)
            VALUES(%s,0,0)""", (clean_name,))
    return connect(dbWorker, True)


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
    def dbWorker(c):
        c.execute("SELECT * from players ORDER BY wins DESC;")
        wins_tbl = c.fetchall()
        return wins_tbl
    return connect(dbWorker, False)


def reportMatch(winner, loser):
    """Records the outcome of a single match between two players.

    Args:
      winner:  the id number of the player who won
      loser:  the id number of the player who lost
    """
    def dbWorker(c):
        c.execute("""UPDATE players
            SET wins= wins+1, matches = matches+1
            WHERE player_id=%d""" % (winner,))
        c.execute("""UPDATE players
            SET matches = matches+1
            WHERE player_id=%d""" % (loser, ))
        c.execute("""INSERT INTO matches (winner, loser)
            VALUES(%d,%d);""" % (winner, loser, ))
    return connect(dbWorker, True)


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
    def dbWorker(c):
        c.execute("""SELECT *
            FROM players
            ORDER BY wins DESC""")
        playerAr = c.fetchall()
        numOfPlayers = len(playerAr)
        print numOfPlayers
        matchAr = [
            (playerAr[0][0], playerAr[0][1], playerAr[1][0], playerAr[1][1]),
            (playerAr[2][0], playerAr[2][1], playerAr[3][0], playerAr[3][1])
        ]
        return matchAr
    return connect(dbWorker, False)
