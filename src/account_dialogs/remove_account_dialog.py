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

        self.text = QLabel(Dialog)
        self.text.setGeometry(95, 30, 211, 51)
        self.text.setFont(self.font)
        self.text.setAlignment(Qt.AlignCenter)

        self.line_password = QLineEdit(Dialog)
        self.line_password.setGeometry(90, 89, 221, 31)
        self.line_password.setFont(self.font)
        self.line_password.setMaxLength(10)
        self.line_password.setEchoMode(QLineEdit.Password)
        self.line_password.setFrame(False)
        self.line_password.setClearButtonEnabled(True)

        self.lbl_warn = QLabel(Dialog)
        self.lbl_warn.setObjectName("Warn")
        self.lbl_warn.setGeometry(90, 120, 225, 41)
        self.lbl_warn.setFont(self.font)

        self.cancel = QPushButton(Dialog)
        self.cancel.setGeometry(300, 200, 75, 31)
        self.cancel.setFont(self.font)
        self.cancel.setCursor(self.cursor)

        self.ok = QPushButton(Dialog)
        self.ok.setGeometry(214, 200, 75, 31)
        self.ok.setFont(self.font)
        self.ok.setCursor(self.cursor)

        self.text_func(Dialog)

    def text_func(self, Dialog):
        Dialog.setWindowTitle(texts["title_removing"])

        self.line_password.setPlaceholderText(texts["line_password"])
        self.cancel.setText(texts["cancel"])
        self.ok.setText(texts["ok"])
        self.text.setText(texts["text_removing_account_info"])
