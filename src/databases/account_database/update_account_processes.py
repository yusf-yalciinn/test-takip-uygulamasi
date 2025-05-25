# Files and Libraries
from databases.connection import cursor, connection
from databases.account_database.user import User
from langs import texts


# Updating Processes = f("thing to change", "user")
class UpdateAccountProcesses:

    def __init__(self):
        pass
    
    # Updating Password of a User
    @staticmethod
    def update_password(password: str, user: User):
        if len(password) < 8:
            raise ValueError(texts["update_password_error"])

        sql = """UPDATE users SET password = ? WHERE id = ?"""
        params = password, user.id
        cursor.execute(sql, params)
        connection.commit()

    # Updating Username of a User
    @staticmethod
    def update_username(username: str, user: User):
        if len(username) < 5:
            raise ValueError("Your new username can't be less\nthan 5 characters.")

        sql = """UPDATE users SET username = ? WHERE id = ?"""
        params = username, user.id
        cursor.execute(sql, params)
        connection.commit()

    # Updating Name of a User
    @staticmethod
    def update_name(name: str, user: User):
        if name == "":
            raise ValueError(texts["update_name_error"])

        sql = """UPDATE users SET name = ? WHERE id = ?"""
        params = name, user.id
        cursor.execute(sql, params)
        connection.commit()

    # Updating Surname of a User
    @staticmethod
    def update_surname(surname: str, user: User):
        if surname == "":
            raise ValueError(texts["update_surname_error"])

        sql = """UPDATE users SET surname = ? WHERE id = ?"""
        params = surname, user.id
        cursor.execute(sql, params)
        connection.commit()
