#!/usr/bin/env python
# 
# tournament.py -- implementation of a Swiss-system tournament
#

import psycopg2

def connect():
    return psycopg2.connect("dbname=tournament")

def deleteMatches():
    """Remove all match records from the database"""
    conn = connect()
    c = conn.cursor()
    c.execute("DELETE FROM matches")
    conn.commit()
    conn.close()

def deletePlayers():
    """Remove all player records from the database"""
    conn = connect()
    c = conn.cursor()
    c.execute("DELETE FROM players")
    conn.commit()
    conn.close()

def countPlayers():
    """Returns the number of players that are currently registered"""
    conn = connect()
    c = conn.cursor()
    c.execute("SELECT COUNT(*) FROM players")
    player_count = c.fetchone()[0]
    conn.commit()
    conn.close()
    return player_count

def registerPlayer(name):
    """This adds a player to the tournament database.
    It assigns a unique id number for the player. 
    The name does not need to be unique"""
    conn = connect()
    c = conn.cursor()
    c.execute("INSERT INTO Players (player_name) VALUES (%s)", (name,))
    conn.commit()
    conn.close()

def playerStandings():
    """Returns a list of the players and their win records, sorted by wins.
    Returns: A list of tuples, each of which contains (id, name, wins, matches):
        id: the player's unique id (assigned by the database)
        name: the player's full name (as registered)
        wins: the number of matches the player has won
        matches: the number of matches the player has played
    """
    conn = connect()
    c = conn.cursor()
    c.execute("""SELECT * FROM standings""")
    winner_table = c.fetchall()
    conn.commit()
    conn.close()
    return winner_table

def reportMatch(winner, loser):
    """Records the outcome of a single match between two players.
      winner:  the id number of the player who won
      loser:  the id number of the player who lost
    """
    conn = connect()
    c = conn.cursor()
    c.execute("""
              INSERT INTO matches (winner, loser)
              VALUES (%s, %s)""", (winner, loser))
    conn.commit()
    conn.close()

def swissPairings():
    """Returns a list of the pairs of players for the next round of a match.
    Each player is paired with another player with an equal or nearly-equal win 
    record.
    Returns:
      A list of tuples, each of which contains (id1, name1, id2, name2)
        id1: the first player's unique id
        name1: the first player's name
        id2: the second player's unique id
        name2: the second player's name
    """
    conn = connect()
    c = conn.cursor()
    c.execute('SELECT * from WIN_BY_PLAYER_ORDERED_VIEW')
    player_list = c.fetchall()
    conn.commit()
    conn.close()
    result = []

    for i, player in enumerate(player_list):
        if i % 2 == 0:
            pair = (player_list[i][0],
                    player_list[i][1],
                    player_list[i+1][0],
                    player_list[i+1][1])
            result.append(pair)

    return result
