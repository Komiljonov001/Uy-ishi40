from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
import sys
class parol(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setGeometry(750, 400, 500, 500)
        self.setFont(QFont("Sans serif", 14))
        self.setWindowTitle("Parol Tekshirish")
        self.lbl = QLabel("Parolni kiriting:",self)
        self.lbl.setGeometry(100,100,300,50)
        self.parol = QLineEdit(self)
        self.parol.setGeometry(100,150,300,50)
        self.btn = QPushButton("Tekshirish",self)
        self.btn.setGeometry(100,200,300,50)
        self.btn.clicked.connect(self.paroltekshirish)
        self.natija = QLabel("",self)
        self.natija.setGeometry(100,250,300,50)
        self.natija.setVisible(False)
    def paroltekshirish(self):
        if len(self.parol.text()) < 6:
            self.natija.setText("Natija: Juda zaif (6 tadan kam)")
            self.natija.setVisible(True)
        else:
            self.natija.setText("Natija: Kuchli (6 tadan ko'p)")
            self.natija.setVisible(True)
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = parol()
    window.show()
    sys.exit(app.exec_())