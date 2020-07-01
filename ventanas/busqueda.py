# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'archivos_ventanas/busqueda.ui'
#
# Created by: PyQt5 UI code generator 5.14.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class VentanaBusqueda(object):
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
        self.groupBox.setObjectName("groupBox")
        self.btn_inicio = QtWidgets.QPushButton(self.groupBox)
        self.btn_inicio.setGeometry(QtCore.QRect(500, 430, 97, 27))
        self.btn_inicio.setObjectName("btn_inicio")
        self.tabla_busqueda = QtWidgets.QTableWidget(self.groupBox)
        self.tabla_busqueda.setGeometry(QtCore.QRect(30, 40, 551, 351))
        self.tabla_busqueda.setObjectName("tabla_busqueda")
        self.tabla_busqueda.setColumnCount(0)
        self.tabla_busqueda.setRowCount(0)
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
        self.groupBox.setTitle(_translate("MainWindow", "Resultado Busqueda"))
        self.btn_inicio.setText(_translate("MainWindow", "inicio"))
from PyQt5 import QtQuickWidgets
