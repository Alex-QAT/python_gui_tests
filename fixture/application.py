from pywinauto.application import Application as WinApp

from fixture.group import GroupHelper


class Application:

    def __init__(self, target_path):
        self.application = WinApp(backend="win32").start(target_path)
        self.main_window = self.application.window(title="Free Address Book")
        self.main_window.wait("visible")
        self.groups = GroupHelper(self)

    def destroy(self):
        self.main_window.close()

