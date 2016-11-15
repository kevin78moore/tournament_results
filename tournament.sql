-- Table definitions for the tournament project.
--

DROP DATABASE IF EXISTS tournament;

CREATE DATABASE tournament;

\c tournament;

-- Creates the Player table
CREATE TABLE players (
  ID serial PRIMARY KEY,
  player_name varchar(255)
);

-- Creates the Matches table
CREATE TABLE matches (
  ID serial PRIMARY KEY,
  loser integer references Players(ID),
  winner integer references Players(ID)
);

-- Creates a table listing the number of wins for each player
CREATE VIEW WIN_BY_PLAYER_VIEW AS
SELECT winner, COUNT(winner) win_count
FROM matches
GROUP BY winner;

-- Creates a table of the standings
CREATE VIEW standings AS
SELECT players_id as player_id, players_name,
(SELECT count(*) FROM matches WHERE matches.winner = players.id) AS matches_Won,
(SELECT count(*) FROM matches WHERE players.id in (winner, loser)) as matches_Played
FROM players
GROUP BY players.id
ORDER BY matches_Won DESC;

-- Creates a table (player id, player name, win count) to be used in the last test 
CREATE VIEW WIN_BY_PLAYER_ORDERED_VIEW AS
SELECT players.id, players.player_name, coalesce(win_count,0) AS win_count 
FROM players
LEFT JOIN (
  SELECT winner, COUNT(winner) win_count
  FROM matches
  GROUP BY winner
) as WIN_TABLE
ON players.id = WIN_TABLE.winner
ORDER BY win_count DESC;
