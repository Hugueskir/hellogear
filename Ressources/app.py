from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow
import sys
import random

from caller import caller

xpos, zpos, width, heigh = 200,  200, 300, 300


class myWindow(QMainWindow):

    def __init__(self):

        # Cette même class hérite toutes les fonctions de QMainWindow
        super(myWindow, self).__init__()

        self.setGeometry(xpos, zpos, width, heigh)
        self.setWindowTitle("Hello Gear")
        self.initUI()

    def initUI(self):

        self.label = QtWidgets.QLabel(self)
        self.label.setText('start')
        self.label.move(50, 50)

        self.b1 = QtWidgets.QPushButton(self)
        self.b1.setText('Click Button')
        self.b1.clicked.connect(self.clicked)

    def clicked(self):
        from PyQt5 import QtWidgets


xpos, zpos, width, heigh = 200,  200, 300, 300


class myWindow(QMainWindow):

    def __init__(self):

        # Cette même class hérite toutes les fonctions de QMainWindow
        super(myWindow, self).__init__()

        self.setGeometry(xpos, zpos, width, heigh)
        self.setWindowTitle("Hello Gear")
        self.initUI()

    def initUI(self):

        self.label = QtWidgets.QLabel(self)
        self.label.setText('start')
        self.label.move(50, 50)

        self.b1 = QtWidgets.QPushButton(self)
        self.b1.setText('Click Button')
        self.b1.clicked.connect(self.clicked)

    def clicked(self):
        caller()

    def update(self):
        self.label.adjustSize()


def window():
    app = QApplication(sys.argv)
    win = myWindow()

    win.show()
    sys.exit(app.exec_())


window()


def update(self):
    self.label.adjustSize()


def window():
    app = QApplication(sys.argv)
    win = myWindow()

    win.show()
    sys.exit(app.exec_())


window()
