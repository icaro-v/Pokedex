from imports import *
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5 import QtGui
import sys

class UiPokedex(QMainWindow, Ui_pokedex):
    pokemons = []

    def __init__(self) -> None:        
        super(UiPokedex, self).__init__()
        self.setupUi(self)
        self.setWindowTitle("Pokédex Simpá7ica")   

        self.carrega_pokemos()
        self.showInfo()
        
        self.BtnNext.clicked.connect(self.next_poke)
        self.BtnPrevious.clicked.connect(self.previous_poke) 
    
    def set_buttons(self):
        if self.current == len(self.pokemons) - 1:
           self.BtnNext.setEnabled(False)
        
        if self.current < len(self.pokemons) - 1:
           self.BtnNext.setEnabled(True)
        
        if self.current > 1:
           self.BtnPrevious.setEnabled(True) 

        if self.current == 1:
           self.BtnPrevious.setEnabled(False)

    def next_poke(self):
        self.current += 1
        self.showInfo()

    def previous_poke(self):   
        self.current -= 1    
        self.showInfo()

    def carrega_pokemos(self):
        self.pokemons.append(Pokemon(0, '', '', '', '', '')) 
        self.pokemons.append(Pokemon(1, 'charmander', 'fogo', '', 'Lagarto de fogo', 'C:\\Users\\dev10\\Desktop\\Pokedex\\img\\pokemons\\charmander.png'))    
        self.pokemons.append(Pokemon(2, 'charmeleon', 'fogo', '', 'Lagarto de fogo evoluído', 'C:\\Users\\dev10\\Desktop\\Pokedex\\img\\pokemons\\charmeleon.png'))
        self.pokemons.append(Pokemon(3, 'charizard', 'fogo', 'voador', 'Lagarto de fogo voador (melhor pokémon de todos)', 'C:\\Users\\dev10\\Desktop\\Pokedex\\img\\pokemons\\charizard.png'))

        self.current = 1
   
    def showInfo(self):
        self.LbNome.setText(self.pokemons[self.current].name)
        self.LbImagem.setPixmap(QtGui.QPixmap(self.pokemons[self.current].picture)) 
        self.LbTipo1.setText(self.pokemons[self.current].type1)
        self.LbTipo2.setText(self.pokemons[self.current].type2)
        self.LbDescricao.setText(self.pokemons[self.current].description)       

        self.set_buttons()
    

def inicia_app():
    window.show()
    sys.exit(app.exec())

app = QApplication(sys.argv)
window = UiPokedex()

inicia_app()
