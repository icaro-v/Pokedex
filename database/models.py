from peewee import Model, CharField, ForeignKeyField
from database.connection import DatabaseSingleton

class BaseModel(Model):
    class Meta:
        database = DatabaseSingleton.get_instance()

class Type(BaseModel):
    name = CharField()
    color = CharField()    

class Pokemon(BaseModel):
    name = CharField()
    type1 = ForeignKeyField(Type, backref='pokemons_type1', column_name='type1')
    type2 = ForeignKeyField(Type, backref='pokemons_type2', null=True, column_name='type2') 
    description = CharField() 
