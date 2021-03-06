# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file './Fich_Designer/of_mantenimiento.ui'
#
# Created by: PyQt5 UI code generator 5.15.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Maintenance_Dialog(object):
    def setupUi(self, Maintenance_Dialog):
        Maintenance_Dialog.setObjectName("Maintenance_Dialog")
        Maintenance_Dialog.resize(419, 461)
        Maintenance_Dialog.setMinimumSize(QtCore.QSize(419, 461))
        Maintenance_Dialog.setMaximumSize(QtCore.QSize(419, 461))
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        Maintenance_Dialog.setFont(font)
        Maintenance_Dialog.setFocusPolicy(QtCore.Qt.NoFocus)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/capture.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Maintenance_Dialog.setWindowIcon(icon)
        Maintenance_Dialog.setToolTipDuration(-1)
        Maintenance_Dialog.setStyleSheet("QDialog{\n"
"background-color:qconicalgradient(cx:0.8125, cy:0.761, angle:0, stop:0 rgba(75, 151, 227, 255), stop:0.16 rgba(85, 170, 255, 255), stop:0.225 rgba(166, 140, 41, 255), stop:0.285 rgba(204, 181, 74, 255), stop:0.345 rgba(235, 219, 102, 255), stop:0.420455 rgba(63, 126, 189, 255), stop:0.52 rgba(209, 190, 76, 255), stop:0.57 rgba(73, 147, 221, 255), stop:0.635 rgba(168, 142, 42, 255), stop:0.695 rgba(202, 174, 68, 255), stop:0.75 rgba(223, 205, 8, 255), stop:0.815 rgba(208, 187, 73, 255), stop:0.88 rgba(170, 170, 0, 255), stop:0.935 rgba(137, 108, 26, 255), stop:1 rgba(172, 172, 172, 255))}")
        Maintenance_Dialog.setSizeGripEnabled(True)
        self.ok_button = QtWidgets.QPushButton(Maintenance_Dialog)
        self.ok_button.setGeometry(QtCore.QRect(80, 360, 93, 41))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.ok_button.setFont(font)
        self.ok_button.setStyleSheet("background-color:qlineargradient(spread:pad, x1:0.99005, y1:0.966, x2:0.945199, y2:0.068, stop:0.134328 rgba(141, 141, 141, 255), stop:1 rgba(255, 255, 255, 255))")
        self.ok_button.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/Apply.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.ok_button.setIcon(icon1)
        self.ok_button.setIconSize(QtCore.QSize(32, 32))
        self.ok_button.setFlat(False)
        self.ok_button.setObjectName("ok_button")
        self.cancel_button = QtWidgets.QPushButton(Maintenance_Dialog)
        self.cancel_button.setEnabled(False)
        self.cancel_button.setGeometry(QtCore.QRect(230, 360, 93, 41))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.cancel_button.setFont(font)
        self.cancel_button.setStyleSheet("background-color:qlineargradient(spread:pad, x1:0.99005, y1:0.966, x2:0.945199, y2:0.068, stop:0.134328 rgba(175, 175, 175, 255), stop:1 rgba(255, 255, 255, 255))")
        self.cancel_button.setObjectName("cancel_button")
        self.fich_oferta = QtWidgets.QLineEdit(Maintenance_Dialog)
        self.fich_oferta.setGeometry(QtCore.QRect(60, 120, 241, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.fich_oferta.setFont(font)
        self.fich_oferta.setStyleSheet("QLineEdit{color:rgb(0, 85, 255)}")
        self.fich_oferta.setAlignment(QtCore.Qt.AlignCenter)
        self.fich_oferta.setObjectName("fich_oferta")
        self.browse_offer = QtWidgets.QPushButton(Maintenance_Dialog)
        self.browse_offer.setGeometry(QtCore.QRect(310, 120, 41, 31))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.browse_offer.setFont(font)
        self.browse_offer.setFocusPolicy(QtCore.Qt.NoFocus)
        self.browse_offer.setStyleSheet("background-color:qlineargradient(spread:pad, x1:0.99005, y1:0.966, x2:0.945199, y2:0.068, stop:0.134328 rgba(164, 211, 255, 255), stop:1 rgba(255, 255, 255, 255))")
        self.browse_offer.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/Folder.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.browse_offer.setIcon(icon2)
        self.browse_offer.setObjectName("browse_offer")
        self.progreso = QtWidgets.QLabel(Maintenance_Dialog)
        self.progreso.setEnabled(True)
        self.progreso.setGeometry(QtCore.QRect(30, 290, 351, 41))
        font = QtGui.QFont()
        font.setItalic(True)
        self.progreso.setFont(font)
        self.progreso.setStyleSheet("background-color:rgb(255, 255, 255);\n"
"font-color:rgb(195, 0, 0)")
        self.progreso.setText("")
        self.progreso.setAlignment(QtCore.Qt.AlignCenter)
        self.progreso.setObjectName("progreso")
        self.frame = QtWidgets.QFrame(Maintenance_Dialog)
        self.frame.setGeometry(QtCore.QRect(60, 180, 291, 80))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.backout_button = QtWidgets.QRadioButton(self.frame)
        self.backout_button.setGeometry(QtCore.QRect(30, 10, 221, 20))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.backout_button.setFont(font)
        self.backout_button.setObjectName("backout_button")
        self.csv_button = QtWidgets.QRadioButton(self.frame)
        self.csv_button.setGeometry(QtCore.QRect(30, 50, 191, 20))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.csv_button.setFont(font)
        self.csv_button.setObjectName("csv_button")
        self.operacion = QtWidgets.QLabel(Maintenance_Dialog)
        self.operacion.setGeometry(QtCore.QRect(64, 40, 281, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.operacion.setFont(font)
        self.operacion.setAlignment(QtCore.Qt.AlignCenter)
        self.operacion.setObjectName("operacion")
        self.label = QtWidgets.QLabel(Maintenance_Dialog)
        self.label.setGeometry(QtCore.QRect(10, 10, 81, 31))
        self.label.setFocusPolicy(QtCore.Qt.NoFocus)
        self.label.setStyleSheet("")
        self.label.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.label.setFrameShadow(QtWidgets.QFrame.Plain)
        self.label.setMidLineWidth(0)
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap(":/NTT.png"))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        self.version = QtWidgets.QLabel(Maintenance_Dialog)
        self.version.setGeometry(QtCore.QRect(290, 420, 121, 21))
        self.version.setMinimumSize(QtCore.QSize(0, 0))
        self.version.setMaximumSize(QtCore.QSize(320, 420))
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setItalic(True)
        self.version.setFont(font)
        self.version.setStyleSheet("color: rgb(0, 0, 255);")
        self.version.setText("")
        self.version.setAlignment(QtCore.Qt.AlignCenter)
        self.version.setObjectName("version")
        self.plantillaLight = QtWidgets.QCheckBox(Maintenance_Dialog)
        self.plantillaLight.setGeometry(QtCore.QRect(130, 90, 131, 17))
        font = QtGui.QFont()
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.plantillaLight.setFont(font)
        self.plantillaLight.setStyleSheet("color: rgb(170, 0, 0);")
        self.plantillaLight.setObjectName("plantillaLight")
        self.oferta_cliente = QtWidgets.QCheckBox(Maintenance_Dialog)
        self.oferta_cliente.setGeometry(QtCore.QRect(110, 260, 191, 16))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.oferta_cliente.setFont(font)
        self.oferta_cliente.setStyleSheet("color: rgb(170, 0, 0);")
        self.oferta_cliente.setObjectName("oferta_cliente")

        self.retranslateUi(Maintenance_Dialog)
        QtCore.QMetaObject.connectSlotsByName(Maintenance_Dialog)

    def retranslateUi(self, Maintenance_Dialog):
        _translate = QtCore.QCoreApplication.translate
        Maintenance_Dialog.setWindowTitle(_translate("Maintenance_Dialog", "Ofertas de mantenimiento"))
        self.cancel_button.setText(_translate("Maintenance_Dialog", "Cancel"))
        self.fich_oferta.setPlaceholderText(_translate("Maintenance_Dialog", "Fichero de la oferta"))
        self.backout_button.setText(_translate("Maintenance_Dialog", "Carga de precios de backout"))
        self.csv_button.setText(_translate("Maintenance_Dialog", "Generación de fichero csv"))
        self.operacion.setText(_translate("Maintenance_Dialog", "<html><head/><body><p align=\"center\"><span style=\" font-size:12pt; font-weight:600;\">Búsqueda de backouts</span></p></body></html>"))
        self.plantillaLight.setText(_translate("Maintenance_Dialog", "Usar plantilla light"))
        self.oferta_cliente.setText(_translate("Maintenance_Dialog", "Generar oferta de cliente"))
import icons_rc
