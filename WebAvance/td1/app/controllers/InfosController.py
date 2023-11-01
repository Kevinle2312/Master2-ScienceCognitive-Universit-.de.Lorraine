from flask import render_template

from WebAvance.td1.app import app

basepath = '/'


@app.route(basepath + 'infos', methods=['GET'])
def infos():
    return render_template('infos.html', data={"name": "Gaël", "favoriteFruit": "🍉"})
