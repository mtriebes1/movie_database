/*----------------------------------------------------------------------
 * Name: Erik Ratchford & Matthew Triebes
 * File: DBMS_Project.sql
 * Date: 10/22/2020
 * Class: DBMS
 * Description: program to construct tables for movie DB
 ----------------------------------------------------------------------*/

set FOREIGN_KEY_CHECKS = 0;
drop table if exists movie;
drop table if exists db_user;
drop table if exists movie_db_user_review;
drop table if exists streaming_service; 
drop table if exists hosted_by; 
drop table if exists actor_actress; 
drop table if exists appears_in; 
drop table if exists director; 
drop table if exists movie_award;

set FOREIGN_KEY_CHECKS = 1;

SET sql_mode = STRICT_ALL_TABLES;


CREATE TABLE director	(
	director_name			VARCHAR(50),
	PRIMARY KEY (director_name)
);

INSERT INTO director VALUES('Christopher Nolan');
INSERT INTO director VALUES('Michael Bay');
INSERT INTO director VALUES('James Cameron');
INSERT INTO director VALUES('Steven Spielberg');
INSERT INTO director VALUES('Quentin Tarantino');
INSERT INTO director VALUES('Brad Anderson');
INSERT INTO director VALUES('Alfred Hitchcock');
INSERT INTO director VALUES('Sofia Coppola');
INSERT INTO director VALUES('Kathryn Bigelow');
INSERT INTO director VALUES('Wes Anderson');
INSERT INTO director VALUES('Guy Richie');
INSERT INTO director VALUES('Steve McQueen');
INSERT INTO director VALUES('Bong Jun-Ho');



CREATE TABLE movie 	(
	title			VARCHAR(50),
	year_released	YEAR,
	genre			VARCHAR(30),
	director_name	VARCHAR(50),
	PRIMARY KEY (title),
	FOREIGN KEY (director_name) REFERENCES director (director_name)
);


INSERT INTO movie VALUES('The Dark Knight', 2008, 'Drama', 'Christopher Nolan');
INSERT INTO movie VALUES('The Dark Knight Rises', 2012, 'Drama', 'Christopher Nolan');
INSERT INTO movie VALUES('Avatar', 2009, 'Drama', 'James Cameron');
INSERT INTO movie VALUES('Django Unchained', 2012, 'Western', 'Quentin Tarantino');
INSERT INTO movie VALUES('Lincoln', 2012, 'Drama', 'Steven Spielberg');
INSERT INTO movie VALUES('Transformers', 2007, 'Action', 'Michael Bay');
INSERT INTO movie VALUES('The Machinist', 2004, 'Thriller', 'Brad Anderson');


CREATE TABLE db_user	(
	user_id			INT,
	PRIMARY KEY (user_id)
);

INSERT INTO db_user VALUES(0);
INSERT INTO db_user VALUES(1);
INSERT INTO db_user VALUES(2);
INSERT INTO db_user VALUES(3);
INSERT INTO db_user VALUES(4);
INSERT INTO db_user VALUES(5);
INSERT INTO db_user VALUES(6);
INSERT INTO db_user VALUES(7);


CREATE TABLE movie_db_user_review	(
	movie_title		VARCHAR(50),
	user_id			INT,
	rating			INT CHECK (rating > -1 AND rating < 6),
	PRIMARY KEY (movie_title, user_id),
	FOREIGN KEY (movie_title) REFERENCES movie (title),
	FOREIGN KEY (user_id) REFERENCES db_user (user_id)
);


INSERT INTO movie_db_user_review VALUES('The Dark Knight', 0, 5);
INSERT INTO movie_db_user_review VALUES('The Dark Knight', 1, 5);
INSERT INTO movie_db_user_review VALUES('The Dark Knight', 2, 5);
INSERT INTO movie_db_user_review VALUES('The Dark Knight', 7, 5);
INSERT INTO movie_db_user_review VALUES('The Dark Knight', 4, 5);
INSERT INTO movie_db_user_review VALUES('Django Unchained', 7, 4);
INSERT INTO movie_db_user_review VALUES('Django Unchained', 4, 1);
INSERT INTO movie_db_user_review VALUES('Django Unchained', 6, 5);



CREATE TABLE streaming_service		(
	name			VARCHAR(50),
	PRIMARY KEY (name)
);


INSERT INTO streaming_service VALUES('Netflix');
INSERT INTO streaming_service VALUES('Hulu');
INSERT INTO streaming_service VALUES('Prime');


CREATE TABLE hosted_by		(
	movie_title		VARCHAR(50),
	streaming_service_name	VARCHAR(50),
	PRIMARY KEY (movie_title, streaming_service_name),
	FOREIGN KEY (movie_title) REFERENCES movie (title),
	FOREIGN KEY (streaming_service_name) REFERENCES streaming_service (name)
);


INSERT INTO hosted_by VALUES('The Dark Knight', 'Netflix');
INSERT INTO hosted_by VALUES('The Dark Knight', 'Prime');
INSERT INTO hosted_by VALUES('Avatar', 'Hulu');
INSERT INTO hosted_by VALUES('The Dark Knight Rises', 'Netflix');
INSERT INTO hosted_by VALUES('Django Unchained', 'Prime');
INSERT INTO hosted_by VALUES('Transformers', 'Netflix');
INSERT INTO hosted_by VALUES('Transformers', 'Prime');
INSERT INTO hosted_by VALUES('Lincoln', 'Prime');
INSERT INTO hosted_by VALUES('Lincoln', 'Hulu');
INSERT INTO hosted_by VALUES('The Machinist', 'Netflix');


CREATE TABLE actor_actress	(
	actor_name		VARCHAR(50),
	PRIMARY KEY (actor_name)
);

INSERT INTO actor_actress VALUES('Christian Bale');
INSERT INTO actor_actress VALUES('Zoe Saldana');
INSERT INTO actor_actress VALUES('Daniel Day-Lewis');

CREATE TABLE appears_in		(
	movie_title		VARCHAR(50),
	actor_name		VARCHAR(50),
	PRIMARY KEY (movie_title, actor_name),
	FOREIGN KEY (movie_title) REFERENCES movie (title),
	FOREIGN KEY (actor_name) REFERENCES actor_actress (actor_name)
);

INSERT INTO appears_in VALUES('The Dark Knight', 'Christian Bale');
INSERT INTO appears_in VALUES('The Dark Knight Rises', 'Christian Bale');
INSERT INTO appears_in VALUES('Avatar', 'Zoe Saldana');
INSERT INTO appears_in VALUES('The Machinist', 'Christian Bale');
INSERT INTO appears_in VALUES('Lincoln', 'Daniel Day-Lewis');

CREATE TABLE movie_award	(
	award_type		VARCHAR(50),
	award_name		VARCHAR(50),
	year_awarded	YEAR,
	movie_title		VARCHAR(50),
	PRIMARY KEY (award_type, award_name, movie_title),
	FOREIGN KEY (movie_title) REFERENCES movie (title)
);

INSERT INTO movie_award VALUES('Oscar', 'Best Original Screenplay', 2008, 'The Dark Knight');
INSERT INTO movie_award VALUES('Oscar', 'Best Sound Mixing', 2009, 'Avatar');
INSERT INTO movie_award VALUES('Oscar', 'Best Production Design', 2013, 'Lincoln');

show tables;