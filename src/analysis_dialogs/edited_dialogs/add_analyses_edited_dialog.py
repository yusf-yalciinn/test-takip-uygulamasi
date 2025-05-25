from PyQt5.QtWidgets import QDialog, QAction, QDesktopWidget
from PyQt5.QtGui import QKeySequence
from PyQt5.QtCore import Qt, QDate, QPoint
from databases.analysis_database.insert_analysis import insert_analyses
from databases.analysis_database.analysis import Analysis
from databases.account_database.login_account_processes import find_logged_user
from databases.analysis_database.get_lesson import get_lessons
from analysis_dialogs.add_analyses_dialog import UiDialog
from message_dialogs.adding_message_dialog import CustomizeAddingMessageBox
import json
from langs import texts


class AddAnalyses(QDialog):
    def __init__(self):
        super(AddAnalyses, self).__init__()
        self.ui = UiDialog(self)
        self.user = find_logged_user()
        self.analysis_list = []

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
        self.ui.next.clicked.connect(self.func)

        self.ui.lbl_analysis_count.setText("1" + ".")

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

        elif sender == texts["next"]:
            if (
                not (self.ui.spin_correct_count.value() == 0) or
                not (self.ui.spin_wrong_count.value() == 0) or
                not (self.ui.spin_gap_count.value() == 0)
            ):
                self.analysis_list.append(
                    Analysis(
                        self.ui.spin_correct_count.value(),
                        self.ui.spin_wrong_count.value(),
                        self.ui.spin_gap_count.value(),
                        Analysis.transform_date(self.ui.date.date(), "to_sql_date"),
                        self.ui.lesson.currentIndex() + 1,
                        self.user
                    )
                )
                self.stable_statue()

            else:
                self.ui.lbl_warn.setText(texts["adding_error"])

            if (len(self.analysis_list) + 1) == 10:
                self.ui.next.setEnabled(False)
                self.ui.lbl_analysis_count.setText(str(len(self.analysis_list) + 1) + ".")

            else:
                self.ui.lbl_analysis_count.setText(str(len(self.analysis_list) + 1) + ".")

        elif sender == texts["ok"]:
            def ok_clicked():
                insert_analyses(self.analysis_list)
                mess.close()

            def cancel_clicked():
                mess.close()

            try:
                if not(self.analysis_list == []):
                    if not (
                            self.ui.spin_correct_count.value() == 0 and
                            self.ui.spin_wrong_count.value() == 0 and
                            self.ui.spin_gap_count.value() == 0
                    ):
                        self.analysis_list.append(
                            Analysis(
                                self.ui.spin_correct_count.value(),
                                self.ui.spin_wrong_count.value(),
                                self.ui.spin_gap_count.value(),
                                Analysis.transform_date(self.ui.date.date(), "to_sql_date"),
                                self.ui.lesson.currentIndex() + 1,
                                self.user
                            )
                        )

                    mess = CustomizeAddingMessageBox()
                    mess.ui.ok.clicked.connect(ok_clicked)
                    mess.ui.cancel.clicked.connect(cancel_clicked)

                    mess.ui.text.setText(f"({len(self.analysis_list)}) {texts['text_adding']}")

                    self.close()
                    mess.setModal(True)
                    mess.exec_()
                else:
                    if not (
                            self.ui.spin_correct_count.value() == 0 and
                            self.ui.spin_wrong_count.value() == 0 and
                            self.ui.spin_gap_count.value() == 0
                    ):
                        self.analysis_list.append(
                            Analysis(
                                self.ui.spin_correct_count.value(),
                                self.ui.spin_wrong_count.value(),
                                self.ui.spin_gap_count.value(),
                                Analysis.transform_date(self.ui.date.date(), "to_sql_date"),
                                self.ui.lesson.currentIndex() + 1,
                                self.user
                            )
                        )

                        mess = CustomizeAddingMessageBox()
                        mess.ui.ok.clicked.connect(ok_clicked)
                        mess.ui.cancel.clicked.connect(cancel_clicked)

                        mess.ui.text.setText(f"({len(self.analysis_list)}) {texts['text_adding']}")

                        self.close()
                        mess.setModal(True)
                        mess.exec_()

                    else:
                        self.ui.lbl_warn.setText(texts["adding_error"])

            except Exception as err:
                print(err)

    def stable_statue(self):
        self.ui.lbl_warn.clear()
        self.ui.date.setMaximumDate(QDate.currentDate())
        self.ui.date.setDate(QDate.currentDate())
        self.ui.lesson.addItems(get_lessons())
        self.ui.spin_correct_count.setValue(0)
        self.ui.spin_wrong_count.setValue(0)
        self.ui.spin_gap_count.setValue(0)

    def theme(self):
        if self.value["Theme"] == "0":
            with open("themes\\white_style.css", "r") as f:
                self.setStyleSheet(f.read())

        elif self.value["Theme"] == "1":
            with open("themes\\dark_style.css", "r") as f:
                self.setStyleSheet(f.read())
