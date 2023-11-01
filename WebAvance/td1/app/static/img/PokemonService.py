from typing import List, Dict

from WebAvance.td1.app.models.PokemonDAO import PokemonJsonDAO


class PokemonService():
    """
    Class dedicated for the logic behind the pokemons
    """

    def __init__(self):
        # this line uses the Data Access Object (DAO) dedicated to json file
        self.pdao = PokemonJsonDAO()

    def getPokemonByNumber(self, num) -> List[Dict]:
        res = [self.pdao.findByNumber(num)]
        return res

    def getPokemonTypes(self) -> List:
        # here is an example of where the service shines compared to the DAO
        # (this logic can work independently to the way we retrieve data)
        return list(set([pokemon["Type_1"] for pokemon in self.pdao.findAll()]))

    def getPokemonsByType(self, ptype) -> List[Dict]:
        res = self.pdao.findByType(ptype)
        if len(res) > 0: return res
        return [{}]
