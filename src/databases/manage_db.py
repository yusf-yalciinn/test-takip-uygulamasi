# The Library and The File
import os
from databases.connection import connection, cursor


# Creating the Database
def exists():
    if os.stat(f"{os.path.expanduser('~')}\\Documents\\FaRK\\fark_db.db").st_size == 0:
        with open("set_db.sql", "r") as sql_script:
            sql_script = sql_script.read()

        try:
            cursor.executescript(sql_script)
            connection.commit()
        except Exception as err:
            print(err)
