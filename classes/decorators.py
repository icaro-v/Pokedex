from type import Type as t

class MainDecorator:
    def __init__(self, pokemon):
        self.pokemon = pokemon

class TypeDecorator(MainDecorator):
    def __init__(self, pokemon, types):
        super().__init__(pokemon)
        for pokemon_type in types:
            if pokemon.type1.id == pokemon_type.id: 
                pokemon.type1 = pokemon_type

            if pokemon.type2 == None:
                pokemon.type2 = t(0, '', '')    
            elif pokemon.type2.id == pokemon_type.id:
                pokemon.type2 = pokemon.type2       
