-- Add dummy data into tables for testing


\c tournament;
DELETE FROM matches;
DELETE FROM players;
INSERT INTO players (name, wins, matches) values('a', 2, 2, 0.0, 0.0);
INSERT INTO players (name, wins, matches) values('b', 1, 2, 0.0, 0.0);
INSERT INTO players (name, wins, matches) values('c', 1, 2, 0.0, 0.0);
INSERT INTO players (name, wins, matches) values('d', 0, 2, 0.0, 0.0);
INSERT INTO players (name, wins, matches) values('e', 2, 2, 0.0, 0.0);
INSERT INTO players (name, wins, matches) values('f', 1, 2, 0.0, 0.0);
INSERT INTO players (name, wins, matches) values('g', 1, 2, 0.0, 0.0);
INSERT INTO players (name, wins, matches) values('h', 0, 2, 0.0, 0.0);
insert into matches (player1, player2, tie) values (
	(select player_id from players where name = 'a'),
	(select player_id from players where name = 'b'),
	False
);
insert into matches (player1, player2, tie) values (
	(select player_id from players where name = 'c'),
	(select player_id from players where name = 'd'),
	False
);
insert into matches (player1, player2, tie) values (
	(select player_id from players where name = 'e'),
	(select player_id from players where name = 'f'),
	False
);
insert into matches (player1, player2, tie) values (
	(select player_id from players where name = 'g'),
	(select player_id from players where name = 'h'),
	False
);
insert into matches (player1, player2, tie) values (
	(select player_id from players where name = 'a'),
	(select player_id from players where name = 'c'),
	False
);
insert into matches (player1, player2, tie) values (
	(select player_id from players where name = 'e'),
	(select player_id from players where name = 'g'),
	False
);
insert into matches (player1, player2, tie) values (
	(select player_id from players where name = 'b'),
	(select player_id from players where name = 'd'),
	False
);
insert into matches (player1, player2, tie) values (
	(select player_id from players where name = 'f'),
	(select player_id from players where name = 'h'),
	False
);

select * from players;
select * from matches;
