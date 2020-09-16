from PySide2 import QtWidgets

class App(QtWidgets.QWidget): #herite de qwidget...
    def __init__(self):
        super().__init__() # me permet d'init le qwidget ce qui reviens a => QtWidgets.QWidget.__init__()
        self.setWindowTitle("Convertisseur de devises by greg.B.")

app = QtWidgets.QApplication([]) # toujours  lui passer une liste vide sinon artoum ERROR
win =App()
win.show() # pour afficher la fenetre a l'utilsateur
app.exec_() # on execute la variable app