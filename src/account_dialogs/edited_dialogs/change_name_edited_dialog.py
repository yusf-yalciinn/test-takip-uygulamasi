from PyQt5.QtWidgets import QDialog, QAction, QDesktopWidget
from PyQt5.QtGui import QKeySequence
from PyQt5.QtCore import Qt, QPoint
from account_dialogs.change_name_dialog import Ui_Dialog
from databases.account_database.login_account_processes import find_logged_user
from databases.account_database.update_account_processes import UpdateAccountProcesses
from langs import texts
import json


class ChangeName(QDialog):
    def __init__(self):
        super(ChangeName, self).__init__()
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

        self.ui.line_name.setText(self.user.name)

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
            if not(self.user.name == self.ui.line_name.text().replace("i", "İ").replace("ı", "I").title()):
                try:
                    UpdateAccountProcesses.update_name(
                        self.ui.line_name.text().replace("i", "İ").replace("ı", "I").title().strip(),
                        self.user
                    )
                    self.close()

                except ValueError as err:
                    self.ui.lbl_warn.setText("* " + str(err))
                    self.edit_text()

            else:
                self.close()

    def edit_text(self):
        self.ui.line_name.setText(
            self.ui.line_name.text().replace("İ", "i").replace("I", "ı").title().strip()
        )

    def theme(self):
        if self.value["Theme"] == "0":
            with open("themes\\white_style.css", "r") as f:
                self.setStyleSheet(f.read())

        elif self.value["Theme"] == "1":
            with open("themes\\dark_style.css", "r") as f:
                self.setStyleSheet(f.read())
