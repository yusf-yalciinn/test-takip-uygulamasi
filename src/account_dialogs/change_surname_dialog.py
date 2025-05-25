from PyQt5.QtWidgets import (
    QFrame,
    QLineEdit,
    QPushButton,
    QLabel
)
from PyQt5.QtGui import QIcon, QFont, QCursor
from PyQt5.QtCore import Qt
from langs import texts


class Ui_Dialog(QFrame):
    def __init__(self, Dialog):
        super(Ui_Dialog, self).__init__()
        Dialog.setFixedSize(400, 250)
        Dialog.setObjectName("dialog")
        Dialog.setWindowIcon(QIcon("main_icon\\icon.ico"))
        self.font = QFont()
        self.font.setFamily("Arial")
        self.font.setPointSize(10)
        self.cursor = QCursor(Qt.PointingHandCursor)

        self.line_surname = QLineEdit(Dialog)
        self.line_surname.setFont(self.font)
        self.line_surname.setGeometry(90, 89, 221, 31)
        self.line_surname.setMaxLength(45)
        self.line_surname.setFrame(False)
        self.line_surname.setClearButtonEnabled(True)

        self.lbl_warn = QLabel(Dialog)
        self.lbl_warn.setFont(self.font)
        self.lbl_warn.setGeometry(90, 120, 225, 41)
        self.lbl_warn.setObjectName("Warn")

        self.ok = QPushButton(Dialog)
        self.ok.setFont(self.font)
        self.ok.setCursor(self.cursor)
        self.ok.setGeometry(214, 200, 75, 31)

        self.cancel = QPushButton(Dialog)
        self.cancel.setFont(self.font)
        self.cancel.setCursor(self.cursor)
        self.cancel.setGeometry(300, 200, 75, 31)

        self.text(Dialog)

    def text(self, Dialog):
        Dialog.setWindowTitle(texts["title_change"])

        self.line_surname.setPlaceholderText(texts["text_surname"])
        self.ok.setText(texts["ok"])
        self.cancel.setText(texts["cancel"])
