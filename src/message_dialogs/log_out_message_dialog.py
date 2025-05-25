from PyQt5.QtWidgets import QDialog, QAction, QDesktopWidget
from PyQt5.QtGui import QKeySequence
from PyQt5.QtCore import Qt, QPoint
from message_box_templates.double_buttons_message_box import Ui_Dialog
from databases.account_database.login_account_processes import log_out
import json
from langs import texts


class CustomizeLogOutDialog(QDialog):
    def __init__(self):
        super(CustomizeLogOutDialog, self).__init__()
        self.ui = Ui_Dialog(self)

        with open("options.json", "r") as f:
            self.value = json.load(f)

        self.theme()

        self.setWindowFlag(Qt.FramelessWindowHint, True)
        self.setAcceptDrops(True)

        self.setWindowTitle(texts["title_log_out"])
        self.setFixedSize(300, 150)
        self.ui.text.setText(texts["text_log_out"])

        find_next_ret_act = QAction(self, triggered=self.ui.ok.animateClick)
        find_next_ret_act.setShortcut(QKeySequence("Return"))

        find_next_enter_act = QAction(self, triggered=self.ui.ok.animateClick)
        find_next_enter_act.setShortcut(QKeySequence("Enter"))

        # Now add (connect) these actions to the push button
        self.ui.ok.addActions([find_next_ret_act, find_next_enter_act])

        self.ui.ok.clicked.connect(self.ok)
        self.ui.cancel.clicked.connect(self.cancel)

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

    def ok(self):
        log_out()
        self.close()

    def cancel(self):
        self.close()

    def theme(self):
        if self.value["Theme"] == "0":
            with open("themes\\white_style.css", "r") as f:
                self.setStyleSheet(f.read())

        elif self.value["Theme"] == "1":
            with open("themes\\dark_style.css", "r") as f:
                self.setStyleSheet(f.read())
