# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\cooki\OneDrive - Staffordshire University\projects\qtgui\ui\MainWindow.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(791, 467)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setSizeConstraint(QtWidgets.QLayout.SetMinimumSize)
        self.verticalLayout.setObjectName("verticalLayout")
        spacerItem = QtWidgets.QSpacerItem(20, 30, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        self.textEdit = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit.setMinimumSize(QtCore.QSize(0, 100))
        self.textEdit.setMaximumSize(QtCore.QSize(16777215, 225))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.textEdit.setFont(font)
        self.textEdit.setReadOnly(True)
        self.textEdit.setObjectName("textEdit")
        self.verticalLayout.addWidget(self.textEdit)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.menuBar = QtWidgets.QMenuBar(MainWindow)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 791, 21))
        self.menuBar.setObjectName("menuBar")
        self.menuLog_Level = QtWidgets.QMenu(self.menuBar)
        self.menuLog_Level.setObjectName("menuLog_Level")
        MainWindow.setMenuBar(self.menuBar)
        self.actionDISABLE = QtWidgets.QAction(MainWindow)
        self.actionDISABLE.setCheckable(True)
        self.actionDISABLE.setObjectName("actionDISABLE")
        self.actionWARNING = QtWidgets.QAction(MainWindow)
        self.actionWARNING.setCheckable(True)
        self.actionWARNING.setObjectName("actionWARNING")
        self.actionINFO = QtWidgets.QAction(MainWindow)
        self.actionINFO.setCheckable(True)
        self.actionINFO.setObjectName("actionINFO")
        self.actionDEBUG = QtWidgets.QAction(MainWindow)
        self.actionDEBUG.setCheckable(True)
        self.actionDEBUG.setObjectName("actionDEBUG")
        self.actionVERBOSE = QtWidgets.QAction(MainWindow)
        self.actionVERBOSE.setCheckable(True)
        self.actionVERBOSE.setObjectName("actionVERBOSE")
        self.menuLog_Level.addAction(self.actionDISABLE)
        self.menuLog_Level.addAction(self.actionWARNING)
        self.menuLog_Level.addAction(self.actionINFO)
        self.menuLog_Level.addAction(self.actionDEBUG)
        self.menuLog_Level.addAction(self.actionVERBOSE)
        self.menuBar.addAction(self.menuLog_Level.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.menuLog_Level.setTitle(_translate("MainWindow", "Log Level"))
        self.actionDISABLE.setText(_translate("MainWindow", "DISABLE"))
        self.actionWARNING.setText(_translate("MainWindow", "WARNING"))
        self.actionINFO.setText(_translate("MainWindow", "INFO"))
        self.actionDEBUG.setText(_translate("MainWindow", "DEBUG"))
        self.actionVERBOSE.setText(_translate("MainWindow", "VERBOSE"))
