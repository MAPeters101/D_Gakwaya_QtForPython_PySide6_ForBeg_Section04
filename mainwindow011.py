from PySide6.QtCore import QSize
from PySide6.QtGui import QAction
from PySide6.QtWidgets import QMainWindow, QToolBar


class MainWindow(QMainWindow):
  def __init__(self, app):
    super().__init__()
    self.app = app #declare an app member
    self.setWindowTitle("Custom MainWindow")

    # Menubar and menus
    menu_bar = self.menuBar()
    file_menu = menu_bar.addMenu("File")
    quit_action = file_menu.addAction("Quit")
    quit_action.triggered.connect(self.quit_app)

    edit_menu = menu_bar.addMenu("Edit")
    edit_menu.addAction("Copy")
    edit_menu.addAction("Cut")
    edit_menu.addAction("Paste")
    edit_menu.addAction("Undo")
    edit_menu.addAction("Redo")

    edit_menu = menu_bar.addMenu("Window")
    edit_menu = menu_bar.addMenu("Setting")
    edit_menu = menu_bar.addMenu("Help")

    # Working with toolbars
    toolbar = QToolBar("My main toolbar")
    toolbar.setIconSize(QSize(16, 16))
    self.addToolBar(toolbar)

    # Add the quit action to the toolbar
    toolbar.addAction(quit_action)

    action1 = QAction("Some Action", self)
    action1.setStatusTip("Status message for some action")
    action1.triggered.connect(self.toolbar_button_click)
    toolbar.addAction(action1)


  def quit_app(self):
    self.app.quit()

  def toolbar_button_click(self):
    print("action triggered")


