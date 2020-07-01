# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'prueba.ui'
#
# Created by: PyQt5 UI code generator 5.14.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class VentanaPrincipal(object):
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
        self.groupBox.setGeometry(QtCore.QRect(30, 10, 631, 461))
        font = QtGui.QFont()
        font.setFamily("Menlo")
        self.groupBox.setFont(font)
        self.groupBox.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.groupBox.setMouseTracking(False)
        self.groupBox.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.groupBox.setAlignment(QtCore.Qt.AlignCenter)
        self.groupBox.setObjectName("groupBox")
        self.btn_autos = QtWidgets.QPushButton(self.groupBox)
        self.btn_autos.setGeometry(QtCore.QRect(370, 70, 171, 91))
        self.btn_autos.setObjectName("btn_autos")
        self.btn_clientes = QtWidgets.QPushButton(self.groupBox)
        self.btn_clientes.setGeometry(QtCore.QRect(50, 70, 171, 91))
        self.btn_clientes.setObjectName("btn_clientes")
        self.btn_servicios = QtWidgets.QPushButton(self.groupBox)
        self.btn_servicios.setGeometry(QtCore.QRect(50, 220, 171, 91))
        self.btn_servicios.setObjectName("btn_servicios")
        self.btn_facturas = QtWidgets.QPushButton(self.groupBox)
        self.btn_facturas.setGeometry(QtCore.QRect(370, 220, 171, 91))
        self.btn_facturas.setObjectName("btn_facturas")
        self.btn_solicitud = QtWidgets.QPushButton(self.groupBox)
        self.btn_solicitud.setGeometry(QtCore.QRect(180, 350, 221, 81))
        self.btn_solicitud.setObjectName("btn_solicitud")
        self.ayuda = QtWidgets.QPushButton(self.groupBox)
        self.ayuda.setGeometry(QtCore.QRect(500, 390, 97, 27))
        self.ayuda.setObjectName("ayuda")
        self.label = QtWidgets.QLabel(self.groupBox)
        self.label.setGeometry(QtCore.QRect(56, 20, 471, 31))
        self.label.setObjectName("label")
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
        self.groupBox.setTitle(_translate("MainWindow", "Inicio"))
        self.btn_autos.setText(_translate("MainWindow", "Autos"))
        self.btn_clientes.setText(_translate("MainWindow", "Clientes"))
        self.btn_servicios.setText(_translate("MainWindow", "Servicios"))
        self.btn_facturas.setText(_translate("MainWindow", "facturas"))
        self.btn_solicitud.setText(_translate("MainWindow", "Solicitar Servicios"))
        self.ayuda.setText(_translate("MainWindow", "ayuda"))
        self.label.setText(_translate("MainWindow", "Bienvenido al sistema de gestion de concesionario"))
from PyQt5 import QtQuickWidgets
