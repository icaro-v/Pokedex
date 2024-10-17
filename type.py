from entity import Entity

class Type(Entity):
    def __init__(self, id, name, color, strength, weakness):
        super().__init__(id, name)
        self.color = color
        self.strength = strength
        self.weakness = weakness
        