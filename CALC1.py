import cmath
import sys
from PyQt5.QtWidgets import *
#Files stores under dist after using pyinstaller

def dialog():
    global mbox,A,B,C
    mbox = QMessageBox()
    A =float(a.text())
    B =float(b.text())
    C =float(c.text())

    D=(B**2)-(4*A*C)
    sol1=(-B-cmath.sqrt(D))/(2*A)
    sol2=(-B+cmath.sqrt(D))/(2*A)
    mbox.setWindowTitle("Answer")
    mbox.setText(f"Solutions: {sol1},{sol2}")
    mbox.exec_()
    

if __name__ =="__main__":
    app = QApplication(sys.argv)
    w = QWidget()
    w.resize(400,400)
    w.setWindowTitle("CALCULATOR")
    layout = QFormLayout()
    #QFormLayout-> input widget and their associate label on a single line
    #QLineEdit=allows us to edit line
    a = QLineEdit()
    b = QLineEdit()
    c = QLineEdit()
    layout.addRow("A:",a)
    layout.addRow("B:",b)
    layout.addRow("C:",c)

    btn = QPushButton(w)
    btn.setText("CALCULATE")
    btn.move(150,150)
    btn.show()
    btn.clicked.connect(dialog)

    w.setLayout(layout)
    w.show()
    sys.exit(app.exec_())