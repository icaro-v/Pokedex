from .entity import Entity

class Type(Entity):
    def __init__(self, id, name, color):
        super().__init__(id, name)
        self.color = color   

    def set_strengths(self, strengths):
        self.strengths = strengths

    def set_weaknesses(self, weaknesses):    
        self.weaknesses = weaknesses    
    