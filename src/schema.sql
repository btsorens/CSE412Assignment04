-- Drop the tables if recreating the database
DROP TABLE IF EXISTS gamestats;
DROP TABLE IF EXISTS players;

-- Create players table
CREATE TABLE players (
    player_id SERIAL PRIMARY KEY,
    first_name VARCHAR(50) NOT NULL,
    last_name VARCHAR(50) NOT NULL,
    date_of_birth DATE NOT NULL CHECK (date_of_birth BETWEEN '1970-01-01' AND '2010-12-31'),
    hometown VARCHAR(100),
    state VARCHAR(2),
    position VARCHAR(10),
    height INTEGER CHECK (height BETWEEN 68 and 80),
    weight INTEGER CHECK (weight BETWEEN 150 and 300),
    jersey_number INTEGER CHECK (jersey_number BETWEEN 0 and 99)
);

CREATE TABLE gamestats (
    stat_id SERIAL PRIMARY KEY,
    player_id INTEGER REFERENCES players(player_id) ON DELETE CASCADE,
    date_of_game DATE NOT NULL,
    stadium_name VARCHAR(100),
    rush_yards INTEGER DEFAULT 0,
    num_rushes INTEGER DEFAULT 0,
    rec_yards INTEGER DEFAULT 0,
    num_receptions INTEGER DEFAULT 0,
    points INTEGER DEFAULT 0,
    snaps_played INTEGER CHECK (snaps_played >= 0)
);