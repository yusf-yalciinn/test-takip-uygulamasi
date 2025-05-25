from PyQt5.QtWidgets import QWidget, QTableWidgetItem, QProgressBar, QVBoxLayout, QHBoxLayout
from widget_guis.main_widget import Ui_Form as main_widget
from message_dialogs.quit_message_dialog import CustomizeQuitMessageBox
from message_dialogs.log_out_message_dialog import CustomizeLogOutDialog
from message_dialogs.process_successful_dialog import CustomizeProcessMessageBox
from message_dialogs.adding_message_dialog import CustomizeAddingMessageBox
from databases.account_database.login_account_processes import find_logged_user
from databases.analysis_database.get_analyses import get_analyses_elements
from databases.analysis_database.get_lesson import get_lesson_with_text, get_lessons
from PyQt5.QtCore import pyqtSignal
from account_dialogs.edited_dialogs.change_password_edited_dialog import ChangePassword
from account_dialogs.edited_dialogs.change_username_edited_dialog import ChangeUsername
from account_dialogs.edited_dialogs.change_name_edited_dialog import ChangeName
from account_dialogs.edited_dialogs.change_surname_edited_dialog import ChangeSurname
from account_dialogs.edited_dialogs.remove_account_edited_dialog import RemoveAccount
from analysis_dialogs.edited_dialogs.add_analyses_edited_dialog import AddAnalyses
from analysis_dialogs.edited_dialogs.edit_analysis_edited_dialog import EditDialog
from graphics_codes.graphics import *
import os
from matplotlib.ticker import MultipleLocator
import json
from langs import texts


class MainWidget(QWidget):
    switch_window = pyqtSignal()

    def __init__(self):
        super(MainWidget, self).__init__()
        self.ui = main_widget()
        self.ui.setupUi(self)
        self.user = find_logged_user()
        with open("options.json", "r") as f:
            self.value = json.load(f)

        self.theme()

        self.ui.lbl_list_name.setText(f"({self.user.name} {self.user.surname}) {texts['table']}")
        self.ui.table_analyses.setHorizontalHeaderLabels(texts["columns"])

        self.analyses_table()
        self.graphs_settings()

        self.ui.table_analyses.clicked.connect(self.table_clicked)
        self.ui.table_analyses.setFocusPolicy(0)

        self.ui.btn_edit.setEnabled(False)

        # Easter Egg
        self.ui.label.setToolTip(texts["easter_egg"])

        # Date Tooltips
        self.ui.end_date.setToolTip(texts["end_date_tooltip"])
        self.ui.starting_date.setToolTip(texts["start_date_tooltip"])

        # Button Texts
        self.ui.btn_add.setText(texts["btn_add"])
        self.ui.btn_edit.setText(texts["btn_edit"])
        self.ui.btn_graphic_correct.setText(texts["btn_graphic_correct"])
        self.ui.btn_graphic_wrong.setText(texts["btn_graphic_wrong"])
        self.ui.btn_graphic_gap.setText(texts["btn_graphic_gap"])
        self.ui.btn_graphic_question.setText(texts["btn_graphic_question"])
        self.ui.btn_account.setText(texts["btn_account"])
        self.ui.btn_back_graph.setText(texts["back"])
        self.ui.btn_back_account.setText(texts["back"])
        self.ui.btn_change_name.setText(texts["change_name"])
        self.ui.btn_change_surname.setText(texts["change_surname"])
        self.ui.btn_change_username.setText(texts["change_username"])
        self.ui.btn_change_password.setText(texts["change_password"])
        self.ui.btn_remove.setText(texts["remove"])

        # Button ToolTips
        self.ui.btn_graphic_correct.setToolTip(texts["btn_correct_tooltip"])
        self.ui.btn_graphic_wrong.setToolTip(texts["btn_wrong_tooltip"])
        self.ui.btn_graphic_gap.setToolTip(texts["btn_gap_tooltip"])
        self.ui.btn_exit.setToolTip(f'{texts["btn_exit"]} (ESC)')
        self.ui.btn_log_out.setToolTip(texts["btn_log_out"])
        self.ui.btn_settings.setToolTip(texts["btn_settings"])
        self.ui.save_button.setToolTip(texts["save_tooltip"])
        self.ui.confirm_button.setToolTip(texts["confirm_tooltip"])

        # Label Texts
        self.ui.label_2.setText(texts["lbl_name"])
        self.ui.label_3.setText(texts["lbl_surname"])
        self.ui.label_4.setText(texts["lbl_username"])
        self.ui.label_5.setText(texts["lbl_password"])
        self.ui.label_6.setText(texts["lbl_analysis"])

        # Button Actions
        self.ui.btn_exit.clicked.connect(self.exit)
        self.ui.btn_log_out.clicked.connect(self.log_out)
        self.ui.btn_account.clicked.connect(self.main_func)
        self.ui.btn_graphic_correct.clicked.connect(self.main_func)
        self.ui.btn_graphic_wrong.clicked.connect(self.main_func)
        self.ui.btn_graphic_gap.clicked.connect(self.main_func)
        self.ui.btn_graphic_question.clicked.connect(self.main_func)

        # Table Buttons Actions
        self.ui.btn_add.clicked.connect(self.table_func)
        self.ui.btn_edit.clicked.connect(self.table_func)

        # Account Buttons Actions
        self.ui.btn_change_password.clicked.connect(self.account_func)
        self.ui.btn_change_username.clicked.connect(self.account_func)
        self.ui.btn_change_name.clicked.connect(self.account_func)
        self.ui.btn_change_surname.clicked.connect(self.account_func)
        self.ui.btn_remove.clicked.connect(self.account_func)

        # Back Buttons Action
        self.ui.btn_back_account.clicked.connect(self.back)
        self.ui.btn_back_graph.clicked.connect(self.back)

        # The Graphic Button
        self.ui.save_button.clicked.connect(self.save_button)

    def exit(self):
        mess = CustomizeQuitMessageBox()
        mess.setModal(True)
        mess.exec_()

    def log_out(self):
        mess = CustomizeLogOutDialog()
        mess.setModal(True)
        mess.exec_()

        try:
            find_logged_user()

        except Exception:
            self.switch_window.emit()

    def main_func(self):
        sender = self.sender().text()

        if sender == texts["btn_account"]:
            self.disable_table_buttons()
            self.account_labels()
            self.ui.stacked_widget.setCurrentIndex(1)

        elif sender == texts["btn_graphic_correct"]:
            self.disable_table_buttons()
            self.ui.stacked_widget.setCurrentIndex(2)
            self.date_options()
            a_list = self.graph_values("correct")

            self.ui.confirm_button.clicked.connect(
                lambda: self.graph_processes("correct", self.graph_values("correct"))
            )

            self.graph_processes("correct", a_list)

        elif sender == texts["btn_graphic_wrong"]:
            self.disable_table_buttons()
            self.ui.stacked_widget.setCurrentIndex(2)
            self.date_options()
            a_list = self.graph_values("wrong")

            self.ui.confirm_button.clicked.connect(
                lambda: self.graph_processes("wrong", self.graph_values("wrong"))
            )

            self.graph_processes("wrong", a_list)

        elif sender == texts["btn_graphic_gap"]:
            self.disable_table_buttons()
            self.ui.stacked_widget.setCurrentIndex(2)
            self.date_options()
            a_list = self.graph_values("gap")

            self.ui.confirm_button.clicked.connect(
                lambda: self.graph_processes("gap", self.graph_values("gap"))
            )

            self.graph_processes("gap", a_list)

        elif sender == texts["btn_graphic_question"]:

            self.disable_table_buttons()
            self.ui.stacked_widget.setCurrentIndex(2)
            self.date_options()
            a_list = self.graph_values("question")

            self.ui.confirm_button.clicked.connect(
                lambda: self.graph_processes("question", self.graph_values("question"))
            )

            self.graph_processes("question", a_list)

    def account_func(self):
        sender = self.sender().text()

        if sender == texts["change_password"]:
            dia = ChangePassword()
            dia.setModal(True)
            dia.exec_()

            new_user = find_logged_user()
            if not(self.user.password == new_user.password):
                self.user = new_user
                self.account_labels()
                mess = CustomizeProcessMessageBox()
                mess.setModal(True)
                mess.exec_()

        elif sender == texts["change_username"]:
            dia = ChangeUsername()
            dia.setModal(True)
            dia.exec_()

            new_user = find_logged_user()
            if not (self.user.username == new_user.username):
                self.user = new_user
                self.account_labels()
                mess = CustomizeProcessMessageBox()
                mess.setModal(True)
                mess.exec_()

        elif sender == texts["change_name"]:
            dia = ChangeName()
            dia.setModal(True)
            dia.exec_()

            new_user = find_logged_user()
            if not (self.user.name == new_user.name):
                self.user = new_user
                self.account_labels()
                mess = CustomizeProcessMessageBox()
                mess.setModal(True)
                mess.exec_()

        elif sender == texts["change_surname"]:
            dia = ChangeSurname()
            dia.setModal(True)
            dia.exec_()

            new_user = find_logged_user()
            if not (self.user.surname == new_user.surname):
                self.user = new_user
                self.account_labels()
                mess = CustomizeProcessMessageBox()
                mess.setModal(True)
                mess.exec_()

        elif sender == texts["remove"]:
            dia = RemoveAccount()
            dia.setModal(True)
            dia.exec_()

            try:
                find_logged_user()

            except Exception:
                mess = CustomizeProcessMessageBox()
                mess.setModal(True)
                mess.exec_()
                self.switch_window.emit()

    def table_func(self):
        sender = self.sender().text()

        if sender == texts["btn_add"]:
            dia = AddAnalyses()
            dia.setModal(True)
            dia.exec_()

            new_user = find_logged_user()
            if not(self.user.analyses_count == new_user.analyses_count):
                difference = new_user.analyses_count - self.user.analyses_count
                self.user = new_user

                self.analyses_table()

                self.account_labels()

                mess = CustomizeProcessMessageBox()
                mess.ui.text.setText(f"{difference} {texts['text_successful_adding']}")
                mess.setModal(True)
                mess.exec_()

        elif sender == texts["btn_edit"]:
            lessons = get_lessons()

            i = 0
            for lesson in lessons:
                if lesson == self.ui.table_analyses.selectedItems()[4].text():
                    break
                i += 1

            current_row = Analysis(
                date=self.ui.table_analyses.selectedItems()[0].text(),
                true_count=int(self.ui.table_analyses.selectedItems()[1].text()),
                wrong_count=int(self.ui.table_analyses.selectedItems()[2].text()),
                gap_count=int(self.ui.table_analyses.selectedItems()[3].text()),
                lesson_id=i + 1,
                user=self.user
            )

            dia = EditDialog(current_row)
            dia.setModal(True)
            dia.exec_()

            self.user = find_logged_user()

            self.analyses_table()

            self.account_labels()

    def back(self):
        self.ui.table_analyses.setCurrentCell(-1, -1)
        self.enable_table_buttons()
        self.analyses_table()
        self.ui.stacked_widget.setCurrentIndex(0)

    def analyses_table(self):
        analyses = get_analyses_elements(self.user)
        edited_list = list()

        self.is_enable_graphic_buttons(analyses)

        try:
            for analysis in analyses:
                if len(get_lesson(analysis[5])) == 2:
                    edited_list.append(
                        {
                            "Date": analysis[4],
                            "Lesson": f"{get_lesson(analysis[5])[0]} ({get_lesson(analysis[5])[1]})",
                            "True-Count": analysis[1],
                            "Wrong-Count": analysis[2],
                            "Gap-Count": analysis[3],
                            "True-Ratio": QProgressBar(),
                            "Wrong-Ratio": QProgressBar(),
                            "Gap-Ratio": QProgressBar()
                        }
                    )

                else:
                    edited_list.append(
                        {
                            "Date": analysis[4],
                            "Lesson": f"{get_lesson(analysis[5])[0]}",
                            "True-Count": analysis[1],
                            "Wrong-Count": analysis[2],
                            "Gap-Count": analysis[3],
                            "True-Ratio": QProgressBar(),
                            "Wrong-Ratio": QProgressBar(),
                            "Gap-Ratio": QProgressBar()
                        }
                    )

        except Exception as err:
            print(err)

        self.ui.table_analyses.setRowCount(len(analyses))

        row_count = 0
        for analysis in edited_list:
            self.ui.table_analyses.setItem(row_count, 0, QTableWidgetItem(analysis["Date"]))
            self.ui.table_analyses.setItem(row_count, 1, QTableWidgetItem(str(analysis["True-Count"])))
            self.ui.table_analyses.setItem(row_count, 2, QTableWidgetItem(str(analysis["Wrong-Count"])))
            self.ui.table_analyses.setItem(row_count, 3, QTableWidgetItem(str(analysis["Gap-Count"])))
            self.ui.table_analyses.setItem(row_count, 4, QTableWidgetItem(analysis["Lesson"]))

            analysis["True-Ratio"].setValue(
                analysis["True-Count"] /
                (analysis["True-Count"] + analysis["Wrong-Count"] + analysis["Gap-Count"]) * 100
            )

            analysis["True-Ratio"].setStyleSheet(
                """QProgressBar{
                    border: 1 solid green;
                }
                QProgressBar::chunk{
                    border-radius:3;
                    background-color:green;
                }"""
            )

            analysis["Wrong-Ratio"].setValue(
                analysis["Wrong-Count"] /
                (analysis["True-Count"] + analysis["Wrong-Count"] + analysis["Gap-Count"]) * 100
            )

            analysis["Wrong-Ratio"].setStyleSheet(
                """QProgressBar{
                    border: 1 solid red;
                }
                QProgressBar::chunk{
                    border-radius:3;
                    background-color:red;
                }"""
            )

            analysis["Gap-Ratio"].setValue(
                analysis["Gap-Count"] /
                (analysis["True-Count"] + analysis["Wrong-Count"] + analysis["Gap-Count"]) * 100
            )

            analysis["Gap-Ratio"].setStyleSheet(
                """QProgressBar{
                    border: 1 solid yellow;
                }
                QProgressBar::chunk{
                    border-radius:3;
                    background-color:yellow;
                }"""
            )

            self.ui.table_analyses.setCellWidget(row_count, 5, analysis["True-Ratio"])
            self.ui.table_analyses.setCellWidget(row_count, 6, analysis["Wrong-Ratio"])
            self.ui.table_analyses.setCellWidget(row_count, 7, analysis["Gap-Ratio"])
            row_count += 1

    def account_labels(self):
        self.ui.lbl_name.setText(self.user.name)
        self.ui.lbl_surname.setText(self.user.surname)
        self.ui.lbl_username.setText(self.user.username)
        self.ui.lbl_password.setText(self.user.password[:3] + ("*" * len(self.user.password[3:])))
        self.ui.lbl_analysis_count.setText(str(self.user.analyses_count))

    def table_clicked(self):
        self.ui.btn_edit.setEnabled(True)

    def disable_table_buttons(self):
        self.ui.btn_edit.setEnabled(False)
        self.ui.btn_add.setEnabled(False)

    def enable_table_buttons(self):
        if self.ui.table_analyses.currentRow() > 0:
            self.ui.btn_edit.setEnabled(True)
        self.ui.btn_add.setEnabled(True)

    def is_enable_graphic_buttons(self, analysis_list: list):
        try:
            if not analysis_list:
                self.ui.btn_graphic_correct.setEnabled(False)
                self.ui.btn_graphic_wrong.setEnabled(False)
                self.ui.btn_graphic_gap.setEnabled(False)
                self.ui.btn_graphic_question.setEnabled(False)

            elif analysis_list:
                self.ui.btn_graphic_correct.setEnabled(True)
                self.ui.btn_graphic_wrong.setEnabled(True)
                self.ui.btn_graphic_gap.setEnabled(True)
                self.ui.btn_graphic_question.setEnabled(True)

        except Exception as err:
            print(err)

    def graphs_settings(self):
        graph_option_buttons_layout = QHBoxLayout()
        graph_option_buttons_layout.addWidget(self.ui.starting_date)
        graph_option_buttons_layout.addWidget(self.ui.end_date)
        graph_option_buttons_layout.addWidget(self.ui.lessons)
        graph_option_buttons_layout.addWidget(self.ui.confirm_button)
        graph_option_buttons_layout.addWidget(self.ui.save_button)

        self.graph_layout = QVBoxLayout(self.ui.page_3)
        self.graph_layout.addLayout(graph_option_buttons_layout)
        self.graph_layout.addWidget(self.ui.line_4)

        self.graph = Graph(self, width=5, height=4, dpi=75)
        if self.value["Theme"] == "1":
            self.graph.fig.set_facecolor("#292828")

        self.graph_layout.addWidget(self.graph)

        self.graph_layout.addWidget(self.ui.line_5)
        self.graph_layout.addWidget(self.ui.btn_back_graph)

        self.graph_layout.setStretch(2, 9)

    def graph_processes(self, graph_type: str, a_list: list):
        self.graph_layout.removeWidget(self.graph)
        self.graph.fig.clf()
        ax = self.graph.fig.add_subplot(111)
        ax.grid(True, linestyle="--")

        if self.value["Theme"] == "0":
            ax.plot(a_list[0], a_list[1], "-ok", ms=5)

        elif self.value["Theme"] == "1":
            ax.plot(a_list[0], a_list[1], "-ow", ms=5)
            ax.set_facecolor("#292828")

        ax.set_title(f"({self.user.name} {self.user.surname}) {texts[graph_type]} {texts['graph']}")
        if (
                graph_type == "correct" or
                graph_type == "wrong" or
                graph_type == "gap"
        ):
            ax.set_ylim(0, 100)
            ax.set_ylabel(f"{texts[graph_type]} {texts['graph_ratios']} (%)")

            ax.yaxis.set_major_locator(MultipleLocator(20))
            ax.yaxis.set_major_formatter('{x:.0f}')
            ax.yaxis.set_minor_locator(MultipleLocator(5))

        elif graph_type == "question":
            ax.set_ylabel(texts["graph_question"])

            ax.yaxis.set_major_locator(MultipleLocator(5))
            ax.yaxis.set_major_formatter('{x:.0f}')
            ax.yaxis.set_minor_locator(MultipleLocator(1))

        for tick in ax.get_xticklabels():
            tick.set_rotation(90)

        self.graph.draw()
        self.graph_layout.removeWidget(self.ui.btn_back_graph)
        self.graph_layout.removeWidget(self.ui.line_5)

        self.graph_layout.addWidget(self.graph)
        self.graph_layout.addWidget(self.ui.line_5)
        self.graph_layout.addWidget(self.ui.btn_back_graph)
        self.graph_layout.setStretch(2, 9)

    def graph_values(self, g_type: str):
        try:
            lesson_id = get_lesson_with_text(self.ui.lessons.currentText())
            if g_type == "correct":
                func = correct_graph_func

            elif g_type == "wrong":
                func = wrong_graph_func

            elif g_type == "gap":
                func = gap_graph_func

            elif g_type == "question":
                func = question_graph_func

            a_list = func(
                self.user,
                Analysis.transform_date(self.ui.starting_date.date(), "to_sql_date"),
                Analysis.transform_date(self.ui.end_date.date(), "to_sql_date"),
                lesson_id
            )

            return a_list
        except Exception as err:
            print(err)

    def date_options(self):
        self.ui.lessons.clear()
        self.ui.lessons.addItem(texts["all_lessons"])
        self.ui.lessons.addItems(get_existing_lessons(self.user))

        dates = get_start_and_end_dates(self.user)

        self.ui.starting_date.setDate(dates[0])
        self.ui.starting_date.setMinimumDate(dates[0])
        self.ui.starting_date.setMaximumDate(dates[1])

        self.ui.end_date.setDate(dates[1])
        self.ui.end_date.setMinimumDate(dates[0])
        self.ui.end_date.setMaximumDate(dates[1])

    def save_button(self):
        def ok():
            file_list = os.listdir("saved_graphics")
            for file in file_list:
                if file.startswith("fig"):
                    i = int(file[3:-4]) + 1
                    self.graph.figure.savefig(f"saved_graphics/fig{i}.pdf")
            else:
                self.graph.figure.savefig("saved_graphics/fig1.pdf")

            mess.close()

        mess = CustomizeAddingMessageBox()
        mess.ui.ok.clicked.connect(ok)
        mess.ui.text.setText(texts["text_save_graph"])
        mess.setWindowTitle(texts["title_save"])
        mess.ui.cancel.clicked.connect(lambda: mess.close())
        mess.setModal(True)
        mess.exec_()

    def theme(self):
        if self.value["Theme"] == "0":
            with open("themes\\white_style.css", "r") as f:
                self.setStyleSheet(f.read())

        elif self.value["Theme"] == "1":
            with open("themes\\dark_style.css", "r") as f:
                self.setStyleSheet(f.read())
