-- Table definitions for the tournament project.
--
-- Put your SQL 'create table' statements in this file; also 'create view'
-- statements if you choose to use it.
--
-- You can write comments in this file by starting them with two dashes, like
-- these lines here.

DROP TABLE IF EXISTS players CASCADE;

CREATE TABLE players(
	player_id serial primary key UNIQUE,
	name text,
	wins int,
	matches int,
	points real, -- 1 for every win, .5 for tie
	opp_points real -- recorded only when victorious
);

DROP TABLE IF EXISTS matches CASCADE;

CREATE TABLE matches(
	match_id serial primary key UNIQUE,
	player1 int references players (player_id) ON DELETE CASCADE,
	player2 int references players (player_id) ON DELETE CASCADE,
	winner int references players (player_id) ON DELETE CASCADE,
	tie boolean
);






