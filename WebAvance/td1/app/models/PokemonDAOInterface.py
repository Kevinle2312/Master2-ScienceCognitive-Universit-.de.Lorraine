from typing import List, Dict


class PokemonDAOInterface():
    """ Interface for the pokemon dao """

    def findAll(self) -> List[Dict]:
        """ finds all the pokemons """
        pass

    def findByNumber(self, number: int) -> List[Dict]:
        """ finds by a pokemon by number in the database """
        pass

    def findByType(self, ptype: str) -> List[Dict]:
        """ finds all the pokemons with a dedicated type """
        pass
