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
	matches int
);

DROP TABLE IF EXISTS matches CASCADE;

CREATE TABLE matches(
	match_id serial primary key UNIQUE,
	winner int references players (player_id) ON DELETE CASCADE,
	loser int references players (player_id) ON DELETE CASCADE
);






