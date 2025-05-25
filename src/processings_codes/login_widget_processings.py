from PyQt5.QtWidgets import QFrame, QAction, QDesktopWidget
from PyQt5.QtGui import QKeySequence
from widget_guis.login_widget import Ui_Form as login_widget
from message_dialogs.quit_message_dialog import CustomizeQuitMessageBox
from account_dialogs.edited_dialogs.sign_up_edited_dialog import SignUpDialog
from databases.account_database.login_account_processes import log_in
from PyQt5.QtCore import pyqtSignal, Qt, QPoint
from langs import texts
import json


class LoginWidget(QFrame):
    switch_window = pyqtSignal()

    def __init__(self):
        super(LoginWidget, self).__init__()
        self.ui = login_widget(self)
        with open("options.json", "r") as f:
            self.value = json.load(f)

        self.theme()

        self.setWindowFlag(Qt.FramelessWindowHint, True)
        self.setAcceptDrops(True)

        find_next_ret_act = QAction(self, triggered=self.ui.btn_log_in.animateClick)
        find_next_ret_act.setShortcut(QKeySequence("Return"))

        find_next_enter_act = QAction(self, triggered=self.ui.btn_log_in.animateClick)
        find_next_enter_act.setShortcut(QKeySequence("Enter"))

        # Now add (connect) these actions to the push button
        self.ui.btn_log_in.addActions([find_next_ret_act, find_next_enter_act])

        # Button Actions
        self.ui.btn_exit.clicked.connect(self.func)
        self.ui.btn_register.clicked.connect(self.func)
        self.ui.btn_log_in.clicked.connect(self.func)

        # Move Event
        self.oldPos = self.pos()
        self.center()

    def center(self):
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

    def mousePressEvent(self, event):
        self.oldPos = event.globalPos()

    def mouseMoveEvent(self, event):
        delta = QPoint(event.globalPos() - self.oldPos)
        self.move(self.x() + delta.x(), self.y() + delta.y())
        self.oldPos = event.globalPos()

    def func(self):
        sender = self.sender().text()

        if sender == texts["btn_exit"]:
            mess = CustomizeQuitMessageBox()
            mess.setModal(True)
            mess.exec_()

        elif sender == texts["btn_register"]:
            dia = SignUpDialog()
            dia.setModal(True)
            dia.exec_()

        elif sender == texts["btn_log_in"]:
            try:
                log_in(
                    self.ui.line_username.text().replace("I", "ı").replace("İ", "i").lower(),
                    self.ui.line_password.text()
                )

            except Exception as err:
                self.ui.lbl_warn.setText("* " + str(err))
                self.clear_password()
                self.edit_text()

            else:
                self.switch_window.emit()

    def edit_text(self):
        self.ui.line_username.setText(
            self.ui.line_username.text().replace("İ", "i").replace("I", "ı").lower().strip()
        )

    def clear_password(self):
        self.ui.line_password.setText("")

    def theme(self):
        if self.value["Theme"] == "0":
            with open("themes\\white_style.css", "r") as f:
                self.setStyleSheet(f.read())

        elif self.value["Theme"] == "1":
            with open("themes\\dark_style.css", "r") as f:
                self.setStyleSheet(f.read())
