# Files and Libraries
from databases.connection import cursor, connection
from databases.account_database.user import User


# Removing Process = f(user)
def remove(user: User):
    sql = """DELETE FROM analyses WHERE userId = ?"""
    param = user.id,
    cursor.execute(sql, param)
    connection.commit()

    sql = """DELETE FROM users WHERE id = ?"""
    param = user.id,
    cursor.execute(sql, param)
    connection.commit()
