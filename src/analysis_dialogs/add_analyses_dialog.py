from PyQt5.QtWidgets import (
    QFrame,
    QLabel,
    QComboBox,
    QPushButton,
    QDateEdit,
    QSpinBox
    )
from PyQt5.QtGui import QIcon, QFont, QCursor
from PyQt5.QtCore import Qt, QDate
from langs import texts


class UiDialog(QFrame):
    def __init__(self, Dialog):
        super(UiDialog, self).__init__()
        Dialog.setFixedSize(400, 250)
        Dialog.setObjectName("dialog")
        Dialog.setWindowIcon(QIcon("main_icon\\icon.ico"))
        self.font = QFont()
        self.font.setFamily("Arial")
        self.font.setPointSize(10)
        self.cursor = QCursor(Qt.PointingHandCursor)

        self.cancel = QPushButton(Dialog)
        self.cancel.setGeometry(300, 200, 75, 31)
        self.cancel.setFont(self.font)
        self.cancel.setCursor(self.cursor)

        self.ok = QPushButton(Dialog)
        self.ok.setGeometry(128, 200, 75, 31)
        self.ok.setFont(self.font)
        self.ok.setCursor(self.cursor)

        self.next = QPushButton(Dialog)
        self.next.setGeometry(214, 200, 75, 31)
        self.next.setFont(self.font)
        self.next.setCursor(self.cursor)

        self.lbl_warn = QLabel(Dialog)
        self.lbl_warn.setObjectName("Warn")
        self.lbl_warn.setFont(self.font)
        self.lbl_warn.setGeometry(25, 131, 349, 41)

        self.lesson = QComboBox(Dialog)
        self.lesson.setGeometry(205, 109, 169, 21)
        self.lesson.setFont(self.font)
        self.lesson.setFrame(False)

        self.c_label = QLabel(Dialog)
        self.c_label.setGeometry(25, 43, 109, 21)
        self.c_label.setFont(self.font)
        self.c_label.setAlignment(Qt.AlignCenter)

        self.w_label = QLabel(Dialog)
        self.w_label.setGeometry(145, 40, 109, 21)
        self.w_label.setFont(self.font)
        self.w_label.setAlignment(Qt.AlignCenter)

        self.g_label = QLabel(Dialog)
        self.g_label.setGeometry(265, 40, 109, 21)
        self.g_label.setFont(self.font)
        self.g_label.setAlignment(Qt.AlignCenter)

        self.spin_correct_count = QSpinBox(Dialog)
        self.spin_correct_count.setGeometry(25, 70, 109, 29)
        self.spin_correct_count.setFont(self.font)
        self.spin_correct_count.setAccelerated(True)
        self.spin_correct_count.setProperty("showGroupSeparator",True)
        self.spin_correct_count.setMaximum(999)

        self.spin_wrong_count = QSpinBox(Dialog)
        self.spin_wrong_count.setGeometry(145, 70, 109, 29)
        self.spin_wrong_count.setFont(self.font)
        self.spin_wrong_count.setAccelerated(True)
        self.spin_wrong_count.setProperty("showGroupSeparator",True)
        self.spin_wrong_count.setMaximum(999)

        self.spin_gap_count = QSpinBox(Dialog)
        self.spin_gap_count.setGeometry(265, 70, 109, 29)
        self.spin_gap_count.setFont(self.font)
        self.spin_gap_count.setAccelerated(True)
        self.spin_gap_count.setProperty("showGroupSeparator",True)
        self.spin_gap_count.setMaximum(999)

        self.date = QDateEdit(Dialog)
        self.date.setGeometry(25, 109, 169, 22)
        self.date.setFont(self.font)
        self.date.setFrame(False)
        self.date.setAlignment(Qt.AlignCenter)
        self.date.setAccelerated(True)
        self.date.setMinimumDate(QDate(2004, 1, 1))
        self.date.setCalendarPopup(True)

        self.lbl_analysis_count = QLabel(Dialog)
        self.lbl_analysis_count.setGeometry(25, 200, 51, 31)
        self.lbl_analysis_count.setFont(self.font)
        self.lbl_analysis_count.setStyleSheet("margin: 5;")

        self.text_func(Dialog)

    def text_func(self, Dialog):
        Dialog.setWindowTitle(texts["title_adding"])
        
        self.c_label.setText(texts["lbl_correct"])
        self.w_label.setText(texts["lbl_wrong"])
        self.g_label.setText(texts["lbl_gap"])
        
        self.cancel.setText(texts["cancel"])
        self.next.setText(texts["next"])
        self.ok.setText(texts["ok"])
