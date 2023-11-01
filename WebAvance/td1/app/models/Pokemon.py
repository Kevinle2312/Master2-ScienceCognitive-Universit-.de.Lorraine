from sqlalchemy import Column, Integer, String, TIMESTAMP, func
from sqlalchemy.orm import declarative_base

# récupération de la base déclarative issue de SQLAlchemy
Base = declarative_base()


class Pokemon(Base):
    # nom de la table dans la bdd
    __tablename__ = "pokemons"

    # défini une colonne. Le premier argument est le nom de la colonne dans la bdd. Vous pouvez donc changer le nom
    # de la proporiété de la classe python
    Number = Column("Number", Integer, primary_key=True)  # auto_increment est le comportement par défaut
    created = Column(TIMESTAMP, default=func.current_timestamp())
    # avec l'argument nullable on peut spécifier si une colonne peut être non nulle
    Name = Column("Name", String, nullable=False)
    Type_1 = Column("Type_1", String, nullable=False)
    # il est important d'utiliser les types issus de SQLalchemy !
    Generation = Column("Generation", Integer, nullable=False)
