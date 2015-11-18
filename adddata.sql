
\c tournament;
DELETE FROM games;
DELETE FROM players;
INSERT INTO players (name, wins, matches) values('babloo', 0, 0);
INSERT INTO players (name, wins, matches) values('pintoo', 2, 3);
INSERT INTO players (name, wins, matches) values('chinyu', 1, 4);
INSERT INTO players (name, wins, matches) values('tom', 3, 5);
INSERT INTO players (name, wins, matches) values('dick', 0, 2);
INSERT INTO players (name, wins, matches) values('harry', 0, 0);
insert into games values((select player_id from players where name = 'tom'),
	(select player_id from players where name = 'dick'),
	(select player_id from players where name = 'tom'),
	false);
select * from players;
select * from games;
