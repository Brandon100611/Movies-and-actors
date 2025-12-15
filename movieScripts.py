'''A python script to create a database of movies in SQLite.
authors: Kyle Burke.'''
import sqlite3
 
connection = sqlite3.connect("movies.db")
 
cursor = connection.cursor()
 
##sql = """DROP TABLE movies"""
##try:
##    cursor.execute(sql)
##except:
##    print("Hi!")
 
sql = "PRAGMA foreign_keys = ON"
cursor.execute(sql)
 
sql = """DROP TABLE IF EXISTS actors_in_movies"""
cursor.execute(sql)
 
sql = """DROP TABLE IF EXISTS movies"""
cursor.execute(sql)
 
sql = """DROP TABLE IF EXISTS actors"""
cursor.execute(sql)
 
sql = """CREATE TABLE IF NOT EXISTS actors (
    name TEXT NOT NULL PRIMARY KEY,
    birthdate DATETIME CHECK (birthdate < CURRENT_DATE),
    net_worth REAL,
    num_movies INTEGER CHECK (num_movies >= 0)
)"""
cursor.execute(sql)
 
sql = """CREATE TABLE IF NOT EXISTS movies (
title TEXT NOT NULL,
release_date DATETIME CHECK (release_date > '1888-10-13'
    AND release_date < CURRENT_DATE),
run_time INTEGER,
box_office_earnings REAL,
PRIMARY KEY (title, release_date)
)"""
cursor.execute(sql)
 
sql = """CREATE TABLE IF NOT EXISTS movie_genres (
    title TEXT NOT NULL,
    release_date DATETIME,
    genre TEXT,
    PRIMARY KEY (title, release_date, genre),
    FOREIGN KEY (title, release_date) REFERENCES
        movies(title, release_date)
)"""
cursor.execute(sql)
 
sql = """CREATE TABLE IF NOT EXISTS actors_in_movies (
    actor_name TEXT NOT NULL,
    title TEXT NOT NULL,
    release_date DATETIME,
    FOREIGN KEY (actor_name) REFERENCES actors(name),
    FOREIGN KEY (title, release_date) REFERENCES
        movies(title, release_date)
)"""
cursor.execute(sql)
 
 
sql = """INSERT INTO movies (release_date, run_time,
box_office_earnings, title) VALUES
('2010-07-09', 95, 543200000.00,
'Despicable Me');"""
cursor.execute(sql)
 
 
 
sql = """INSERT INTO movies (title, release_date, run_time,
box_office_earnings) VALUES
('Raiders of the Lost Ark', '1981-06-12', 115,
389900000.00)"""
cursor.execute(sql)
 
sql = """INSERT INTO movies
(title, release_date, run_time, box_office_earnings)
VALUES 
('Despicable Me 2', '2013-07-03', 98,
971000000.00),
('Despicable Me 3', '2017-06-30', 96,
1034000000.00);"""
cursor.execute(sql)
 
sql = """INSERT INTO movies
(title, release_date, run_time, box_office_earnings)
VALUES 
('Captain America: The Winter Soldier', '2014-04-04', 136,
714400000.00);"""
cursor.execute(sql)
 
sql = """INSERT INTO movies
(title, release_date, run_time, box_office_earnings)
VALUES 
('Singing in the Rain', '1952-03-27', 103, 7200000.00);"""
cursor.execute(sql)
 
sql = """INSERT INTO movies
(title, release_date, box_office_earnings)
VALUES 
('Chicken Little', '2015-10-06', 314400000.00);"""
cursor.execute(sql)
 
 
#sql = """DELETE
#FROM movies
#WHERE run_time < 100"""
#cursor.execute(sql)
 
sql = """UPDATE movies
SET release_date = '2005-10-06'
WHERE title = 'Chicken Little'
"""
cursor.execute(sql)
 
sql = """INSERT INTO movies
(title, release_date, run_time, box_office_earnings)
VALUES 
('Lord of the Rings: Return of the King', '2003-12-16',
201, 1137600000.00);"""
cursor.execute(sql)
 
 
sql = """
INSERT INTO
    movie_genres (title, release_date, genre)
VALUES
    (?, ?, ?)
"""
genre_data= [
    ('Despicable Me', '2010-07-09', 'family'),
    ('Despicable Me', '2010-07-09', 'comedy'),
    ('Despicable Me 2', '2013-07-03', 'family'),
    ('Despicable Me 2', '2013-07-03', 'comedy'),
    ('Despicable Me 3', '2017-06-30', 'family'),
    ('Despicable Me 3', '2017-06-30', 'comedy'),
    ('Raiders of the Lost Ark', '1981-06-12', 'action'),
    ('Raiders of the Lost Ark', '1981-06-12', 'adventure'),
    ('Captain America: The Winter Soldier', '2014-04-04', 'action'),
    ('Captain America: The Winter Soldier', '2014-04-04', 'adventure'),
    ('Singing in the Rain', '1952-03-27', 'musical'),
    ('Chicken Little', '2005-10-06', 'family'),
    ('Chicken Little', '2005-10-06', 'comedy'),
    ('Lord of the Rings: Return of the King', '2003-12-16', 'action'),
    ('Lord of the Rings: Return of the King', '2003-12-16', 'adventure')
]
cursor.executemany(sql, genre_data)
 
sql = """INSERT INTO movies
(title, release_date, run_time, box_office_earnings)
VALUES 
(?, ?, ?, ?);"""
movie_data = [
    ('Death Becomes Her', "1992-07-31",
          104, 149000000.00),
    ('500 Days of Summer', "2009-07-17",
          95, 60000000.00),
    ("She's All That", "1999-01-29",
          None, 103000000.00),
    ('Gladiator', "2000-05-01",
          155, 465400000.00),
    ('Gladiator', "1992-03-06",
         101, 9200000.00),
    ('Les Miserables', "2012-12-25",
         158, 442700000.00),
    ('Lord of the Rings: Return of the Monkey', '2004-12-16',
200, 137600000.00),
    ('Joker', '2019-10-04',
122, 1079000000.00),
    ('Pretty Woman', '1990-03-23',
125, 463000000.00),
    ('Silence of the Lambs', '1991-02-14',
118, 272000000.00),
    ('Dumb and Dumber', "1994-12-16",
          113, 247000000.00),
    ('The Hangover', "2009-06-05",
          96, 469300000.00),
    ("Thor: Love and Thunder", "2022-07-08",
         119, 760000000.00),
    ("Lucy in the Sky", "2019-10-04",
         124, 325000.00),
    ("The Exorcism", "2024-06-21",
         93, 9000000.00),
    ("The Prestige", "2006-10-20",
         130, 109000000.00),
    ("The Lawnmower Man", "1992-03-06",
         141, 150000000.00),
    #("The Lawnmower Man", "1992",
         #141, 150000000.00, "sci fi horror"),
    #These don't get added (because the first one causes an error)
    ('Gladiator', "2000-05-01",
          156, 465420000.00),
    ("George Washington Gets Dentures", '2083-07-04',
     115, 1000000000.00),
    ("George Washington Wrestled a Bear", '1783-07-04',
     11, 1000000.00)
    ]
##values = ('Death Becomes Her', "1992-07-31",
##          104, 149000000.00, "comedy")
##cursor.execute(sql, values)
##values = ('500 Days of Summer', "2009-07-17",
##          95, 60000000.00, "romantic comedy")
##cursor.execute(sql, values)
##values = ("She's All That", "1999-01-29",
##          95, 103000000.00, "romantic comedy")
##cursor.execute(sql, values)
 
try:
    cursor.executemany(sql, movie_data)
except:
    pass
 
 
 
 
 
sql = """INSERT INTO actors
(name, birthdate, net_worth, num_movies)
VALUES 
(?, ?, ?, ?);"""
value_data = [
    ("Russell Crowe", "1964-04-07", 120000000.00, 55),
    ("Joaquin Phoenix", "1974-10-25", 80000000.00, 55),
    ("Natalie Portman", "1981-06-09", 90000000.00, 51),
    ("Chris Evans", "1981-06-13", 110000000.00, 33),
    ("Hugh Jackman", "1968-10-12", 180000000.00, 53),
    ("Pierce Brosnan", "1953-05-16", 200000000.00, 72),
    ("Anne Hathaway", "1982-10-12", 80000000.00, 50),
    ("Jenny Wright", "1962-03-23", 1000000.00, 22),
    ("Cuba Gooding Jr.", "1968-01-02", 12000000.00, 56),
    ("Viggo Mortensen", "1958-10-20", 40000000.00, 46),
    ("Tom Holland", "1996-06-01", 25000000.00, 39)
]
cursor.executemany(sql, value_data)
 
 
sql = """INSERT INTO actors_in_movies
(actor_name, title, release_date)
VALUES 
(?, ?, ?);"""
value_data = [
    ("Russell Crowe", "Les Miserables", "2012-12-25"),
    ("Russell Crowe", "Gladiator", "2000-05-01"),
    ("Russell Crowe", "Thor: Love and Thunder", "2022-07-08"),
    ("Russell Crowe", "The Exorcism", "2024-06-21"),
    ("Joaquin Phoenix", "Gladiator", "2000-05-01"),
    ("Joaquin Phoenix", "Joker", "2019-10-04"),
    ("Natalie Portman", "Thor: Love and Thunder", "2022-07-08"),
    ("Natalie Portman", "Lucy in the Sky", "2019-10-04"),
    ("Hugh Jackman", "The Prestige", "2006-10-20"),
    ("Chris Evans", 'Captain America: The Winter Soldier',
     '2014-04-04'),
    ("Pierce Brosnan", "The Lawnmower Man", "1992-03-06"),
    ("Anne Hathaway", "Les Miserables", "2012-12-25"),
    ("Jenny Wright", "The Lawnmower Man", "1992-03-06"),
    ("Cuba Gooding Jr.", 'Gladiator', "1992-03-06"),
    ("Viggo Mortensen", 'Lord of the Rings: Return of the King', '2003-12-16')
]
cursor.executemany(sql, value_data)
 
 
print("~~~~~ WHERE example ~~~~~~~~~~~~~~~~")
 
sql = """SELECT
*
FROM movies
WHERE box_office_earnings > ?"""
cursor.execute(sql, (100.00, ) )
results = cursor.fetchall()
for result in results:
    print(result)
 
print("~~~~ SELECT example ~~~~~~~~~~~~~~~~~~")
 
sql = """SELECT
*
FROM actors"""
cursor.execute(sql)
results = cursor.fetchall()
for result in results:
    print(result)
 
print("~~~~~ MAX example ~~~~~~~~~~~~~~~~~")
 
sql = """SELECT
MAX(release_date), title
FROM movies"""
cursor.execute(sql)
results = cursor.fetchall()
for result in results:
    print(result)
 
print("~~~~~ MAX example ~~~~~~~~~~~~~~~~")
sql = """SELECT
MAX(box_office_earnings), title
FROM movies"""
cursor.execute(sql)
results = cursor.fetchall()
for result in results:
    print(result)
 
print("~~~~~~ DISTINCT example ~~~~~~~~~~~~~~~~")
sql = """SELECT
COUNT(DISTINCT box_office_earnings), title
FROM movies"""
cursor.execute(sql)
results = cursor.fetchall()
for result in results:
    print(result)
 
print("~~~~~~ MAX with WHERE example ~~~~~~~~~~~~~~~~")
sql = """SELECT
actor_name, title, MAX(release_date)
FROM actors_in_movies
WHERE actor_name = ?"""
params = ['Russell Crowe']
cursor.execute(sql, params)
results = cursor.fetchall()
for result in results:
    print(result)
 
print("~~~~~ GROUP BY example ~~~~~~~~~~~~~~~~~~~")
sql = """SELECT
genre, title, MIN(release_date)
FROM movies
GROUP BY genre"""
params = []
#cursor.execute(sql, params)
#results = cursor.fetchall()
#for result in results:
#    print(result)
 
print("~~~ HAVING example~~~~~~~~~~~~")
sql = """SELECT
genre, COUNT(*), MAX(release_date), MIN(release_date)
FROM movies
GROUP BY genre
HAVING COUNT(*) > 1"""
params = []
#cursor.execute(sql, params)
#results = cursor.fetchall()
#for result in results:
#    print(result)
 
print("~~~ Another HAVING example~~~~~~~~~~~~")
sql = """SELECT
genre, COUNT(*)
FROM movies
GROUP BY genre
HAVING MAX(release_date) >= '2000-01-01' AND
    MIN(release_date) <= '2000-01-01'"""
params = []
#cursor.execute(sql, params)
#results = cursor.fetchall()
#for result in results:
#    print(result)
 
print("~~~ Yet another HAVING example~~~~~~~~~~~~")
sql = """
SELECT
    actor_name, COUNT(*)
FROM
    actors_in_movies
GROUP BY
    actor_name
HAVING
    MAX(release_date)  >= '2015-01-01'"""
params = []
cursor.execute(sql, params)
results = cursor.fetchall()
for result in results:
    print(result)
 
print("~~~ ORDER BY example ~~~~~~~~~~~~")
sql = """
SELECT
    *
FROM
    movies
ORDER BY
    release_date DESC, box_office_earnings DESC"""
params = []
cursor.execute(sql, params)
results = cursor.fetchall()
for result in results:
    print(result)
 
print("~~~ Subquery Example ~~~~~~~~~~~~")
sql = """
SELECT
    *
FROM
    actors
WHERE
    actors.name IN
        (SELECT actor_name
        FROM actors_in_movies)"""
params = []
cursor.execute(sql, params)
results = cursor.fetchall()
for result in results:
    print(result)
 
print("~~~ Subquery Bad Example 2 ~~~~~~~~~~~~")
sql = """
SELECT
    *
FROM
    movies
WHERE
    movies.release_date IN
        (SELECT release_date
        FROM actors_in_movies) AND
    movies.title IN
        (SELECT title
        FROM actors_in_movies)"""
params = []
cursor.execute(sql, params)
results = cursor.fetchall()
for result in results:
    print(result)
 
print("~~~ Subquery Example 2 ~~~~~~~~~~~~")
sql = """
SELECT
    *
FROM
    movies
WHERE
    (movies.release_date, movies.title) IN
        (SELECT release_date, title
        FROM actors_in_movies)"""
params = []
cursor.execute(sql, params)
results = cursor.fetchall()
for result in results:
    print(result)
 
print("~~~ Subquery = Example ~~~~~~~~~~~~")
sql = """
SELECT
    *
FROM
    movies
WHERE
    (movies.release_date, movies.title) =
        (SELECT release_date, title
        FROM actors_in_movies)"""
params = []
cursor.execute(sql, params)
results = cursor.fetchall()
for result in results:
    print(result)
 
#get names and birthdates of actors in earliest-released
#movie with an actor
print("~~~ SubSubquery Example ~~~~~~~~~~~~")
sql = """
SELECT
    name, birthdate
FROM
    actors
WHERE
    name IN
        (SELECT
            actor_name
        FROM
            actors_in_movies
        WHERE release_date IN
            (SELECT
                MIN(release_date)
            FROM
                actors_in_movies))
ORDER BY
    birthdate"""
params = []
cursor.execute(sql, params)
results = cursor.fetchall()
for result in results:
    print(result)
 
#get names and birthdates of all actors from all movies
#that made the most money
print("~~~ SubSubSubquery Example ~~~~~~~~~~~~")
sql = """
SELECT
    name, birthdate
FROM
    actors
WHERE
    name IN
        (SELECT
            actor_name
        FROM
            actors_in_movies
        WHERE
            title IN
                (SELECT
                    name
                FROM
                    movies
                WHERE box_office_earnings =
                    (SELECT
                        MAX(box_office_earnings)
                    FROM
                        movies)))
ORDER BY
    birthdate"""
params = []
cursor.execute(sql, params)
results = cursor.fetchall()
for result in results:
    print(result)
 
 
print("~~~ Actors from most money movie: ~~~~~~~~~~~~")
sql = """SELECT
                    title
                FROM
                    movies
                WHERE box_office_earnings =
                    (SELECT
                        MAX(box_office_earnings)
                    FROM
                        movies)"""
params = []
cursor.execute(sql, params)
results = cursor.fetchall()
for result in results:
    print(result)
 
 
#get names and birthdates of actors in earliest-released
#movie with an actor
print("~~~ ALIAS example ~~~~~~~~~~~~")
sql = """
SELECT
    actor_name
FROM
    actors_in_movies AS a
WHERE
    (a.title, a.release_date) IN
        (SELECT
            title, release_date
        FROM
            movies
        WHERE
            box_office_earnings =
                (SELECT
                    MAX(box_office_earnings)
                FROM
                    movies))
    """
params = []
cursor.execute(sql, params)
results = cursor.fetchall()
for result in results:
    print(result)
 
 
 
print("~~~ ALIAS example 2 ~~~~~~~~~~~~")
sql = """
SELECT
    actor_name, title
FROM
    actors_in_movies AS a
WHERE
    release_date =
        (SELECT
            MIN(release_date)
        FROM
            actors_in_movies
        WHERE
            a.actor_name = actor_name)
    """
params = []
cursor.execute(sql, params)
results = cursor.fetchall()
for result in results:
    print(result)
 
 
#Join the entire actors and actors_in_movies tables
#WHY???????
print("~~~ JOIN example 0 (too big) ~~~~~~~~~~~~")
sql = """
SELECT
    *
FROM
    actors
INNER JOIN
    actors_in_movies
    """
params = []
cursor.execute(sql, params)
results = cursor.fetchall()
for result in results:
    print(result)
 
 
#Get the name and birthdate and release date of each
#actor and movie they acted in.
print("~~~ JOIN example 1 ~~~~~~~~~~~~")
sql = """
SELECT
    actors.name, actors.birthdate,
    a.release_date
FROM
    actors
INNER JOIN
    actors_in_movies AS a
ON
    actors.name = a.actor_name
    """
params = []
cursor.execute(sql, params)
results = cursor.fetchall()
for result in results:
    print(result)
 
 
#Get the name and box office earnings of each actor
#and each movie they acted in.
print("~~~ JOIN example 2 ~~~~~~~~~~~~")
sql = """
SELECT
    a.actor_name, m.box_office_earnings, m.title
FROM
    actors_in_movies AS a
INNER JOIN
    movies AS m
ON
    a.title = m.title AND
    a.release_date = m.release_date
    """
params = []
cursor.execute(sql, params)
results = cursor.fetchall()
for result in results:
    print(result)
 
 
#Join movies and actors_in_movies in the sensible way
print("~~~ USING example ~~~~~~~~~~~~")
sql = """
SELECT
    *
FROM
    movies
INNER JOIN
    actors_in_movies
USING (release_date, title)
    """
params = []
cursor.execute(sql, params)
results = cursor.fetchall()
for result in results:
    print(result)
 
 
#For each actor in a movie, I want the net worth of the
#actor and the box office earnings of the movie    
print("~~~ JOIN x2 example ~~~~~~~~~~~~")
sql = """
SELECT
    am.actor_name, a.net_worth, m.box_office_earnings
FROM
    actors_in_movies AS am
INNER JOIN
    actors AS a
ON
    a.name = am.actor_name
INNER JOIN
    movies AS m
ON
    am.title = m.title AND
    am.release_date = m.release_date
    """
params = []
cursor.execute(sql, params)
results = cursor.fetchall()
for result in results:
    print(result)
 
 
#For each actor get a tuple with that actor's net worth
# and the name of the movie they were in that made
# the most money.
print("~~~ JOIN x2 + GROUP BY example ~~~~~~~~~~~~")
sql = """
SELECT
    am.actor_name, a.net_worth, m.title,
    MAX(box_office_earnings)
FROM
    actors_in_movies AS am
INNER JOIN
    actors AS a
ON
    a.name = am.actor_name
INNER JOIN
    movies AS m
ON
    am.title = m.title AND
    am.release_date = m.release_date
GROUP BY
    am.actor_name
    """
params = []
cursor.execute(sql, params)
results = cursor.fetchall()
for result in results:
    print(result)
 
 
#For each actor get a tuple with that actor's net worth
# and the name of the movie they were in that made
# the most money.
print("~~~ JOIN x3 + Subquery example ~~~~~~~~~~~~")
sql = """
SELECT
    name, net_worth, title
FROM
    actors
INNER JOIN
    actors_in_movies
ON
    name = actor_name
INNER JOIN
    movies AS m
USING
    (title, release_date)
WHERE
    m.box_office_earnings =
        (SELECT
            MAX(box_office_earnings)
        FROM
            movies
        INNER JOIN
            actors_in_movies
        USING
            (title, release_date)
        WHERE
            actor_name = name)
    """
params = []
cursor.execute(sql, params)
results = cursor.fetchall()
for result in results:
    print(result)
 
 
 
 
 
 
#Get the name and birthdate and release date of each
#actor and movie they acted in.
print("~~~ OUTER JOIN example 1 ~~~~~~~~~~~~")
sql = """
SELECT
    actors.name, actors.birthdate,
    a.release_date
FROM
    actors
LEFT JOIN
    actors_in_movies AS a
ON
    actors.name = a.actor_name
    """
params = []
cursor.execute(sql, params)
results = cursor.fetchall()
for result in results:
    print(result)
 
 
 
#Just get the movies
print("~~~ boring example ~~~~~~~~~~~~")
sql = """
SELECT
    *
FROM
    movies
    """
params = []
cursor.execute(sql, params)
results = cursor.fetchall()
for result in results:
    print(result)
 
 
 
 
 
 
 
 
 
 
 
 
def has_movie(db_connection, title):
    '''Returns whether this database has a movie with title.'''
    #perform the database query
    cursor = db_connection.cursor()
    sql = "SELECT * from movies"
    cursor.execute(sql)
    results = cursor.fetchall()
 
    #search through the returned results
    for result in results:
        if result[0] == title:
            #Found it!
            return True
    #Didn't find it. :( 
    return False
 
        
##title = input("What movie do you want me to search for?\n")
##if has_movie(connection, title):
##    print("Hooray, " + title + " is there!")
##else:
##    print("No " + title + ".  :(")
 
 
 
connection.commit()
 