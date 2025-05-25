import os
import sqlite3

if not os.path.exists(f"{os.path.expanduser('~')}\\Documents\\FaRK"):
    os.mkdir(f"{os.path.expanduser('~')}\\Documents\\FaRK")

connection = sqlite3.connect(f"{os.path.expanduser('~')}\\Documents\\FaRK\\fark_db.db")
cursor = connection.cursor()
