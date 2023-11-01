import json
import sqlite3
from typing import List, Dict

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
from termcolor import colored

from WebAvance.td1.app import app
from WebAvance.td1.app.models.Pokemon import Pokemon
from WebAvance.td1.app.models.PokemonDAOInterface import PokemonDAOInterface


class PokemonJsonDAO():
    """
    Pokemon data access object dedicated to the JSON file access
    """

    def __init__(self):
        with open(app.static_folder + "/data/pokemons.json") as f:
            print(colored('opening', 'red'))
            self.pokemons = json.load(f)

    def findAll(self) -> List[Dict]:
        """ finds all the pokemons """
        return self.pokemons

    def findByNumber(self, number) -> List[Dict]:
        """ finds by a pokemon by number in the database """
        for pokemon in self.pokemons:
            if pokemon["Number"] == number:
                return pokemon
        return [{}]

    def findByType(self, ptype) -> List[Dict]:
        """ finds all the pokemons with a dedicated type """
        pokemons = [pokemon for pokemon in self.pokemons if pokemon['Type_1'] == ptype]
        return pokemons


class PokemonSqliteDAO(PokemonDAOInterface):
    """
        Pokemon data access object dedicated to sqllite
    """

    def __init__(self):
        self.databasename = app.root_path + '/database.db'

    def getDbConnection(self):
        """ connect the database and returns the connection object """
        conn = sqlite3.connect(self.databasename)
        conn.row_factory = sqlite3.Row
        return conn

    def res2listOfJson(self, dboutput):
        """ transforms an output from the databse into a list of dictionaries"""
        return [{k: item[k] for k in item.keys()} for item in dboutput]

    def findAll(self):
        """ finds all the pokemons """
        conn = self.getDbConnection()
        pokemons = conn.execute('SELECT * FROM pokemons').fetchall()
        pokemons = self.res2listOfJson(pokemons)
        conn.close()
        return pokemons

    def findByNumber(self, number) -> List[Dict]:
        """ finds by a pokemon by number in the database """
        conn = self.getDbConnection()
        pokemons = conn.execute("SELECT * FROM pokemons WHERE Number = ?", (str(number)))
        pokemons = self.res2listOfJson(pokemons)
        conn.close()
        return pokemons[0]

    def findByType(self, ptype: str) -> List[Dict]:
        """ finds all the pokemons with a specific type (Type 1)"""
        conn = self.getDbConnection()
        pokemons = conn.execute("SELECT * FROM pokemons WHERE Type_1 = ?", (ptype,))
        pokemons = self.res2listOfJson(pokemons)
        conn.close()
        return pokemons


class PokemonSqliteORM(PokemonDAOInterface):
    """
    Cette classe hérite encore une fois de l'interface. Elle est dédiée à l'ORM
    Note : de bons commentaires sont des commentaires en anglais. Le français est ici uniquement pour le cours.
    Pokemon data access object dedicated to sqlite ORM with sqlalchemy
    """

    # on crée le moteur à l'aide du chemin de la base de données (mis  dans la config de l'app pour plus de propreté)
    engine = create_engine(app.config['SQLALCHEMY_DATABASE_URI'])
    # on initialise une base déclarative de sqlalchemy
    Base = declarative_base()

    def connect(self):
        """
        commence la session de transaction avec la bdd
        start the transaction session for the database
        """
        # on créer la classe session grace au sessionmaker qu'on lie (bind) avec le moteur
        Session = sessionmaker(bind=PokemonSqliteORM.engine)
        # on instancie la classe session
        session = Session()
        return session

    def findAll(self) -> List[Dict]:
        """ finds all the pokemons """
        # on connecte la bdd
        session = self.connect()
        # la requete (query) donne une liste d'instance de la classe Pokemon
        res = (session.query(Pokemon).all())
        # nous n'avons plus besoin de la bdd donc on ferme la session
        session.close()
        # pour ne pas changer notre service, nous prenons ces pokemons au format dictionnaire
        res = [r.__dict__ for r in res]
        return res

    def findByNumber(self, number: int) -> List[Dict]:
        """ finds by a pokemon by number in the database """
        # on connecte la bdd
        session = self.connect()
        # on demande tous les pokémons avec une valeur spécifique dans Number
        # la requete (query) donne une liste d'instance de la classe Pokemon
        res = (session.query(Pokemon).filter_by(Number=number))
        # nous n'avons plus besoin de la bdd donc on ferme la session
        session.close()
        # pour ne pas changer notre service, nous prenons ces pokemons au format dictionnaire
        res = [r.__dict__ for r in res]
        return res

    def findByType(self, ptype: str) -> List[Dict]:
        """ finds all the pokemons with a dedicated type """
        # on connecte la bdd
        session = self.connect()
        # on demande tous les pokémons avec une valeur spécifique dans Type_1
        # la requete (query) donne une liste d'instance de la classe Pokemon
        res = (session.query(Pokemon).filter_by(Type_1=ptype))
        # nous n'avons plus besoin de la bdd donc on ferme la session
        session.close()
        # pour ne pas changer notre service, nous prenons ces pokemons au format dictionnaire
        res = [r.__dict__ for r in res]
        return res
