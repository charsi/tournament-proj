-- Table definitions for the tournament project.

DROP DATABASE IF EXISTS tournament;
CREATE DATABASE tournament;
\c tournament

CREATE TABLE players(
	player_id serial primary key,
	name text  NOT NULL CHECK (name <> ''),
	wins int DEFAULT 0,
	matches int DEFAULT 0,
	points real DEFAULT 0.0, -- Win = 1, tie = 0.5
	-- cumulative points of opponents defeated
	opp_points real DEFAULT 0.0 
);

CREATE VIEW wins_tbl AS SELECT player_id, name, wins, matches
	FROM players ORDER BY points DESC, opp_points DESC;


CREATE TABLE matches(
	match_id serial primary key,
	player1 int references players (player_id) ON DELETE CASCADE,
	player2 int references players (player_id) ON DELETE CASCADE,
	winner int references players (player_id) ON DELETE CASCADE,
	tie boolean DEFAULT False
);


