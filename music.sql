CREATE TABLE artist
(
id INTEGER PRIMARY KEY,
first_name TEXT,
last_name TEXT
);

CREATE TABLE album
(
id INTEGER PRIMARY KEY,
name TEXT,
artist_id INTEGER
);

CREATE TABLE song
(
id INTEGER PRIMARY KEY,
name TEXT,
track_number INTEGER,
song_length INTEGER,
album_id INTEGER
);

        