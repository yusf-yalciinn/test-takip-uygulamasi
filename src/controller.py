from processings_codes.login_widget_processings import LoginWidget
from processings_codes.main_widget_processings import MainWidget


class Controller:
    def show_login_window(self):
        self.login_window = LoginWidget()
        self.login_window.switch_window.connect(self.show_main_window)
        self.login_window.show()

    def show_main_window(self):
        self.main_window = MainWidget()
        self.main_window.switch_window.connect(self.exit_account)
        self.login_window.close()
        self.main_window.showFullScreen()

    def exit_account(self):
        self.main_window.close()
        self.show_login_window()
