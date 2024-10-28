from imports import UiPokedexBuilder, sys
from PyQt5.QtWidgets import QApplication


app = QApplication(sys.argv)
builder = UiPokedexBuilder()
pokedex = builder.build()
pokedex.show()
sys.exit(app.exec())
