from PyQt6.QtWidgets import QMainWindow
from CentralWidget import CentralWidget


class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.central_widget = CentralWidget(parent)

        self.setCentralWidget(self.central_widget)

        self.setWindowTitle("Chart Übung")