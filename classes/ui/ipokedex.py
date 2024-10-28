# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\dev10\Desktop\Escola\Pokedex\classes\ui\ipokedex.ui'
#
# Created by: PyQt5 UI code generator 5.15.11
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_pokedex(object):
    def setupUi(self, pokedex):
        pokedex.setObjectName("pokedex")
        pokedex.resize(605, 605)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(pokedex.sizePolicy().hasHeightForWidth())
        pokedex.setSizePolicy(sizePolicy)
        pokedex.setMinimumSize(QtCore.QSize(605, 605))
        pokedex.setMaximumSize(QtCore.QSize(605, 600))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("C:\\Users\\dev10\\Desktop\\Escola\\Pokedex\\classes\\ui\\../../img/pokeball.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        pokedex.setWindowIcon(icon)
        pokedex.setTabShape(QtWidgets.QTabWidget.Triangular)
        self.centralwidget = QtWidgets.QWidget(pokedex)
        self.centralwidget.setObjectName("centralwidget")
        self.FramePrincipal = QtWidgets.QFrame(self.centralwidget)
        self.FramePrincipal.setGeometry(QtCore.QRect(0, 0, 621, 591))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.FramePrincipal.sizePolicy().hasHeightForWidth())
        self.FramePrincipal.setSizePolicy(sizePolicy)
        self.FramePrincipal.setAutoFillBackground(False)
        self.FramePrincipal.setStyleSheet("background-color:#FFFFFF")
        self.FramePrincipal.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.FramePrincipal.setFrameShadow(QtWidgets.QFrame.Raised)
        self.FramePrincipal.setObjectName("FramePrincipal")
        self.LbImagem = QtWidgets.QLabel(self.FramePrincipal)
        self.LbImagem.setGeometry(QtCore.QRect(320, 70, 220, 220))
        self.LbImagem.setStyleSheet("")
        self.LbImagem.setText("")
        self.LbImagem.setPixmap(QtGui.QPixmap("C:\\Users\\dev10\\Desktop\\Escola\\Pokedex\\classes\\ui\\img/pokemons/bulbasaur.png"))
        self.LbImagem.setAlignment(QtCore.Qt.AlignCenter)
        self.LbImagem.setObjectName("LbImagem")
        self.LbTipo1 = QtWidgets.QLabel(self.FramePrincipal)
        self.LbTipo1.setGeometry(QtCore.QRect(30, 130, 181, 51))
        self.LbTipo1.setStyleSheet("border: 2px solid black;\n"
"border-radius: 20px;\n"
"background-color: purple\n"
"")
        self.LbTipo1.setText("")
        self.LbTipo1.setTextFormat(QtCore.Qt.AutoText)
        self.LbTipo1.setAlignment(QtCore.Qt.AlignCenter)
        self.LbTipo1.setObjectName("LbTipo1")
        self.LbTipo2 = QtWidgets.QLabel(self.FramePrincipal)
        self.LbTipo2.setGeometry(QtCore.QRect(30, 210, 181, 51))
        self.LbTipo2.setStyleSheet("border: 2px solid black;\n"
"border-radius: 20px;\n"
"background-color: green\n"
"\n"
"")
        self.LbTipo2.setText("")
        self.LbTipo2.setAlignment(QtCore.Qt.AlignCenter)
        self.LbTipo2.setObjectName("LbTipo2")
        self.BtnPrevious = QtWidgets.QPushButton(self.FramePrincipal)
        self.BtnPrevious.setGeometry(QtCore.QRect(30, 320, 261, 61))
        self.BtnPrevious.setStyleSheet("border: 1px solid black;\n"
"border-radius: 20px;")
        self.BtnPrevious.setObjectName("BtnPrevious")
        self.BtnNext = QtWidgets.QPushButton(self.FramePrincipal)
        self.BtnNext.setGeometry(QtCore.QRect(320, 320, 261, 61))
        self.BtnNext.setStyleSheet("border: 1px solid black;\n"
"border-radius: 20px;")
        self.BtnNext.setObjectName("BtnNext")
        self.LbDescricao = QtWidgets.QLabel(self.FramePrincipal)
        self.LbDescricao.setGeometry(QtCore.QRect(30, 410, 551, 161))
        self.LbDescricao.setStyleSheet("border: 1px solid black;\n"
"padding: 15px;\n"
"background-color: #BEBEBE")
        self.LbDescricao.setText("")
        self.LbDescricao.setTextFormat(QtCore.Qt.PlainText)
        self.LbDescricao.setWordWrap(True)
        self.LbDescricao.setObjectName("LbDescricao")
        self.LbNome = QtWidgets.QLabel(self.FramePrincipal)
        self.LbNome.setGeometry(QtCore.QRect(160, 10, 281, 51))
        self.LbNome.setStyleSheet("border: 1px solid black;\n"
"font-size: 24px; \n"
"font-weight: bold;\n"
"background-color: #BEBEBE;")
        self.LbNome.setFrameShape(QtWidgets.QFrame.WinPanel)
        self.LbNome.setFrameShadow(QtWidgets.QFrame.Plain)
        self.LbNome.setText("")
        self.LbNome.setAlignment(QtCore.Qt.AlignCenter)
        self.LbNome.setObjectName("LbNome")
        pokedex.setCentralWidget(self.centralwidget)

        self.retranslateUi(pokedex)
        QtCore.QMetaObject.connectSlotsByName(pokedex)

    def retranslateUi(self, pokedex):
        _translate = QtCore.QCoreApplication.translate
        pokedex.setWindowTitle(_translate("pokedex", "MainWindow"))
        self.BtnPrevious.setText(_translate("pokedex", "Anterior"))
        self.BtnNext.setText(_translate("pokedex", "Próximo"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    pokedex = QtWidgets.QMainWindow()
    ui = Ui_pokedex()
    ui.setupUi(pokedex)
    pokedex.show()
    sys.exit(app.exec_())