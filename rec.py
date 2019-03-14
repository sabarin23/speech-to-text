# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'rec.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Recorder(object):
    def setupUi(self, Recorder):
        Recorder.setObjectName("Recorder")
        Recorder.resize(579, 593)
        self.centralwidget = QtWidgets.QWidget(Recorder)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(20, 20, 531, 23))
        self.pushButton.setObjectName("pushButton")
        self.textEdit = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit.setGeometry(QtCore.QRect(20, 90, 531, 261))
        self.textEdit.setObjectName("textEdit")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(370, 390, 75, 23))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(470, 390, 75, 23))
        self.pushButton_3.setObjectName("pushButton_3")
        Recorder.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(Recorder)

        self.menubar.setGeometry(QtCore.QRect(0, 0, 579, 21))
        self.menubar.setObjectName("menubar")
        Recorder.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(Recorder)
        self.statusbar.setObjectName("statusbar")
        Recorder.setStatusBar(self.statusbar)

        self.retranslateUi(Recorder)
        QtCore.QMetaObject.connectSlotsByName(Recorder)

    def retranslateUi(self, Recorder):
        _translate = QtCore.QCoreApplication.translate
        Recorder.setWindowTitle(_translate("Recorder", "Speech-to-Text"))
        self.pushButton.setText(_translate("Recorder", "RECORD AUDIO"))
        self.pushButton_2.setText(_translate("Recorder", "COPY"))
        self.pushButton_3.setText(_translate("Recorder", "CLEAR"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Recorder = QtWidgets.QMainWindow()
    ui = Ui_Recorder()
    ui.setupUi(Recorder)
    Recorder.show()
    sys.exit(app.exec_())

