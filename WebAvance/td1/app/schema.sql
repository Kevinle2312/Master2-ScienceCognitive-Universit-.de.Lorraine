DROP TABLE IF EXISTS pokemons;

CREATE TABLE pokemons
(
    Number      INTEGER PRIMARY KEY AUTOINCREMENT,
    created     TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    Name        TEXT      NOT NULL,
    Type_1      TEXT      NOT NULL,
    Type_2      TEXT,
    Total       INTEGER,
    HP          INTEGER,
    Attack      INTEGER,
    Defense     INTEGER,
    Sp_Atk      INTEGER,
    Sp_Def      INTEGER,
    Speed       INTEGER,
    Generation  INTEGER,

    Color       TEXT,

    Pr_Male     REAL,
    Egg_Group_1 TEXT,
    Egg_Group_2 TEXT,

    Height_m    REAL,
    Weight_kg   REAL,
    Catch_Rate  INTEGER,
    Body_Style  TEXT

);