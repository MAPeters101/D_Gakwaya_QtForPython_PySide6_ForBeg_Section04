from PySide6.QtWidgets import QWidget, QLabel, QHBoxLayout, QVBoxLayout, QSizePolicy

class Widget(QWidget):
  def __init__(self):
    super().__init__()

    self.setWindowTitle("Size policies and stretches")