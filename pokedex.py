from imports import *
from PyQt5.QtWidgets import QApplication, QMainWindow
import sys

class UiPokedex(QMainWindow, Ui_pokedex):
    def __init__(self) -> None:
        super(UiPokedex, self).__init__()
        self.setupUi(self)
        self.setWindowTitle("Pokédex Simpá7ica")

        self.BtnNext.clicked.connect(self.next_picture)

def inicia_app():
    window.show()
    sys.exit(app.exec())

app = QApplication(sys.argv)
window = UiPokedex()

inicia_app()
