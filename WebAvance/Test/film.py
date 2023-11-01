from sqlalchemy import Column, Integer, String, TIMESTAMP
from sqlalchemy import create_engine, func
from sqlalchemy.orm import declarative_base, sessionmaker

# moteur déclaré avec notre base de données
engine = create_engine("sqlite:///films.db", echo=True)

# obtention de la base déclarative
Base = declarative_base()


class Film(Base):
    """ notre modèle de film qui hérite Base"""
    __tablename__ = "films"  # nom de la table de la BDD

    # colonne id primaire. Par defaut elle est auto incrementée
    id = Column(Integer, primary_key=True)
    # colonne de création de type timestamp avec valeur par défaut
    created = Column(TIMESTAMP, default=func.current_timestamp())
    # colonne de titre de type string qui ne peut pas être vide
    titre = Column(String, nullable=False)
    # colonne de qualité, un entier qui a 0 comme valeur par défaut
    qualite = Column(Integer, default=0)


def creation():
    """ fonction de création de la bdd """
    Base.metadata.create_all(engine)


def remplir():
    """ fonction de remplissage de la bdd """
    # on créer la classe sessino
    Session = sessionmaker(bind=engine)
    # on instancie la session
    session = Session()

    # voici une liste de tuples qui contiennent les infos pour chaque film
    data = [("2046", 10), ("Mon nom est personne", 7), ("Star Wars 7", 0)]
    # pour tous ces tuples, j'instancie la classe Film avec les infos et l'ajoute à une liste qui est ensuite assignée à la variable films
    films = [Film(titre=d[0], qualite=d[1]) for d in data]
    # j'ajoute tous ces éléments
    session.add_all(films)

    # ne pas oublier de commit pour vraiment effectuer les changements dans la BDD
    session.commit()
    # ne pas oublier de fermer la session d'accès à la BDD
    session.close()


def explorer():
    """ fonction pour explorer la BDD """
    Session = sessionmaker(bind=engine)
    session = Session()

    # je requête la table liée à la classe Film (___tablenme___) et demande tous les éléments présents .all()
    res = (session.query(Film).all())
    # pour chaque élément récupéré, j'affiche ses propriétés sous forme de dictionnaire
    for r in res:
        print(r.__dict__)

    # toujours fermer la session
    session.close()


# Maintenant je peux lancer une ou plusierus de ces fonctions à volonté 😛
creation()
remplir()
explorer()
