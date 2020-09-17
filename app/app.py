from PySide2 import QtWidgets
import currency_converter

class App(QtWidgets.QWidget): #herite de qwidget...
    def __init__(self):
        super().__init__() # me permet d'init le qwidget ce qui reviens a => QtWidgets.QWidget.__init__()
        self.c = currency_converter.CurrencyConverter()
        self.setWindowTitle("Convertisseur de devises by greg.B.")
        self.setup_ui()
        self.set_default_values()
        self.setup_connections()
        self.setup_css()
        self.resize(500, 50)

    def setup_ui(self):
        self.layout = QtWidgets.QHBoxLayout(self) #self design le parent ou creer

        self.cbb_devisesFrom = QtWidgets.QComboBox() #combobox pas de parent on rajoute c'est tout
        self.spn_montant = QtWidgets.QSpinBox()
        self.cbb_devisesTo = QtWidgets.QComboBox()
        self.spn_montantConverti = QtWidgets.QSpinBox()

        self.btn_inverser = QtWidgets.QPushButton("inverser devises")

        self.layout.addWidget(self.cbb_devisesFrom)
        self.layout.addWidget(self.spn_montant)
        self.layout.addWidget(self.cbb_devisesTo)
        self.layout.addWidget(self.spn_montantConverti)
        self.layout.addWidget(self.btn_inverser)

    def set_default_values(self):
        self.cbb_devisesFrom.addItems(sorted(list(self.c.currencies))) # permet d'ajouter des objets dans la combobox, ici je convertie en liste les currencies
        self.cbb_devisesTo.addItems(sorted(list(self.c.currencies))) #idem
        self.cbb_devisesFrom.setCurrentText("EUR") # je definie le texte par default
        self.cbb_devisesTo.setCurrentText("EUR")

        self.spn_montant.setRange(1, 10000000) # on definie le range avant de mettre  la valeur par default sinon ca commence a zero et non 1
        self.spn_montantConverti.setRange(1, 10000000)
        self.spn_montant.setValue(100) # valeur par default
        self.spn_montantConverti.setValue(100)

    def setup_connections(self):
        self.cbb_devisesFrom.activated.connect(self.compute) # sur l'element cbb... si activé alors execute compute
        self.cbb_devisesTo.activated.connect(self.compute) # sur l'element cbb... si activé alors execute compute

        self.spn_montant.valueChanged.connect(self.compute) # idem mais quand la valeur change

        self.btn_inverser.clicked.connect(self.inverser_devise) #idem au clic

    def compute(self):
        montant = self.spn_montant.value()
        devise_from = self.cbb_devisesFrom.currentText()
        devise_to = self.cbb_devisesTo.currentText()

        try: #essai
            montant_converti = self.c.convert(montant, devise_from, devise_to) #
        except currency_converter.currency_converter.RateNotFoundError:
            print("la conversion n'a pas fonctionner")
        else: # si ok
            print(montant_converti)
            self.spn_montantConverti.setValue(montant_converti)

    def inverser_devise(self):
        devise_from = self.cbb_devisesFrom.currentText()
        devise_to = self.cbb_devisesTo.currentText()

        self.cbb_devisesFrom.setCurrentText(devise_to)
        self.cbb_devisesTo.setCurrentText(devise_from)

        self.compute()

    def setup_css(self):
        self.setStyleSheet("""
        background-color: rgb(30, 30, 30);
        color: rgb(240, 240, 240);
        border: 1px solid orange;
        text-align: center;
        """)
        self.btn_inverser.setStyleSheet("background-color: orange; color:black; ")



app = QtWidgets.QApplication([]) # toujours  lui passer une liste vide sinon artoum ERROR
win =App()
win.show() # pour afficher la fenetre a l'utilsateur
app.exec_() # on execute la variable app
