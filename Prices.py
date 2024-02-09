from PyQt6.QtCharts import QChartView, QLineSeries, QChart, QDateTimeAxis, QValueAxis, QSplineSeries
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QColor


class Prices(QChartView):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.series = QSplineSeries()
        self.series.setColor(QColor("green"))
        self.series.setName("Dönerpreise")

        self.bier_series = QSplineSeries()
        self.bier_series.setColor(QColor("brown"))
        self.bier_series.setName("Bierpreis")

        self.chart = QChart()
        self.chart.setTitle("Döner- und Bierpreissteigerung")
        self.chart.addSeries(self.series)
        self.chart.addSeries(self.bier_series)

        axis_x = QValueAxis()
        axis_x.setRange(2015, 2024)

        axis_y = QValueAxis()
        axis_y.setRange(2, 20)

        self.chart.addAxis(axis_x, Qt.AlignmentFlag.AlignBottom)
        self.chart.addAxis(axis_y, Qt.AlignmentFlag.AlignLeft)

        self.series.attachAxis(axis_x)
        self.series.attachAxis(axis_y)

        self.bier_series.attachAxis(axis_x)
        self.bier_series.attachAxis(axis_y)

        self.series.append(2015, 4)
        self.series.append(2016, 4.5)
        self.series.append(2017, 5)
        self.series.append(2018, 5)
        self.series.append(2019, 5.5)
        self.series.append(2020, 5.5)
        self.series.append(2021, 6)
        self.series.append(2022, 6)
        self.series.append(2023, 7.5)
        self.series.append(2024, 8)

        self.bier_series.append(2015, 11)
        self.bier_series.append(2016, 12)
        self.bier_series.append(2017, 12.5)
        self.bier_series.append(2018, 12.5)
        self.bier_series.append(2019, 13)
        self.bier_series.append(2020, 13)
        self.bier_series.append(2021, 14)
        self.bier_series.append(2022, 16)
        self.bier_series.append(2023, 17)
        self.bier_series.append(2024, 18)

        self.setChart(self.chart)
