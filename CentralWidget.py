import random

from PyQt6.QtCore import QTimer, pyqtSlot, pyqtSignal
from PyQt6.QtWidgets import QWidget, QSlider, QHBoxLayout, QGridLayout, QLabel

from ChartView import ChartView
from DateTime import DateTime
from Prices import Prices
from UebungFreddi import UebungFreddi
from ÜbungAlex import UebungAlex


class CentralWidget(QWidget):
    send_random = pyqtSignal(int)

    def __init__(self, parent=None):
        super().__init__(parent)

        self.alex = UebungAlex(parent)

        self.datetime = DateTime(parent)
        self.send_random.connect(self.datetime.add_random_value)

        self.slider = QSlider()
        self.slider.setRange(-5, 5)
        self.slider.valueChanged.connect(self.datetime.add_value)

        layout = QHBoxLayout()

        layout.addWidget(self.alex)
        #layout.addWidget(self.slider)

        self.setLayout(layout)


        self.timer = QTimer()
        self.timer.timeout.connect(self.generate_random)
        self.timer.start(1 * 1000)

    @pyqtSlot()
    def generate_random(self):
        random_value = random.randrange(-5, 6)

        self.send_random.emit(random_value)