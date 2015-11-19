-- Table definitions for the tournament project.

DROP TABLE IF EXISTS players CASCADE;

CREATE TABLE players(
	player_id serial primary key UNIQUE,
	name text,
	wins int,
	matches int,
	points real, -- Win = 1, tie = 0.5
	-- cumulative points of opponents defeated*
	opp_points real 
);

CREATE VIEW wins_tbl AS SELECT player_id, name, wins, matches
	FROM players ORDER BY points DESC, opp_points DESC;

DROP TABLE IF EXISTS matches CASCADE;

CREATE TABLE matches(
	match_id serial primary key UNIQUE,
	player1 int references players (player_id) ON DELETE CASCADE,
	player2 int references players (player_id) ON DELETE CASCADE,
	winner int references players (player_id) ON DELETE CASCADE,
	tie boolean
);


