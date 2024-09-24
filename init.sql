-- Create the database
CREATE DATABASE IF NOT EXISTS basketball_db;
USE basketball_db;

-- Table: players
CREATE TABLE players (
  bioID VARCHAR(255),
  pos VARCHAR(255),
  firstseason INT,
  lastseason INT,
  height FLOAT,
  weight INT,
  college VARCHAR(255),
  collegeOther VARCHAR(255),
  birthDate VARCHAR(255),
  deathDate VARCHAR(255),
  PRIMARY KEY (bioID)
);

-- Table: teams (with explicit index on tmID and lgID)
CREATE TABLE teams (
  year INT,
  lgID VARCHAR(255),
  tmID VARCHAR(255),
  franchID VARCHAR(255),
  confID VARCHAR(255),
  divID VARCHAR(255),
  `rank` INT,  -- Enclose rank in backticks since it's a reserved keyword
  playoff VARCHAR(255),
  seeded INT,
  firstRound VARCHAR(255),
  semis VARCHAR(255),
  finals VARCHAR(255),
  name VARCHAR(255),
  o_fgm INT,
  o_fga INT,
  o_ftm INT,
  o_fta INT,
  o_3pm INT,
  o_3pa INT,
  o_oreb INT,
  o_dreb INT,
  o_reb INT,
  o_asts INT,
  o_pf INT,
  o_stl INT,
  o_to INT,
  o_blk INT,
  o_pts INT,
  d_fgm INT,
  d_fga INT,
  d_ftm INT,
  d_fta INT,
  d_3pm INT,
  d_oreb INT,
  d_dreb INT,
  d_reb INT,
  d_asts INT,
  d_pf INT,
  d_stl INT,
  d_to INT,
  d_blk INT,
  d_pts INT,
  tmORB INT,
  tmDRB INT,
  tmTRB INT,
  opptmORB INT,
  opptmDRB INT,
  opptmTRB INT,
  won INT,
  lost INT,
  GP INT,
  homeW INT,
  homeL INT,
  awayW INT,
  awayL INT,
  confW INT,
  confL INT,
  min INT,
  attend INT,
  arena VARCHAR(255),
  PRIMARY KEY (year, tmID),
  INDEX (tmID),  -- Explicit index on tmID
  INDEX (lgID)   -- Explicit index on lgID
);

-- Table: awards_players
CREATE TABLE awards_players (
  playerID VARCHAR(255),
  award VARCHAR(255),
  year INT,
  lgID VARCHAR(255),
  PRIMARY KEY (playerID, award, year),
  FOREIGN KEY (playerID) REFERENCES players(bioID) ON DELETE CASCADE
);

-- Table: coaches
CREATE TABLE coaches (
  coachID VARCHAR(255),
  year INT,
  tmID VARCHAR(255),
  lgID VARCHAR(255),
  stint INT,
  won INT,
  lost INT,
  post_wins INT,
  post_losses INT,
  PRIMARY KEY (coachID, year, tmID, stint),
  FOREIGN KEY (tmID) REFERENCES teams(tmID) ON DELETE CASCADE,  -- Foreign key constraint to teams.tmID
  FOREIGN KEY (lgID) REFERENCES teams(lgID) ON DELETE CASCADE   -- Foreign key constraint to teams.lgID
);

-- Table: players_teams
CREATE TABLE players_teams (
  playerID VARCHAR(255),
  year INT,
  stint INT,
  tmID VARCHAR(255),
  lgID VARCHAR(255),
  GP INT,
  GS INT,
  minutes INT,
  points INT,
  oRebounds INT,
  dRebounds INT,
  rebounds INT,
  assists INT,
  steals INT,
  blocks INT,
  turnovers INT,
  PF INT,
  fgAttempted INT,
  fgMade INT,
  ftAttempted INT,
  ftMade INT,
  threeAttempted INT,
  threeMade INT,
  dq INT,
  PostGP INT,
  PostGS INT,
  PostMinutes INT,
  PostPoints INT,
  PostoRebounds INT,
  PostdRebounds INT,
  PostRebounds INT,
  PostAssists INT,
  PostSteals INT,
  PostBlocks INT,
  PRIMARY KEY (playerID, year, stint, tmID),
  FOREIGN KEY (playerID) REFERENCES players(bioID) ON DELETE CASCADE,
  FOREIGN KEY (tmID) REFERENCES teams(tmID) ON DELETE CASCADE,  -- Foreign key to teams.tmID
  FOREIGN KEY (lgID) REFERENCES teams(lgID) ON DELETE CASCADE   -- Foreign key to teams.lgID
);

-- Table: series_post
CREATE TABLE series_post (
  year INT,
  round VARCHAR(255),
  series VARCHAR(255),
  tmIDWinner VARCHAR(255),
  lgIDWinner VARCHAR(255),
  tmIDLoser VARCHAR(255),
  lgIDLoser VARCHAR(255),
  W INT,
  L INT,
  PRIMARY KEY (year, series),
  FOREIGN KEY (tmIDWinner) REFERENCES teams(tmID) ON DELETE CASCADE,
  FOREIGN KEY (tmIDLoser) REFERENCES teams(tmID) ON DELETE CASCADE,
  FOREIGN KEY (lgIDWinner) REFERENCES teams(lgID) ON DELETE CASCADE,
  FOREIGN KEY (lgIDLoser) REFERENCES teams(lgID) ON DELETE CASCADE
);

-- Table: teams_post
CREATE TABLE teams_post (
  year INT,
  tmID VARCHAR(255),
  lgID VARCHAR(255),
  W INT,
  L INT,
  PRIMARY KEY (year, tmID),
  FOREIGN KEY (tmID) REFERENCES teams(tmID) ON DELETE CASCADE,
  FOREIGN KEY (lgID) REFERENCES teams(lgID) ON DELETE CASCADE
);

-- Load data from CSV files
-- Load data from CSV files

LOAD DATA INFILE '/docker-entrypoint-initdb.d/players.csv'
INTO TABLE players
FIELDS TERMINATED BY ',' 
ENCLOSED BY '"'
LINES TERMINATED BY '\n'
IGNORE 1 ROWS;


LOAD DATA INFILE '/docker-entrypoint-initdb.d/teams.csv'
INTO TABLE teams
FIELDS TERMINATED BY ',' 
ENCLOSED BY '"'
LINES TERMINATED BY '\n'
IGNORE 1 ROWS;

LOAD DATA INFILE '/docker-entrypoint-initdb.d/awards_players.csv'
INTO TABLE awards_players
FIELDS TERMINATED BY ',' 
ENCLOSED BY '"'
LINES TERMINATED BY '\n'
IGNORE 1 ROWS;

LOAD DATA INFILE '/docker-entrypoint-initdb.d/coaches.csv'
INTO TABLE coaches
FIELDS TERMINATED BY ',' 
ENCLOSED BY '"'
LINES TERMINATED BY '\n'
IGNORE 1 ROWS;

LOAD DATA INFILE '/docker-entrypoint-initdb.d/players_teams.csv'
INTO TABLE players_teams
FIELDS TERMINATED BY ',' 
ENCLOSED BY '"'
LINES TERMINATED BY '\n'
IGNORE 1 ROWS;

LOAD DATA INFILE '/docker-entrypoint-initdb.d/series_post.csv'
INTO TABLE series_post
FIELDS TERMINATED BY ',' 
ENCLOSED BY '"'
LINES TERMINATED BY '\n'
IGNORE 1 ROWS;

LOAD DATA INFILE '/docker-entrypoint-initdb.d/teams_post.csv'
INTO TABLE teams_post
FIELDS TERMINATED BY ',' 
ENCLOSED BY '"'
LINES TERMINATED BY '\n'
IGNORE 1 ROWS;
