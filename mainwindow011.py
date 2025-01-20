from PySide6.QtWidgets import QApplication, QMainWindow


class MainWindow(QMainWindow):
  def __init__(self, app):
    super().__init__()
    self.app = app #declare an app member
    self.setWindowTitle("Custom MainWindow")

    


