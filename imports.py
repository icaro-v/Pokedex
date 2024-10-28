from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton, QLineEdit, QFrame, QVBoxLayout, QDialog, QLabel, QWidget, QFileDialog
from PySide6.QtCore import Qt, QSize, QCoreApplication
from PySide6.QtGui import QPixmap, QCursor, QIcon, QImage
import sys, os, socket, io, database.db as db
from classes.ui.ipokedex import Ui_pokedex
from classes.ui.ui_builder import UiPokedexBuilder
from classes.decorators import TypeDecorator
from classes.pokemon import Pokemon as p
from classes.type import Type as t
from classes.controller.pokedex_controller import PokedexController
