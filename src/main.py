import sys
from PyQt5.QtWidgets import QApplication
from databases.manage_db import exists
from databases.account_database.login_account_processes import log_out
from controller import Controller


exists()
log_out()

app = QApplication(sys.argv)
win = Controller()
win.show_login_window()
sys.exit(app.exec_())
