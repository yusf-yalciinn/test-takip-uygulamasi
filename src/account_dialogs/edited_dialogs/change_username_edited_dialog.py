from PyQt5.QtWidgets import QDialog, QAction
from PyQt5.QtGui import QKeySequence
from PyQt5.QtCore import Qt
from account_dialogs.change_username_dialog import Ui_Dialog
from databases.account_database.login_account_processes import find_logged_user
from databases.account_database.update_account_processes import UpdateAccountProcesses


class ChangeUsername(QDialog):
    def __init__(self):
        super(ChangeUsername, self).__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.user = find_logged_user()

        self.setWindowFlag(Qt.WindowCloseButtonHint, False)
        self.setWindowFlag(Qt.WindowContextHelpButtonHint, False)
        self.setFixedSize(400, 250)

        find_next_ret_act = QAction(self, triggered=self.ui.ok.animateClick)
        find_next_ret_act.setShortcut(QKeySequence("Return"))

        find_next_enter_act = QAction(self, triggered=self.ui.ok.animateClick)
        find_next_enter_act.setShortcut(QKeySequence("Enter"))

        # Now add (connect) these actions to the push button
        self.ui.ok.addActions([find_next_ret_act, find_next_enter_act])

        self.ui.ok.clicked.connect(self.func)
        self.ui.cancel.clicked.connect(self.func)

    def func(self):
        sender = self.sender().text()

        if sender == "Cancel":
            self.close()

        elif sender == "OK":
            if self.ui.line_password.text() == self.user.password:
                try:
                    UpdateAccountProcesses.update_username(
                        self.ui.line_new_username.text().replace("İ", "i").replace("I", "ı").lower().strip(),
                        self.user
                    )
                    self.close()

                except ValueError as err:
                    self.ui.lbl_warn.setText("* " + str(err))
                    self.edit_text()

            else:
                self.ui.lbl_warn.setText("* Your password is wrong.")
                self.clear_password()
                self.edit_text()

    def edit_text(self):
        self.ui.line_new_username.setText(
            self.ui.line_new_username.text().replace("İ", "i").replace("I", "ı").lower().strip()
        )

    def clear_password(self):
        self.ui.line_password.setText("")
