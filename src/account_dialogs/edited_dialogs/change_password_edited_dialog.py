from PyQt5.QtWidgets import QDialog, QAction, QDesktopWidget
from PyQt5.QtGui import QKeySequence
from PyQt5.QtCore import Qt, QPoint
from account_dialogs.change_password_dialog import Ui_Dialog
from databases.account_database.login_account_processes import find_logged_user
from databases.account_database.update_account_processes import UpdateAccountProcesses
import json
from langs import texts


class ChangePassword(QDialog):
    def __init__(self):
        super(ChangePassword, self).__init__()
        self.ui = Ui_Dialog(self)
        self.user = find_logged_user()

        with open("options.json", "r") as f:
            self.value = json.load(f)

        self.theme()

        self.setWindowFlag(Qt.FramelessWindowHint, True)
        self.setAcceptDrops(True)

        self.ui.cancel.clicked.connect(self.func)
        self.ui.ok.clicked.connect(self.func)

        find_next_ret_act = QAction(self, triggered=self.ui.ok.animateClick)
        find_next_ret_act.setShortcut(QKeySequence("Return"))

        find_next_enter_act = QAction(self, triggered=self.ui.ok.animateClick)
        find_next_enter_act.setShortcut(QKeySequence("Enter"))

        # Now add (connect) these actions to the push button
        self.ui.ok.addActions([find_next_ret_act, find_next_enter_act])

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
            if self.ui.line_old_password.text() == self.user.password:
                if self.ui.line_new_password.text() == self.ui.line_new_password_2.text():
                    try:
                        UpdateAccountProcesses.update_password(
                            self.ui.line_new_password.text().strip(),
                            self.user
                        )
                        self.close()

                    except ValueError as err:
                        self.ui.lbl_warn.setText("* " + str(err))
                        self.edit_text()

                else:
                    self.ui.lbl_warn.setText(texts["change_password_error_1"])
                    self.edit_text()

            else:
                self.ui.lbl_warn.setText(texts["change_password_error_2"])
                self.clear_password()
                self.edit_text()

    def edit_text(self):
        self.ui.line_new_password.setText(
            self.ui.line_new_password.text().strip()
        )
        self.ui.line_new_password_2.setText(
            self.ui.line_new_password_2.text().strip()
        )

    def clear_password(self):
        self.ui.line_old_password.setText("")

    def theme(self):
        if self.value["Theme"] == "0":
            with open("themes\\white_style.css", "r") as f:
                self.setStyleSheet(f.read())

        elif self.value["Theme"] == "1":
            with open("themes\\dark_style.css", "r") as f:
                self.setStyleSheet(f.read())
