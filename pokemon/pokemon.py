from entity import Entity

class Pokemon (Entity):
    def __init__(self, id, name, type1, type2, description):
        super().__init__(id, name)
        self.type1 = type1
        self.type2 = type2
        self.description = description
