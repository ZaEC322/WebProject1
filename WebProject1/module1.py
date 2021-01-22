from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QMainWindow, QApplication
import sys


def clicked():
    print("cleck")

def window():
    app = QApplication(sys.argv)
    win = QMainWindow()
    win.setGeometry(200,200,300,300)
    win.setWindowTitle("asd")

    label = QtWidgets.QLabel(win)
    label.setText("addsad")
    label.move(50,50)

    b1 = QtWidgets.QPushButton(win)
    b1.setText("click me")
    b1.clicked.connect(clicked)

    win.show()
    sys.exit(app.exec_())

window()



