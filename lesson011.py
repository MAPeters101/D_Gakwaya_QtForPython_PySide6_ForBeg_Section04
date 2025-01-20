from PySide6.QtWidgets import QApplication
from mainwindow011 import MainWindow
import sys

app = QApplication(sys.argv)

window = MainWindow(app)
window.show()

app.exec()

