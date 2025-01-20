from PySide6.QtWidgets import QWidget, QPushButton

class RockWidget(QWidget):
  def __init__(self):
    super().__init__()
    self.setWindowTitle("RockWidget")
    button1 = QPushButton("Button1")