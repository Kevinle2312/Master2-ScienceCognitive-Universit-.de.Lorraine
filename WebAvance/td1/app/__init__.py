from flask import Flask

app = Flask(__name__, static_url_path='/static')
# il convient de bien ajouter le bon chemin de la bdd en configuration de l'app
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + app.root_path + '/database.db'

from WebAvance.td1.app.controllers import *
