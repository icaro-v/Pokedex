from ..controller.pokedex_controller import PokedexController as pc

class UiPokedexBuilder:
    def __init__(self):         
        self.pokedex = pc()

    def build(self):      
        return self.pokedex
