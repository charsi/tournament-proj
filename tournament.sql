-- Table definitions for the tournament project.

DROP TABLE IF EXISTS players CASCADE;

CREATE TABLE players(
	player_id serial primary key UNIQUE,
	name text,
	wins int,
	matches int,
	points real, -- 1 for every win, .5 for tie
	opp_points real -- recorded only when player wins
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



