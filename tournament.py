#!/usr/bin/env python
#
# tournament.py -- implementation of a Swiss-system tournament
#

import psycopg2
import bleach
import pprint


def connect(workOnDb, commitReqd):
    """Wrapper function which handles connecting and disconnecting to the database.
    Args:
      workOnDb:  function that contains the quries to db
      commitReqd:  bool indicating if changes were made to db"""
    db = psycopg2.connect("dbname=tournament")
    cursor = db.cursor()
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
        c.execute("""INSERT INTO players (name, wins, matches, points, opp_points)
            VALUES(%s, 0, 0, 0.0, 0.0)""", (clean_name,))
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
        c.execute("""SELECT player_id, name, wins, matches
            FROM players ORDER BY points DESC""")
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
        # get current points for the losing player
        c.execute("""SELECT points
            FROM players
            WHERE player_id=%d""" % (loser,))
        loser_points = c.fetchone()[0]
        # increment wins, matches, points, opp_points for the winner
        c.execute("""UPDATE players
            SET wins= wins+1, points= points+1,
            matches = matches+1, opp_points = opp_points+%f
            WHERE player_id=%d""" % (loser_points, winner))
        # increment matches for loser
        c.execute("""UPDATE players
            SET matches = matches+1
            WHERE player_id=%d""" % (loser, ))
        # record result in matches table
        c.execute("""INSERT INTO matches (player1, player2, winner, tie)
            VALUES(%d,%d,%d, False)""" % (winner, loser, winner, ))
    return connect(dbWorker, True)


def reportTiedMatch(player1, player2):
    """Records the outcome of a single match that did not yeild a result.

    Args:
      player1:  the id number of the player who won
      player2:  the id number of the player who lost
    """
    def dbWorker(c):
        # increment wins, matches, points, opp_points for player1
        c.execute("""UPDATE players
            SET points= points+0.5, matches = matches+1
            WHERE player_id IN (%d, %d)""" % (player1, player2, ))
        c.execute("""INSERT INTO matches (player1, player2, tie)
            VALUES(%d,%d, True)""" % (player1, player2, ))
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
    wins_tbl = playerStandings()
    numOfPlayers = len(wins_tbl)
    if numOfPlayers % 2 != 0:
        raise ValueError("This program does not support odd number of players")
    pairList = []
    for i in range(0, numOfPlayers, 2):
        playerOne = wins_tbl[i]
        playerTwo = wins_tbl[i+1]
        pair = (
            playerOne[0], playerOne[1],
            playerTwo[0], playerTwo[1]
        )
        pairList.append(pair)
    return pairList
