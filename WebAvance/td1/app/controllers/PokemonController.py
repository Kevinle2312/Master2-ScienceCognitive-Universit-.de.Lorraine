from flask import render_template, request

from WebAvance.td1.app import app
from WebAvance.td1.app.services.PokemonService import PokemonService

basepath = '/pokemon'

ps = PokemonService()


@app.route(basepath + '/<int:pokedex_id>', methods=['GET'])
def pokemonView(pokedex_id):
    pokemon_data = ps.getPokemonByNumber(pokedex_id)
    return render_template('pokemon.html', pokemons=pokemon_data)


@app.route(basepath, methods=["GET"])
def pokemonByIndex():
    # use form as a dictionary. the key is the name attribute of the HTML tag ;)
    pokedex_id = int(request.form['index'])
    pokemon_data = ps.getPokemonByNumber(pokedex_id)
    return render_template('pokemon.html', pokemons=pokemon_data)


@app.route(basepath + "/type", methods=["GET"])
def pokemonsByType():
    # use args.get to actually retrieve the correct value based on GET arguments
    ptype = request.args.get('pokemontype')
    pokemons = ps.getPokemonsByType(ptype)
    return render_template('pokemon.html', pokemons=pokemons)
