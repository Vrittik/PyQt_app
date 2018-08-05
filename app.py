from PyQt5 import QtWidgets
import sys

def window():
    app=QtWidgets.QApplication(sys.argv)
    w=QtWidgets.QWidget()
    w.setWindowTitle("Hello world")
    l1=QtWidgets.QLabel(w)
    l1.setText("Hello label")
    QtWidgets.QDateEdit(w)

    w.show()
    app.exec_()
window()

