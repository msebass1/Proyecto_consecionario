# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'archivos_ventanas/modulo.ui'
#
# Created by: PyQt5 UI code generator 5.14.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class VentanaModulo(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(684, 575)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.quickWidget = QtQuickWidgets.QQuickWidget(self.centralwidget)
        self.quickWidget.setGeometry(QtCore.QRect(10, 0, 661, 541))
        self.quickWidget.setResizeMode(QtQuickWidgets.QQuickWidget.SizeRootObjectToView)
        self.quickWidget.setObjectName("quickWidget")
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(30, 10, 611, 481))
        self.groupBox.setTitle("")
        self.groupBox.setObjectName("groupBox")
        self.btn_inicio = QtWidgets.QPushButton(self.groupBox)
        self.btn_inicio.setGeometry(QtCore.QRect(60, 270, 161, 61))
        self.btn_inicio.setObjectName("btn_inicio")
        self.etiqueta_tipo = QtWidgets.QLabel(self.groupBox)
        self.etiqueta_tipo.setGeometry(QtCore.QRect(40, 20, 131, 51))
        font = QtGui.QFont()
        font.setFamily("Menlo")
        font.setPointSize(14)
        self.etiqueta_tipo.setFont(font)
        self.etiqueta_tipo.setObjectName("etiqueta_tipo")
        self.creacion = QtWidgets.QPushButton(self.groupBox)
        self.creacion.setGeometry(QtCore.QRect(60, 120, 151, 51))
        self.creacion.setObjectName("creacion")
        self.btn_Id = QtWidgets.QPushButton(self.groupBox)
        self.btn_Id.setGeometry(QtCore.QRect(320, 160, 281, 41))
        self.btn_Id.setObjectName("btn_Id")
        self.seleccion_id = QtWidgets.QComboBox(self.groupBox)
        self.seleccion_id.setGeometry(QtCore.QRect(350, 70, 201, 31))
        self.seleccion_id.setObjectName("seleccion_id")
        self.seleccion_id.addItem("")
        self.id = QtWidgets.QLineEdit(self.groupBox)
        self.id.setGeometry(QtCore.QRect(350, 110, 201, 31))
        self.id.setObjectName("id")
        self.seleccion_orden = QtWidgets.QComboBox(self.groupBox)
        self.seleccion_orden.setGeometry(QtCore.QRect(350, 260, 201, 31))
        self.seleccion_orden.setObjectName("seleccion_orden")
        self.seleccion_orden.addItem("")
        self.btn_orden = QtWidgets.QPushButton(self.groupBox)
        self.btn_orden.setGeometry(QtCore.QRect(320, 310, 281, 41))
        self.btn_orden.setObjectName("btn_orden")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 684, 25))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.btn_inicio.setText(_translate("MainWindow", "inicio"))
        self.etiqueta_tipo.setText(_translate("MainWindow", "Estado"))
        self.creacion.setText(_translate("MainWindow", "Crear"))
        self.btn_Id.setText(_translate("MainWindow", "Buscar por identificador"))
        self.seleccion_id.setItemText(0, _translate("MainWindow", "seleccione..."))
        self.id.setText(_translate("MainWindow", "ingrese el identificador"))
        self.seleccion_orden.setItemText(0, _translate("MainWindow", "seleccione..."))
        self.btn_orden.setText(_translate("MainWindow", "Buscar por orden"))
from PyQt5 import QtQuickWidgets
