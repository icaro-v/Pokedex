from imports import *
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5 import QtGui
import sys 
from database.db import pokemons_database, types_database

class UiPokedex(QMainWindow, Ui_pokedex):
    pokemons = [] 
    types = []

    def __init__(self) -> None:        
        super(UiPokedex, self).__init__()
        self.setupUi(self)
        self.setWindowTitle("Pokédex Simpá7ica")   

        self.load_types()
        self.load_pokemons()
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

    def load_types(self):
        self.types.append(t(0, '', ''))
        for type in types_database:
            self.types.append(t(type.id, type.name, type.color))

    def load_pokemons(self):
        self.pokemons.append(p(0, '', '', '', '')) 
        for pokemon in pokemons_database:
            self.pokemons.append(p(pokemon.id, pokemon.name, pokemon.type1.name, pokemon.type2.name if pokemon.type2 else '', '')) 
            for pokemon_type in self.types:
                if pokemon.type1.id == pokemon_type.id: 
                    self.pokemons[-1].type1 = pokemon_type

                if pokemon.type2 == None:
                    self.pokemons[-1].type2 = t(0, '', '')    
                elif pokemon.type2.id == pokemon_type.id:
                    self.pokemons[-1].type2 = pokemon.type2       

        self.current = 1
   
    def showInfo(self):
        caminho_imgs = 'C:\\Users\\dev10\\Desktop\\Escola\\Pokedex\\img\\pokemons\\'
        self.LbNome.setText(self.pokemons[self.current].name)
        self.LbImagem.setPixmap(QtGui.QPixmap(caminho_imgs+self.pokemons[self.current].name+'.png').scaled(220, 220))
        self.LbTipo1.setText(self.pokemons[self.current].type1.name)
        self.LbTipo1.setStyleSheet(self.styleSheet_padrao() + f"\nbackground-color: {self.pokemons[self.current].type1.color};")
        self.LbTipo2.setText(self.pokemons[self.current].type2.name)
        if self.pokemons[self.current].type2.name == '':            
            self.LbTipo2.setVisible(False)
        else:
            self.LbTipo2.setVisible(True)
            self.LbTipo2.setStyleSheet(self.styleSheet_padrao() + f"\nbackground-color: {self.pokemons[self.current].type2.color};")
        self.LbDescricao.setText(self.pokemons[self.current].description)       

        self.set_buttons()
    
    def styleSheet_padrao(self):
        return '''border: 2px solid black;
                  border-radius: 20px;'''
    

def inicia_app():
    window.show()
    sys.exit(app.exec())

app = QApplication(sys.argv)
window = UiPokedex()

inicia_app()
