from PyQt6.QtCharts import QChart, QChartView, QSplineSeries, QValueAxis, QDateTimeAxis, QLineSeries
from PyQt6.QtCore import Qt, QDateTime
from PyQt6.QtGui import QColor
from PyQt6.QtWidgets import QWidget

# Package: PyQt6-Charts
# https://github.com/chey00/qchart
class UebungFreddi(QChartView):
    def __init__(self, parent=None):
        super().__init__(parent)

        #creating a series
        self.series = QLineSeries()
        self.series.setColor(QColor("green"))

        self.series2 = QSplineSeries()
        self.series2.setColor(QColor("red"))

        self.series3 = QSplineSeries()
        self.series3.setColor(QColor("blue"))

        #creating the Chart
        self.chart = QChart()
        self.chart.setTitle("Dönner preis scalla")
        self.chart.addSeries(self.series)
        self.chart.addSeries(self.series2)
        self.chart.addSeries(self.series3)

        #Creating a DateTimeAxis
        self.axis_x= QDateTimeAxis()
        self.axis_x.setFormat("MMM.yyyy")

        start_date_time = QDateTime().currentDateTime()

        end_date_time = QDateTime().currentDateTime().addYears(10)

        self.axis_x.setRange(start_date_time, end_date_time)

        #creating a value Axis
        self.axis_y = QValueAxis()
        self.axis_y.setRange(3.50, 10.00)
        self.axis_y.setTitleText("in €")

        #setting the orientaten and attaching the axis
        self.chart.addAxis(self.axis_x, Qt.AlignmentFlag.AlignBottom)
        self.series.attachAxis(self.axis_x)
        self.series2.attachAxis(self.axis_x)
        self.series3.attachAxis(self.axis_x)

        self.chart.addAxis(self.axis_y, Qt.AlignmentFlag.AlignLeft)
        self.series.attachAxis(self.axis_y)
        self.series2.attachAxis(self.axis_y)
        self.series3.attachAxis(self.axis_y)

        #how to append series with date time
        self.series.setName("dönner preise")
        self.series.append(QDateTime(2024, 2, 1, 0, 0).toMSecsSinceEpoch(), 3.5)
        self.series.append(QDateTime(2025, 2, 3, 0, 0).toMSecsSinceEpoch(), 4.0)
        self.series.append(QDateTime(2026, 2, 5, 0, 0).toMSecsSinceEpoch(), 5.5)
        self.series.append(QDateTime(2027, 2, 3, 0, 0).toMSecsSinceEpoch(), 6.0)
        self.series.append(QDateTime(2028, 2, 1, 0, 0).toMSecsSinceEpoch(), 7.0)
        self.series.append(QDateTime(2029, 2, 2, 0, 0).toMSecsSinceEpoch(), 8.0)
        self.series.append(QDateTime(2030, 2, 5, 0, 0).toMSecsSinceEpoch(), 10.0)

        self.series2.setName("nicht lineare entwicklung")
        self.series2.append(QDateTime(2024, 2, 1, 0, 0).toMSecsSinceEpoch(), 3.5)
        self.series2.append(QDateTime(2025, 2, 9, 0, 0).toMSecsSinceEpoch(), 4.0)
        self.series2.append(QDateTime(2026, 2, 5, 0, 0).toMSecsSinceEpoch(), 5.5)
        self.series2.append(QDateTime(2027, 2, 6, 0, 0).toMSecsSinceEpoch(), 4.0)
        self.series2.append(QDateTime(2028, 2, 7, 0, 0).toMSecsSinceEpoch(), 6.0)
        self.series2.append(QDateTime(2029, 2, 3, 0, 0).toMSecsSinceEpoch(), 9.0)
        self.series2.append(QDateTime(2030, 2, 5, 0, 0).toMSecsSinceEpoch(), 3.5)

        self.setChart(self.chart)

    #set points with a mouseevent
    def mouseReleaseEvent(self, event) -> None:
        my_point = self.chart.mapToValue(event.pos().toPointF(), self.series3)

        self.series3.append(my_point)