
from imports import UiPokedexBuilder, sys
from PyQt5.QtWidgets import QApplication

class PokedexApp:
    def __init__(self):
        self.app = QApplication(sys.argv)
        self.builder = UiPokedexBuilder()

    def run(self):
        pokedex = self.builder.build()
        pokedex.show()
        sys.exit(self.app.exec())  
