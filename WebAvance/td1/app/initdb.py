import json
import sqlite3

with open("static/data/pokemons.json") as f: pokemons = json.load(f)

connection = sqlite3.connect('database.db')

with open('schema.sql') as f:
    connection.executescript(f.read())

cur = connection.cursor()

for p in pokemons:
    cur.execute(
        "INSERT INTO pokemons (Name, Type_1, Generation) VALUES (?, ?, ?)",
        (p["Name"], p["Type_1"], p["Generation"])
    )
    print(p)

connection.commit()
connection.close()
