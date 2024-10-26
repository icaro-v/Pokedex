from peewee import JOIN
from database.connection import DatabaseSingleton
from database.models import Type, Pokemon

db = DatabaseSingleton.get_instance()
db.connect()
db.create_tables([Type, Pokemon], safe=True)

types_database = Type.select()

pokemons_database = (Pokemon
    .select(Pokemon, Type)
    .join(Type, on=Pokemon.type1 == Type.id)
    .join(Type.alias('type2'), on=(Pokemon.type2 == Type.alias('type2').id), join_type=JOIN.LEFT_OUTER)
    .order_by(Pokemon.id)
)