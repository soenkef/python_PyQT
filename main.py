import sys
import csv
from qtpy import QtWidgets, QtCore

from ui.mainwindow import Ui_MainWindow

app = QtWidgets.QApplication(sys.argv)

class MainWindow(QtWidgets.QMainWindow):
    def __init__(self, parent = None):
        super().__init__(parent)

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.setWindowTitle("Studierendenverwaltung")

        with open('students.csv', newline='') as csvfile:
            reader = csv.reader(csvfile, delimiter=',', quotechar='|')
            for row in reader:
                count = self.ui.tableWidget.rowCount()
                self.ui.tableWidget.insertRow(count)
                name = row[1]
                prename = row[0]
                course = row[2]
                self.ui.tableWidget.setItem(count, 0, QtWidgets.QTableWidgetItem(name))
                self.ui.tableWidget.setItem(count, 1, QtWidgets.QTableWidgetItem(prename))
                self.ui.tableWidget.setItem(count, 2, QtWidgets.QTableWidgetItem(course))

                print(prename)

        self.ui.tableWidget.cellChanged.connect(self.onCellChanged)
        self.ui.addRow.clicked.connect(self.onAddButtonClick)
        self.ui.saveFile.clicked.connect(self.onSaveButtonClick)

    def onCellChanged(self, row, col):
        print(row)
        print(col)
        output = self.ui.tableWidget.item(row, col)

        print(output.text())

    def onAddButtonClick(self):
        count = self.ui.tableWidget.rowCount()
        self.ui.tableWidget.insertRow(count)

        print("onAddButtonClick() gedrückt")

    def onSaveButtonClick(self):
        print("onSaveButtonClick() gedrückt")

        count = self.ui.tableWidget.rowCount()
        
        with open('students.csv', 'w', newline='') as csvfile:
            writer = csv.writer(csvfile, delimiter=',',
                                quotechar='|', quoting=csv.QUOTE_MINIMAL)

            for i in range(0, count):
                name = self.ui.tableWidget.item(i, 0)
                prename = self.ui.tableWidget.item(i, 1)
                course = self.ui.tableWidget.item(i, 2)
                print(prename.text() + "," + name.text() + "," + course.text())

                writer.writerow([prename.text(), name.text(), course.text()])



window = MainWindow()

window.show()

sys.exit(app.exec_())
