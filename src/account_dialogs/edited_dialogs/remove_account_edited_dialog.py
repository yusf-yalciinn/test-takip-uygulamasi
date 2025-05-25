from PyQt5.QtWidgets import QDialog, QAction, QDesktopWidget
from PyQt5.QtGui import QKeySequence
from PyQt5.QtCore import Qt, QPoint
from databases.account_database.remove_account import remove
from databases.account_database.login_account_processes import find_logged_user
from account_dialogs.remove_account_dialog import Ui_Dialog
import json
from langs import texts


class RemoveAccount(QDialog):
    def __init__(self):
        super(RemoveAccount, self).__init__()
        self.ui = Ui_Dialog(self)
        self.user = find_logged_user()

        with open("options.json", "r") as f:
            self.value = json.load(f)

        self.theme()

        self.setWindowFlag(Qt.FramelessWindowHint, True)
        self.setAcceptDrops(True)

        find_next_ret_act = QAction(self, triggered=self.ui.ok.animateClick)
        find_next_ret_act.setShortcut(QKeySequence("Return"))

        find_next_enter_act = QAction(self, triggered=self.ui.ok.animateClick)
        find_next_enter_act.setShortcut(QKeySequence("Enter"))

        # Now add (connect) these actions to the push button
        self.ui.ok.addActions([find_next_ret_act, find_next_enter_act])

        self.ui.ok.clicked.connect(self.func)
        self.ui.cancel.clicked.connect(self.func)

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

        if sender == texts["cancel"]:
            self.close()

        elif sender == texts["ok"]:
            if self.ui.line_password.text().strip() == self.user.password:
                remove(self.user)
                self.close()

            else:
                self.ui.lbl_warn.setText(texts["text_removing_account"])
                self.clear_password()

    def clear_password(self):
        self.ui.line_password.setText("")

    def theme(self):
        if self.value["Theme"] == "0":
            with open("themes\\white_style.css", "r") as f:
                self.setStyleSheet(f.read())

        elif self.value["Theme"] == "1":
            with open("themes\\dark_style.css", "r") as f:
                self.setStyleSheet(f.read())
