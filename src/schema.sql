-- Drop the tables if recreating the database
DROP TABLE IF EXISTS gamestats;
DROP TABLE IF EXISTS players;

-- Create players table
CREATE TABLE players (
    player_id SERIAL PRIMARY KEY,
    first_name VARCHAR(50),
    last_name VARCHAR(50),
    date_of_birth DATE,
    hometown VARCHAR(100),
    state VARCHAR(2),
    position VARCHAR(10),
    height INTEGER,
    weight INTEGER,
    jersey_number INTEGER
);

CREATE TABLE gamestats (
    stat_id SERIAL PRIMARY KEY,
    player_id INTEGER REFERENCES players(player_id),
    date_of_game DATE,
    stadium_name VARCHAR(100),
    rush_yards INTEGER,
    num_rushes INTEGER,
    rec_yards INTEGER,
    num_receptions INTEGER,
    points INTEGER,
    snaps_played INTEGER
);