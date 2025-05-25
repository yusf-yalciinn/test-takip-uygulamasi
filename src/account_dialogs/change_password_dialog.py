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

        self.line_old_password = QLineEdit(Dialog)
        self.line_old_password.setFont(self.font)
        self.line_old_password.setFrame(False)
        self.line_old_password.setGeometry(90, 58, 221, 31)
        self.line_old_password.setMaxLength(10)
        self.line_old_password.setEchoMode(QLineEdit.Password)
        self.line_old_password.setClearButtonEnabled(True)

        self.line_new_password = QLineEdit(Dialog)
        self.line_new_password.setFont(self.font)
        self.line_new_password.setFrame(False)
        self.line_new_password.setGeometry(90, 89, 221, 31)
        self.line_new_password.setMaxLength(10)
        self.line_new_password.setEchoMode(QLineEdit.Password)
        self.line_new_password.setClearButtonEnabled(True)

        self.line_new_password_2 = QLineEdit(Dialog)
        self.line_new_password_2.setFont(self.font)
        self.line_new_password_2.setFrame(False)
        self.line_new_password_2.setGeometry(90, 120, 221, 31)
        self.line_new_password_2.setMaxLength(10)
        self.line_new_password_2.setEchoMode(QLineEdit.Password)
        self.line_new_password_2.setClearButtonEnabled(True)

        self.lbl_warn = QLabel(Dialog)
        self.lbl_warn.setFont(self.font)
        self.lbl_warn.setGeometry(90, 151, 225, 41)
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

        self.line_old_password.setPlaceholderText(texts["text_old_password"])
        self.line_new_password.setPlaceholderText(texts["text_new_password"])
        self.line_new_password_2.setPlaceholderText(texts["text_new_password_2"])

        self.ok.setText(texts["ok"])
        self.cancel.setText(texts["cancel"])
