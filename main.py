from PyQt5 import QtWidgets, QtGui
from ventanas.principal import VentanaPrincipal
from ventanas.ayuda import VentanaAyuda
from ventanas.modulo import VentanaModulo
from ventanas.busqueda import VentanaBusqueda
import modelos
import sys

class Ventana(QtWidgets.QMainWindow):
    def __init__(self):
       super(Ventana, self).__init__()
       self.inicio()

    def inicio(self):
        self.ui = VentanaPrincipal()
        self.ui.setupUi(self)
        self.ui.ayuda.clicked.connect(self.ayuda)
        self.ui.btn_autos.clicked.connect(self.clientes)
        self.ui.btn_clientes.clicked.connect(self.autos)
        self.ui.btn_servicios.clicked.connect(self.servicios)
        self.ui.btn_facturas.clicked.connect(self.facturas)
        self.ui.btn_solicitud.clicked.connect(self.solicitud)
     
    def ayuda(self):
        self.ui = VentanaAyuda()
        self.ui.setupUi(self)
        ayuda = open("archivos/Ayuda.txt")
        self.ui.texto_ayuda.append("<span style=\" color: #101E0D;\">"+ayuda.read()+"</span>") #se añade a la casilla de texto con un xml
        self.ui.btn_inicio.clicked.connect(self.inicio)

    def clientes(self):
        self.ui = VentanaModulo()
        self.ui.setupUi(self)
        self.ui.etiqueta_tipo.setText("clientes")
        self.ui.btn_inicio.clicked.connect(self.inicio)


    def autos(self):
        self.ui = VentanaModulo()
        self.ui.setupUi(self)
        self.ui.etiqueta_tipo.setText("autos")
        self.ui.btn_inicio.clicked.connect(self.inicio)
    
    def servicios(self):
        self.ui = VentanaModulo()
        self.ui.setupUi(self)
        self.ui.etiqueta_tipo.setText("servicios")
        self.ui.btn_inicio.clicked.connect(self.inicio)
        
    def facturas(self):
        self.ui = VentanaModulo()
        self.ui.setupUi(self)
        self.ui.creacion.hide()
        self.ui.etiqueta_tipo.setText("facturas")
        self.ui.btn_inicio.clicked.connect(self.inicio)
    def solicitud(self):
        self.ui.groupBox.hide()

app = QtWidgets.QApplication([])
application = Ventana()
application.show()
sys.exit(app.exec())
