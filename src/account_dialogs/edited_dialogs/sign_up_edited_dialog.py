from PyQt5.QtWidgets import QDialog, QAction
from PyQt5.QtGui import QKeySequence
from PyQt5.QtCore import Qt
from account_dialogs.sign_up_dialog import Ui_Dialog
from databases.account_database.user import User
from databases.account_database.register_account import sign_up
from message_dialogs.process_successful_dialog import CustomizeProcessMessageBox
from sqlite3 import Error


class SignUpDialog(QDialog):
    def __init__(self):
        super(SignUpDialog, self).__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)

        self.setWindowFlag(Qt.WindowCloseButtonHint, False)
        self.setWindowFlag(Qt.WindowContextHelpButtonHint, False)
        self.setFixedSize(400, 250)

        find_next_ret_act = QAction(self, triggered=self.ui.ok.animateClick)
        find_next_ret_act.setShortcut(QKeySequence("Return"))

        find_next_enter_act = QAction(self, triggered=self.ui.ok.animateClick)
        find_next_enter_act.setShortcut(QKeySequence("Enter"))

        # Now add (connect) these actions to the push button
        self.ui.ok.addActions([find_next_ret_act, find_next_enter_act])

        self.ui.cancel.clicked.connect(self.cancel)
        self.ui.ok.clicked.connect(self.ok)

    def cancel(self):
        self.close()

    def ok(self):
        try:
            user = User(
                self.ui.line_name.text().replace("i", "İ").replace("I", "ı").title(),
                self.ui.line_surname.text().replace("i", "İ").upper(),
                self.ui.line_password.text(),
                self.ui.line_username.text().replace("I", "ı").lower()
            )

            sign_up(user)
        except Error:
            self.ui.lbl_warn.setText("* Your username has been already\nusing.")
            self.clear_username()
            self.edit_text()

        except ValueError as err:
            self.ui.lbl_warn.setText("* " + str(err))
            self.edit_text()

        else:
            self.close()

            dia = CustomizeProcessMessageBox()
            dia.setModal(True)
            dia.exec_()

    def edit_text(self):
        self.ui.line_password.setText(
            self.ui.line_password.text().strip()
        )
        self.ui.line_surname.setText(
            self.ui.line_surname.text().replace("İ", "i").replace("I", "ı").upper().strip()
        )
        self.ui.line_username.setText(
            self.ui.line_username.text().replace("İ", "i").replace("I", "ı").lower().strip()
        )
        self.ui.line_name.setText(
            self.ui.line_name.text().replace("İ", "i").replace("I", "ı").title().strip()
        )

    def clear_username(self):
        self.ui.line_username.setText("")
