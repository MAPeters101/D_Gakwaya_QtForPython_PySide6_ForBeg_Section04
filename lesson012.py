from PySide6.QtWidgets import QApplication
from widget012 import Widget
import sys

app = QApplication(sys.argv)

widget = Widget()
widget.show()

app.exec()
