from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
import sys


class Calc(QMainWindow):
        def __init__(self):
                super().__init__()
                self.resize(450, 900)
                self.setStyleSheet("background-color:black")
                self.setWindowTitle("Calc")
                self.setWindowIcon(QIcon("calc.png"))
                self.setFont(QFont("Arial", 20))
                self.setStyleSheet("border: 3px solid grey; background-color: black; color: white; border-radius: 50px;")

                central = QWidget()
                self.setCentralWidget(central)

                main_layout = QVBoxLayout()
                central.setLayout(main_layout)
                main_layout.setContentsMargins(20, 30, 20, 20)

                top_buttons = QHBoxLayout()

                list_btn = QPushButton("☰")
                list_btn.setFixedSize(45, 45)
                list_btn.setStyleSheet("""
                        background-color: #333333;
                        color: white;
                        border-radius: 22px;
                        font-size: 18px;
                """)

                calc_btn = QPushButton(QIcon("calc.png"),"")
                calc_btn.setFixedSize(45, 45)
                calc_btn.setStyleSheet("""
                        background-color: #333333;
                        color: white;
                        border-radius: 22px;
                        font-size: 18px;

                """)

                top_buttons.addWidget(list_btn)
                top_buttons.addStretch()
                top_buttons.addWidget(calc_btn)
                main_layout.addLayout(top_buttons)



                lbl = QLabel("36,670 ÷ 50,000")
                lbl.setAlignment(Qt.AlignRight)
                lbl.setStyleSheet("font-size: 24px; color: grey;border:0px")
                lbl.setGeometry(0, 0, 200, 150)
                main_layout.addWidget(lbl)
                lbl2 = QLabel("0,7734")
                lbl2.setAlignment(Qt.AlignRight)
                lbl2.setStyleSheet("font-size: 70px; color: white;border:0px")
                lbl2.setGeometry(0, 0, 200, 150)
                main_layout.addWidget(lbl2)


                buttons = QGridLayout()
                gray = """
                        background-color: #a5a5a5;
                        color: black;
                        border-radius: 35px;
                        font-size: 22px;
                """
                dark = """
                        background-color: #333333;
                        color: white;
                        border-radius: 35px;
                        font-size: 22px;
                """
                orange = """
                        background-color: #ff9500;
                        color: white;
                        border-radius: 35px;
                        font-size: 26px;
                """
                buttons_info = [
                        ("⌫", 0, 0, gray), ("AC", 0, 1, gray), ("%", 0, 2, gray), ("÷", 0, 3, orange),
                        ("7", 1, 0, dark), ("8", 1, 1, dark), ("9", 1, 2, dark), ("×", 1, 3, orange),
                        ("4", 2, 0, dark), ("5", 2, 1, dark), ("6", 2, 2, dark), ("−", 2, 3, orange),
                        ("1", 3, 0, dark), ("2", 3, 1, dark), ("3", 3, 2, dark), ("+", 3, 3, orange),
                        ("+/-", 4, 0, dark), ("0", 4, 1, dark), (".", 4, 2, dark), ("=", 4, 3, orange),
                ]
                for txt,row,col,color in buttons_info:
                        btn = QPushButton(txt)
                        btn.setFixedSize(70,70)
                        btn.setStyleSheet(color)
                        buttons.addWidget(btn,row,col)
                main_layout.addLayout(buttons)
if __name__ == "__main__":
        app = QApplication([])
        oyna = Calc()
        oyna.show()
        sys.exit(app.exec_())
