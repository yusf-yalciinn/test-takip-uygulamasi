from PyQt5.QtWidgets import QDialog, QAction, QDesktopWidget
from PyQt5.QtGui import QKeySequence
from PyQt5.QtCore import Qt, QDate, QPoint
from databases.analysis_database.update_analysis_processes import update_analysis
from databases.analysis_database.removing_processings_analysis import remove_analysis
from databases.analysis_database.analysis import Analysis
from databases.account_database.login_account_processes import find_logged_user
from databases.analysis_database.get_lesson import get_lessons
from analysis_dialogs.edit_analysis_dialog import Ui_Dialog
from message_dialogs.removing_analysis_message_dialog import CustomizeRemovingMessageBox
import json
from langs import texts


class EditDialog(QDialog):
    def __init__(self, current_analysis: Analysis):
        super(EditDialog, self).__init__()
        self.ui = Ui_Dialog(self)
        self.user = find_logged_user()
        self.analysis = current_analysis

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
        self.ui.remove.clicked.connect(self.remove_analysis)

        self.ui.date.setMaximumDate(QDate.currentDate())

        self.stable_statue()

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
            def update():
                new_analysis = Analysis(
                    self.ui.spin_correct_count.value(),
                    self.ui.spin_wrong_count.value(),
                    self.ui.spin_gap_count.value(),
                    Analysis.transform_date(self.ui.date.date(), "to_sql_date"),
                    self.ui.lesson.currentIndex() + 1,
                    self.user
                )
                update_analysis(new_analysis, self.analysis)

                mess.close()
                self.close()

            def cancel():
                mess.close()

            if (
                    self.ui.spin_correct_count.value() == 0 and
                    self.ui.spin_wrong_count.value() == 0 and
                    self.ui.spin_gap_count.value() == 0
            ):
                self.ui.lbl_warn.setText(texts["adding_error"])

            elif (
                    not (self.analysis.correct_count == self.ui.spin_correct_count.value()) or
                    not (self.analysis.wrong_count == self.ui.spin_wrong_count.value()) or
                    not (self.analysis.gap_count == self.ui.spin_gap_count.value()) or
                    not (Analysis.transform_date(self.analysis.date, "to_q_date") == self.ui.date.date()) or
                    not (self.analysis.lesson_id == (self.ui.lesson.currentIndex() + 1))
            ):
                mess = CustomizeRemovingMessageBox()
                mess.setWindowTitle(texts["title_editing"])
                mess.ui.text.setText(texts["text_editing"])
                mess.ui.ok.clicked.connect(update)
                mess.ui.cancel.clicked.connect(cancel)
                mess.setModal(True)
                mess.exec_()

            else:
                self.close()

    def remove_analysis(self):
        try:
            def remove():
                remove_analysis(self.analysis)
                mess.close()
                self.close()

            def cancel():
                mess.close()

            mess = CustomizeRemovingMessageBox()
            mess.ui.text.setText(texts["text_analysis_removing"])
            mess.ui.ok.clicked.connect(remove)
            mess.ui.cancel.clicked.connect(cancel)
            mess.setModal(True)
            mess.exec_()
        except Exception as err:
            print(err)

    def stable_statue(self):
        self.ui.spin_correct_count.setValue(self.analysis.correct_count)
        self.ui.spin_wrong_count.setValue(self.analysis.wrong_count)
        self.ui.spin_gap_count.setValue(self.analysis.gap_count)
        self.ui.date.setDate(Analysis.transform_date(self.analysis.date, "to_q_date"))
        self.ui.lesson.addItems(get_lessons())
        self.ui.lesson.setCurrentIndex(self.analysis.lesson_id - 1)

    def theme(self):
        if self.value["Theme"] == "0":
            with open("themes\\white_style.css", "r") as f:
                self.setStyleSheet(f.read())

        elif self.value["Theme"] == "1":
            with open("themes\\dark_style.css", "r") as f:
                self.setStyleSheet(f.read())
