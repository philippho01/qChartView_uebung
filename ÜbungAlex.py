from turtle import color

from PyQt6.QtCharts import QLineSeries, QChart, QChartView, QSplineSeries, QValueAxis, QAbstractAxis, QDateTimeAxis
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QPixmap, QBrush, QColor, QPen


# Package: PyQt6-Charts
# https://github.com/chey00/qchart
class UebungAlex(QChartView):
    def __init__(self, parent=None):
        super().__init__(parent)

        #Bild einfügen
        self.background_image = QPixmap("/Users/student/PycharmProjectc/qChartView_uebung/tree-png-image-free-download-picture-5a35c99ee77348.479688361513474462948.jpeg")
        self.background_image = self.background_image.scaled(1200, 600)

        #series erstellt
        self.series = QLineSeries()
        self.series.setName("Series")

        #Farbe für die Line ändern
        pen = QPen(QColor(144, 238, 144))
        pen.setWidth(5)
        self.series.setPen(pen)

        #andere methode für farbe hinzufügen
        #self.series.setColor(QColor("blue"))


        #chart erstellt und series hinzufgefügt
        self.chart = QChart()
        self.chart.setTitle("Karte")
        self.chart.addSeries(self.series)

        #achsen erstellt und range eingestellt
        axis_y = QValueAxis()
        axis_y.setRange(0, 10)
        axis_x = QValueAxis()
        axis_x.setRange(0, 10)

        #achsen dem chart hinzugefügt
        self.chart.addAxis(axis_x, Qt.AlignmentFlag.AlignBottom)
        self.chart.addAxis(axis_y, Qt.AlignmentFlag.AlignLeft)

        #nachdem achsen hinzufügen einfügen
        self.series.attachAxis(axis_x)
        self.series.attachAxis(axis_y)

        #werte für die series hinzufügen
        self.series.append(1,1)
        self.series.append(2, 2)
        self.series.append(3, 3)
        self.series.append(4,4)

        #das bild sichbar machen
        self.chart.setBackgroundVisible(True)
        self.chart.setBackgroundBrush(QBrush(self.background_image))

        #chart anzeigen
        self.setChart(self.chart)