
\c tournament;
DELETE FROM matches;
DELETE FROM players;
INSERT INTO players (name, wins, matches) values('a', 2, 2);
INSERT INTO players (name, wins, matches) values('b', 1, 2);
INSERT INTO players (name, wins, matches) values('c', 1, 2);
INSERT INTO players (name, wins, matches) values('d', 0, 2);
INSERT INTO players (name, wins, matches) values('e', 2, 2);
INSERT INTO players (name, wins, matches) values('f', 1, 2);
INSERT INTO players (name, wins, matches) values('g', 1, 2);
INSERT INTO players (name, wins, matches) values('h', 0, 2);
insert into matches (winner, loser) values (
	(select player_id from players where name = 'a'),
	(select player_id from players where name = 'b')
);
insert into matches (winner, loser) values (
	(select player_id from players where name = 'c'),
	(select player_id from players where name = 'd')
);
insert into matches (winner, loser) values (
	(select player_id from players where name = 'e'),
	(select player_id from players where name = 'f')
);
insert into matches (winner, loser) values (
	(select player_id from players where name = 'g'),
	(select player_id from players where name = 'h')
);
insert into matches (winner, loser) values (
	(select player_id from players where name = 'a'),
	(select player_id from players where name = 'c')
);
insert into matches (winner, loser) values (
	(select player_id from players where name = 'e'),
	(select player_id from players where name = 'g')
);
insert into matches (winner, loser) values (
	(select player_id from players where name = 'b'),
	(select player_id from players where name = 'd')
);
insert into matches (winner, loser) values (
	(select player_id from players where name = 'f'),
	(select player_id from players where name = 'h')
);

select * from players;
select * from matches;
