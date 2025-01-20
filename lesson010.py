from PySide6.QtWidgets import QApplication, QWidget
from rockwidget010 import RockWidget
import sys

app = QApplication(sys.argv)

window = RockWidget()
window.show()

app.exec()
