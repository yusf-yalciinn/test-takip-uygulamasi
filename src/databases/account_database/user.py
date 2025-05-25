# The Library and The File
from databases.connection import cursor


# Account Class
class User:
    def __init__(self, name: str, surname: str, password: str, username: str):
        self.name = name.strip().title()
        self.surname = surname.strip().upper()
        self.password = password.strip()
        self.username = username.strip()

        try:
            sql = """SELECT id FROM users WHERE username = ?"""
            param = self.username,
            cursor.execute(sql, param)
            self.id = cursor.fetchone()[0]

        except Exception:
            pass

        else:
            sql = """SELECT COUNT(id) FROM analyses WHERE userId = ?"""
            param = self.id,
            cursor.execute(sql, param)
            self.analyses_count = cursor.fetchone()[0]
