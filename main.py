import random
import sys
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication
Form, Window = uic.loadUiType("randomizer.ui")


app = QApplication([])
window = Window()
form = Form()
form.setupUi(window)
window.show()

def number():
    a=form.lineEdit.text()
    b=form.lineEdit_2.text()

    a=int(a)
    b=int(b)
    c=random.randint(a,b)
    c=str(c)                
    form.label_out.setText(c)

form.pushButton.clicked.connect(number)




app.exec()
