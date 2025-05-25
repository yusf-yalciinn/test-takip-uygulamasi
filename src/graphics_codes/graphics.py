from databases.connection import connection, cursor
from databases.analysis_database.analysis import Analysis
from databases.account_database.user import User
from databases.analysis_database.get_lesson import get_lesson
from datetime import date
import pandas as pd
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg
from matplotlib.figure import Figure
import matplotlib.pyplot as plt
import json
import matplotlib
matplotlib.use('Qt5Agg')


with open("options.json", "r") as f:
    value = json.load(f)

if value["Theme"] == "1":
    plt.style.use("dark_background")


# Example: type_graph_func(
#               User("Yusuf", "YALÇIN", "12345678", "yousef09"),
#               "15.02.2021",
#               "24.02.2021",
#               2
#          )
def correct_graph_func(
        user: User,
        default_min_date= "01.01.2004",
        default_max_date= Analysis.transform_date(date.today(), "to_sql_date"),
        default_lesson_id= 0,
):
    user = user.id
    if default_lesson_id == 0:
        db = pd.read_sql_query(
            f"SELECT correctCount, wrongCount, gapCount, Date FROM analyses WHERE userId = {user}",
            connection
        )
        db_dates = db.groupby("Date")
        dates = []
        edited_dates = []
        ratios = []

        for i in db_dates.groups.keys():
            if Analysis.transform_date(default_min_date, "to_py_date") <= Analysis.transform_date(i, "to_py_date") <= Analysis.transform_date(default_max_date, "to_py_date"):
                dates.append(Analysis.transform_date(i, "to_py_date"))

        dates.sort()
        for date in dates:
            edited_dates.append(Analysis.transform_date(date, "to_sql_date"))

        for date in edited_dates:
            ratios.append(
                db_dates.sum().loc[date]["correctCount"] / (db_dates.sum().loc[date]["correctCount"] +
                                                            db_dates.sum().loc[date]["wrongCount"] +
                                                            db_dates.sum().loc[date]["gapCount"]) * 100
            )

        return [edited_dates, ratios]

    else:
        db = pd.read_sql_query(
            f"SELECT correctCount, wrongCount, gapCount, Date FROM analyses WHERE userId = {user} and lessonId = {default_lesson_id}",
            connection
        )
        db_dates = db.groupby("Date")
        dates = []
        edited_dates = []
        ratios = []

        for i in db_dates.groups.keys():
            if Analysis.transform_date(default_min_date, "to_py_date") <= Analysis.transform_date(i,
                                                                                                  "to_py_date") <= Analysis.transform_date(
                    default_max_date, "to_py_date"):
                dates.append(Analysis.transform_date(i, "to_py_date"))

        dates.sort()
        for date in dates:
            edited_dates.append(Analysis.transform_date(date, "to_sql_date"))

        for date in edited_dates:
            ratios.append(
                db_dates.sum().loc[date]["correctCount"] / (db_dates.sum().loc[date]["correctCount"] +
                                                            db_dates.sum().loc[date]["wrongCount"] +
                                                            db_dates.sum().loc[date]["gapCount"]) * 100
            )

        return [edited_dates, ratios]


def wrong_graph_func(
        user: User,
        default_min_date= "01.01.2004",
        default_max_date= Analysis.transform_date(date.today(), "to_sql_date"),
        default_lesson_id= 0,
):
    user = user.id
    if default_lesson_id == 0:
        db = pd.read_sql_query(
            f"SELECT correctCount, wrongCount, gapCount, Date FROM analyses WHERE userId = {user}",
            connection
        )
        db_dates = db.groupby("Date")
        dates = []
        edited_dates = []
        ratios = []

        for i in db_dates.groups.keys():
            if Analysis.transform_date(default_min_date, "to_py_date") <= Analysis.transform_date(i, "to_py_date") <= Analysis.transform_date(default_max_date, "to_py_date"):
                dates.append(Analysis.transform_date(i, "to_py_date"))

        dates.sort()
        for date in dates:
            edited_dates.append(Analysis.transform_date(date, "to_sql_date"))

        for date in edited_dates:
            ratios.append(
                db_dates.sum().loc[date]["wrongCount"] / (db_dates.sum().loc[date]["correctCount"] +
                                                            db_dates.sum().loc[date]["wrongCount"] +
                                                            db_dates.sum().loc[date]["gapCount"]) * 100
            )

        return [edited_dates, ratios]

    else:
        db = pd.read_sql_query(
            f"SELECT correctCount, wrongCount, gapCount, Date FROM analyses WHERE userId = {user} and lessonId = {default_lesson_id}",
            connection
        )
        db_dates = db.groupby("Date")
        dates = []
        edited_dates = []
        ratios = []

        for i in db_dates.groups.keys():
            if Analysis.transform_date(default_min_date, "to_py_date") <= Analysis.transform_date(i,
                                                                                                  "to_py_date") <= Analysis.transform_date(
                    default_max_date, "to_py_date"):
                dates.append(Analysis.transform_date(i, "to_py_date"))

        dates.sort()
        for date in dates:
            edited_dates.append(Analysis.transform_date(date, "to_sql_date"))

        for date in edited_dates:
            ratios.append(
                db_dates.sum().loc[date]["wrongCount"] / (db_dates.sum().loc[date]["correctCount"] +
                                                            db_dates.sum().loc[date]["wrongCount"] +
                                                            db_dates.sum().loc[date]["gapCount"]) * 100
            )

        return [edited_dates, ratios]


def gap_graph_func(
        user: User,
        default_min_date= "01.01.2004",
        default_max_date= Analysis.transform_date(date.today(), "to_sql_date"),
        default_lesson_id= 0,
):
    user = user.id
    if default_lesson_id == 0:
        db = pd.read_sql_query(
            f"SELECT correctCount, wrongCount, gapCount, Date FROM analyses WHERE userId = {user}",
            connection
        )
        db_dates = db.groupby("Date")
        dates = []
        edited_dates = []
        ratios = []

        for i in db_dates.groups.keys():
            if Analysis.transform_date(default_min_date, "to_py_date") <= Analysis.transform_date(i, "to_py_date") <= Analysis.transform_date(default_max_date, "to_py_date"):
                dates.append(Analysis.transform_date(i, "to_py_date"))

        dates.sort()
        for date in dates:
            edited_dates.append(Analysis.transform_date(date, "to_sql_date"))

        for date in edited_dates:
            ratios.append(
                db_dates.sum().loc[date]["gapCount"] / (db_dates.sum().loc[date]["correctCount"] +
                                                            db_dates.sum().loc[date]["wrongCount"] +
                                                            db_dates.sum().loc[date]["gapCount"]) * 100
            )

        return [edited_dates, ratios]

    else:
        db = pd.read_sql_query(
            f"SELECT correctCount, wrongCount, gapCount, Date FROM analyses WHERE userId = {user} and lessonId = {default_lesson_id}",
            connection
        )
        db_dates = db.groupby("Date")
        dates = []
        edited_dates = []
        ratios = []

        for i in db_dates.groups.keys():
            if Analysis.transform_date(default_min_date, "to_py_date") <= Analysis.transform_date(i,
                                                                                                  "to_py_date") <= Analysis.transform_date(
                    default_max_date, "to_py_date"):
                dates.append(Analysis.transform_date(i, "to_py_date"))

        dates.sort()
        for date in dates:
            edited_dates.append(Analysis.transform_date(date, "to_sql_date"))

        for date in edited_dates:
            ratios.append(
                db_dates.sum().loc[date]["gapCount"] / (db_dates.sum().loc[date]["correctCount"] +
                                                            db_dates.sum().loc[date]["wrongCount"] +
                                                            db_dates.sum().loc[date]["gapCount"]) * 100
            )

        return [edited_dates, ratios]


def question_graph_func(
        user: User,
        default_min_date= "01.01.2004",
        default_max_date= Analysis.transform_date(date.today(), "to_sql_date"),
        default_lesson_id= 0,
):
    user = user.id
    if default_lesson_id == 0:
        db = pd.read_sql_query(
            f"SELECT correctCount, wrongCount, gapCount, Date FROM analyses WHERE userId = {user}",
            connection
        )
        db_dates = db.groupby("Date")
        dates = []
        edited_dates = []
        ratios = []

        for i in db_dates.groups.keys():
            if Analysis.transform_date(default_min_date, "to_py_date") <= Analysis.transform_date(i, "to_py_date") <= Analysis.transform_date(default_max_date, "to_py_date"):
                dates.append(Analysis.transform_date(i, "to_py_date"))

        dates.sort()
        for date in dates:
            edited_dates.append(Analysis.transform_date(date, "to_sql_date"))

        for date in edited_dates:
            ratios.append(
                (db_dates.sum().loc[date]["correctCount"] +
                 db_dates.sum().loc[date]["wrongCount"] +
                 db_dates.sum().loc[date]["gapCount"])
            )

        return [edited_dates, ratios]

    else:
        db = pd.read_sql_query(
            f"SELECT correctCount, wrongCount, gapCount, Date FROM analyses WHERE userId = {user} and lessonId = {default_lesson_id}",
            connection
        )
        db_dates = db.groupby("Date")
        dates = []
        edited_dates = []
        ratios = []

        for i in db_dates.groups.keys():
            if Analysis.transform_date(default_min_date, "to_py_date") <= Analysis.transform_date(i,
                                                                                                  "to_py_date") <= Analysis.transform_date(
                    default_max_date, "to_py_date"):
                dates.append(Analysis.transform_date(i, "to_py_date"))

        dates.sort()
        for date in dates:
            edited_dates.append(Analysis.transform_date(date, "to_sql_date"))

        for date in edited_dates:
            ratios.append(
                (db_dates.sum().loc[date]["correctCount"] +
                 db_dates.sum().loc[date]["wrongCount"] +
                 db_dates.sum().loc[date]["gapCount"])
            )

        return [edited_dates, ratios]


def get_start_and_end_dates(user: User):
    sql = """SELECT Date FROM analyses WHERE userId = ?"""
    param = user.id,

    cursor.execute(sql, param)
    a_list = cursor.fetchall()
    edited_list = []

    for analysis in a_list:
        edited_list.append(Analysis.transform_date(analysis[0], "to_py_date"))

    return [
        Analysis.transform_date(min(edited_list), "to_q_date"),
        Analysis.transform_date(max(edited_list), "to_q_date")
    ]


def get_existing_lessons(user: User):
    sql = """SELECT lessonId FROM analyses WHERE userId = ?"""
    param = user.id,
    cursor.execute(sql, param)
    l_list = cursor.fetchall()

    i = 0
    for param in l_list:
        l_list[i] = param[0]
        i += 1

    l_list = sorted(set(l_list))
    edited_list = []

    for lesson in l_list:
        new_lesson = get_lesson(lesson)
        if len(new_lesson) > 1:
            new_lesson = f"{new_lesson[0]} {new_lesson[1]}"

        else:
            new_lesson = f"{new_lesson[0]}"

        edited_list.append(new_lesson)

    return edited_list


class Graph(FigureCanvasQTAgg):

    def __init__(self, parent=None, width=5, height=4, dpi=100):
        self.fig = Figure(figsize=(width, height), dpi=dpi)
        self.axes = self.fig.add_subplot(111)
        super(Graph, self).__init__(self.fig)
