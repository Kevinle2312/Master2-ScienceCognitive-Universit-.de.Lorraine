from flask import render_template

from WebAvance.td1.app import app
from WebAvance.td1.app.static.img.PokemonService import PokemonService

ps = PokemonService()
basepath = '/'


@app.route(basepath, methods=['GET'])
def index():
    data = {
        "pokemontypes": ps.getPokemonTypes()
    }
    return render_template('index.html', data=data)
