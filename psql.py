# -*- coding: utf-8 -*-
# login at elephantsql.com to get creds for free dbserver
import psycopg2

DSN = {
    'host': 'manny.db.elephantsql.com',
    'port': '5432',
    'database': '',
    'user': '',
    'password': '',
}

MOVIES = (
    ('Avatar', 7.2),
    ("Pirates of the Caribbean: At World's End", 6.9),
    ('Spectre', 6.3),
    ('The Dark Knight Rises', 7.6),
    ('John Carter', 6.1),
    ('Spider-Man 3', 5.9),
    ('Tangled', 7.4),
    ('Avengers: Age of Ultron', 7.3),
    ('Harry Potter and the Half-Blood Prince', 7.4),
    ('Batman v Superman: Dawn of Justice', 5.7),
    ('Superman Returns', 5.4),
    ('Quantum of Solace', 6.1),
    ("Pirates of the Caribbean: Dead Man's Chest", 7.0),
)


def init():
    with psycopg2.connect(**DSN) as conn:
        with conn.cursor() as curs:
            curs.execute("DROP TABLE IF EXISTS movie;")
            curs.execute("CREATE TABLE movie (id serial PRIMARY KEY, title varchar, rating double precision);")
            for title, rating in MOVIES:
                curs.execute("INSERT INTO movie (title, rating) VALUES (%s, %s)", (title, rating))

    # Note that, unlike file objects or other resources, exiting the connection’s with block doesn’t close
    # the connection but only the transaction associated with it: a connection can be used in more than
    # a with statement and each with block is effectively wrapped in a separate transaction:
    conn.close()


def execute(query):
    with psycopg2.connect(**DSN) as conn:
        with conn.cursor() as curs:
            curs.execute(query)
            for data in curs:
                print(data)

    conn.close()


if __name__ == '__main__':
    init()
    execute("SELECT * FROM movie;")
    execute("SELECT * FROM movie ORDER BY rating DESC LIMIT 1;")
