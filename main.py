from PyQt5 import QtWidgets, QtGui
from ventanas.principal import VentanaPrincipal
from ventanas.ayuda import VentanaAyuda
from ventanas.modulo import VentanaModulo
from ventanas.busqueda import VentanaBusqueda
from ventanas.creacion import VentanaCreacion
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
        self.ui.btn_autos.clicked.connect(self.autos)
        self.ui.btn_clientes.clicked.connect(self.clientes)
        self.ui.btn_facturas.clicked.connect(self.facturas)
        self.ui.btn_solicitud.clicked.connect(self.solicitud)
        self.ui.btn_servicios.clicked.connect(self.servicios)
     
    def ayuda(self):
        self.ui = VentanaAyuda()
        self.ui.setupUi(self)
        ayuda = open("archivos/Ayuda.txt")
        self.ui.texto_ayuda.append("<span style=\" color: #101E0D;\">"+ayuda.read()+"</span>") #se añade a la casilla de texto con un xml
        self.ui.btn_inicio.clicked.connect(self.inicio)

    def clientes(self):
        self.tipo = "cliente"
        self.ui = VentanaModulo()
        self.ui.setupUi(self)
        self.setupSeleccion()
        self.ui.etiqueta_tipo.setText(self.tipo)
        self.ui.btn_inicio.clicked.connect(self.inicio)
        self.ui.btn_orden.clicked.connect(self.busquedaOrden)
        self.ui.btn_Id.clicked.connect(self.busquedaId)
        self.ui.creacion.clicked.connect(self.crear)

    def autos(self):
        self.tipo = "auto"
        self.ui = VentanaModulo()
        self.ui.setupUi(self)
        self.setupSeleccion()
        self.ui.etiqueta_tipo.setText("autos")
        self.ui.btn_inicio.clicked.connect(self.inicio)
        self.ui.btn_orden.clicked.connect(self.busquedaOrden)
        self.ui.btn_Id.clicked.connect(self.busquedaId)
        self.ui.creacion.clicked.connect(self.crear)
    
    def servicios(self):
        self.tipo = "servicio"
        self.ui = VentanaModulo()
        self.ui.setupUi(self)
        self.setupSeleccion()
        self.ui.etiqueta_tipo.setText("servicios")
        self.ui.btn_inicio.clicked.connect(self.inicio)
        self.ui.btn_orden.clicked.connect(self.busquedaOrden)
        self.ui.btn_Id.clicked.connect(self.busquedaId)
        self.ui.creacion.clicked.connect(self.crear)

    def facturas(self):
        self.tipo = "factura"
        self.ui = VentanaModulo()
        self.ui.setupUi(self)
        self.setupSeleccion()
        self.ui.creacion.hide()
        self.ui.etiqueta_tipo.setText("facturas")
        self.ui.btn_inicio.clicked.connect(self.inicio)
        self.ui.btn_orden.clicked.connect(self.busquedaOrden)
        self.ui.btn_Id.clicked.connect(self.busquedaId)

    def solicitud(self):
        self.ui.groupBox.hide()

    def setupSeleccion(self):
        elementos = archivo.leerinfo(self.tipo)
        for elemen in elementos:
            self.ui.seleccion_orden.addItem(elemen)
            self.ui.seleccion_id.addItem(elemen)

    def busquedaId(self):
        identificador = self.ui.id.text()
        seleccion = self.ui.seleccion_id.currentText()
        datos = archivo.busqueda_identificador("archivos/BD_"+self.tipo+"s.txt",seleccion,identificador)
        self.busqueda(datos)

    def busquedaOrden(self):
        seleccion = self.ui.seleccion_orden.currentText() #no cambiar el orden
        datos = (archivo.busqueda_orden("archivos/BD_"+self.tipo+"s.txt",seleccion)) 
        self.busqueda(datos)
        
    def busqueda(self, datos):
        self.ui = VentanaBusqueda()
        self.ui.setupUi(self)
        self.ui.btn_inicio.clicked.connect(self.inicio)

        self.ui.tabla_busqueda.setColumnCount(len(datos[0].keys()))
        self.ui.tabla_busqueda.setRowCount(len(datos)+1)

        i = 0 
        j = 1
        for caracteristica in datos[0].keys():
            self.ui.tabla_busqueda.setItem(0,i,QtWidgets.QTableWidgetItem(caracteristica))
            i += 1 
            for dato in datos:
               self.ui.tabla_busqueda.setItem(j,i-1,QtWidgets.QTableWidgetItem(dato[caracteristica]))
               j += 1
            j = 1

    def crear(self):
        self.ui = VentanaCreacion()
        self.ui.setupUi(self)
        self.ui.btn_inicio.clicked.connect(self.inicio)
        elementos = archivo.leerinfo(self.tipo)
        for elemento in elementos:
            print(elemento)                


app = QtWidgets.QApplication([])
application = Ventana()
application.show()
archivo = modelos.Principal("persona") 
sys.exit(app.exec())
