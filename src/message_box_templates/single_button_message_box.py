from PyQt5.QtWidgets import QFrame, QPushButton, QLabel
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont, QCursor, QIcon
from langs import texts


class Ui_Dialog(QFrame):
    def __init__(self, Dialog):
            super(Ui_Dialog, self).__init__()
            Dialog.setFixedSize(300, 150)
            Dialog.setObjectName("dialog")
            Dialog.setWindowIcon(QIcon("main_icon\\icon.ico"))
            self.font = QFont()
            self.font.setFamily("Arial")
            self.font.setPointSize(10)

            self.text = QLabel(Dialog)
            self.text.setGeometry(20, 30, 265, 51)
            self.text.setFont(self.font)
            self.text.setAlignment(Qt.AlignCenter)

            self.ok = QPushButton(Dialog)
            self.ok.setText(texts["ok"])
            self.ok.setGeometry(210, 100, 75, 31)
            self.ok.setCursor(QCursor(Qt.PointingHandCursor))
            self.ok.setFont(self.font)
