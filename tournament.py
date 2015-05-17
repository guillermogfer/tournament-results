#!/usr/bin/env python
#
# tournament.py -- implementation of a Swiss-system tournament
#

import psycopg2


def connect():
    """Connect to the PostgreSQL database.  Returns a database connection."""
    return psycopg2.connect("dbname=tournament")


def deleteMatches():
    """Remove all the match records from the database."""
    db = connect()
    db_cursor = db.cursor()
    query = "DELETE FROM matches"
    db_cursor.execute(query)
    db.commit()
    db.close()


def deletePlayers():
    """Remove all the player records from the database."""
    db = connect()
    db_cursor = db.cursor()
    query = "DELETE FROM players"
    db_cursor.execute(query)
    db.commit()
    db.close()


def countPlayers():
    """Returns the number of players currently registered."""
    db = connect()
    db_cursor = db.cursor()
    query = "SELECT count(*) FROM players"
    db_cursor.execute(query)
    ret = db_cursor.fetchone()
    #db.commit()
    db.close()

    return ret[0]


def registerPlayer(name):
    """Adds a player to the tournament database.

    The database assigns a unique serial id number for the player.  (This
    should be handled by your SQL database schema, not in your Python code.)

    Args:
      name: the player's full name (need not be unique).
    """
    db = connect()
    db_cursor = db.cursor()
    query = "INSERT INTO players (name) VALUES (%s)"
    db_cursor.execute(query, (name,))
    db.commit()
    db.close()


def playerStandings():
    """Returns a list of the players and their win records, sorted by wins.

    The first entry in the list should be the player in first place, or a player
    tied for first place if there is currently a tie.

    Returns:
      A list of tuples, each of which contains (id, name, wins, matches):
        id: the player's unique id (assigned by the database)
        name: the player's full name (as registered)
        wins: the number of matches the player has won
        matches: the number of matches the player has played
    """
    db = connect()
    db_cursor = db.cursor()
    query = "SELECT tw.id, tw.name, tw.wins, tm.matches FROM total_wins tw, total_matches tm WHERE tw.name=tm.name"
    db_cursor.execute(query)
    ret = db_cursor.fetchall()
    #db.commit()
    db.close()

    return ret


def reportMatch(winner, loser):
    """Records the outcome of a single match between two players.

    Args:
      winner:  the id number of the player who won
      loser:  the id number of the player who lost
    """
    db = connect()
    db_cursor = db.cursor()
    query = "INSERT INTO matches (winner, loser) VALUES (%s, %s)"
    db_cursor.execute(query, (winner, loser))
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
    db = connect()
    db_cursor = db.cursor()
    query = "SELECT * FROM player_standings"
    db_cursor.execute(query)
    players = db_cursor.fetchall()

    pairings = []
    player_added = 0
    current_tuple = ()

    for player in players:
        # If no player was added, add the player and increment the count variable
        if player_added < 1:
            current_tuple = (player[0], player[1])
            player_added += 1
        # If it was a previously player added, add the player to a tuple and append it to the pairings list. Then reset the count variable
        else:
            current_tuple += (player[0], player[1])
            pairings.append(current_tuple)
            player_added = 0

    #db.commit()
    db.close()

    return pairings


