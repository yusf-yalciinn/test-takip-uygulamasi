from PyQt5.QtWidgets import (
    QFrame,
    QLabel,
    QLineEdit,
    QPushButton
    )
from PyQt5.QtGui import QIcon, QPixmap, QFont, QCursor
from PyQt5.QtCore import Qt
from langs import texts, path


class Ui_Form(QFrame):
    def __init__(self, Form):
        super(Ui_Form, self).__init__()
        Form.setFixedSize(1000, 500)
        Form.setWindowTitle("FaRK")
        Form.setObjectName("Login")
        self.font = QFont()
        self.font.setFamily("Arial")
        self.font.setPointSize(10)

        self.minimize_font = QFont()
        self.minimize_font.setFamily("Arial")
        self.minimize_font.setPointSize(20)

        Form.setWindowIcon(QIcon("main_icon/icon.ico"))
        icon = QLabel(Form)
        icon.setPixmap(QPixmap(path))
        icon.setScaledContents(True)
        icon.setWordWrap(False)
        icon.setGeometry(406, 100, 211, 180)
        icon.setObjectName("icon")
        
        sign = QLabel(Form)
        sign.setGeometry(730, 470, 251, 21)
        sign.setFont(self.font)
        sign.setText(texts["sign"])
        sign.setAlignment(Qt.AlignRight)
        sign.setObjectName("sign")

        self.lbl_warn = QLabel(Form)
        self.lbl_warn.setGeometry(304, 442, 221, 21)
        self.lbl_warn.setFont(self.font)
        self.lbl_warn.setObjectName("Warn")

        # Lines
        self.line_username = QLineEdit(Form)
        self.line_username.setGeometry(304, 370, 221, 31)
        self.line_username.setFrame(False)
        self.line_username.setClearButtonEnabled(True)
        self.line_username.setMaxLength(10)
        self.line_username.setFont(self.font)
        self.line_username.setPlaceholderText(texts["line_username"])
        self.line_username.setFont(self.font)

        self.line_password = QLineEdit(Form)
        self.line_password.setGeometry(304, 400, 221, 31)
        self.line_password.setFrame(False)
        self.line_password.setClearButtonEnabled(True)
        self.line_password.setMaxLength(10)
        self.line_password.setFont(self.font)
        self.line_password.setPlaceholderText(texts["line_password"])
        self.line_password.setEchoMode(QLineEdit.Password)
        self.line_password.setFont(self.font)

        # Buttons
        self.btn_log_in = QPushButton(Form)
        self.btn_log_in.setText(texts["btn_log_in"])
        self.btn_log_in.setGeometry(534, 370, 75, 31)
        self.btn_log_in.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_log_in.setToolTip("ENTER")
        self.btn_log_in.setFont(self.font)

        self.btn_settings = QPushButton(Form)
        self.btn_settings.setText(texts["btn_settings"])
        self.btn_settings.setGeometry(614, 370, 75, 31)
        self.btn_settings.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_settings.setShortcut("ctrl+o")
        self.btn_settings.setToolTip("(CTRL + O)")
        self.btn_settings.setFont(self.font)

        self.btn_register = QPushButton(Form)
        self.btn_register.setText(texts["btn_register"])
        self.btn_register.setGeometry(534, 400, 75, 31)
        self.btn_register.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_register.setShortcut("ctrl+r")
        self.btn_register.setToolTip("(CTRL + R)")
        self.btn_register.setFont(self.font)

        self.btn_exit = QPushButton(Form)
        self.btn_exit.setText(texts["btn_exit"])
        self.btn_exit.setGeometry(614, 400, 75, 31)
        self.btn_exit.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_exit.setShortcut("esc")
        self.btn_exit.setToolTip("ESC")
        self.btn_exit.setFont(self.font)

        self.btn_minimize = QPushButton(Form)
        self.btn_minimize.setText("-")
        self.btn_minimize.setGeometry(965, 5, 30, 31)
        self.btn_minimize.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_minimize.clicked.connect(lambda: self.minimize_button(Form))
        self.btn_minimize.setFont(self.minimize_font)
        self.btn_minimize.setToolTip(texts["btn_minimize"])

    def minimize_button(self, Form):
        Form.setWindowState(Qt.WindowMinimized)
