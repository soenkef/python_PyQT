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

        self.readCsvFile("students.csv")

        self.ui.tableWidget.cellChanged.connect(self.onCellChanged)
        self.ui.addRow.clicked.connect(self.onAddButtonClick)
        self.ui.saveFile.clicked.connect(self.onSaveButtonClick)

    def readCsvFile(self, filename):
        with open(filename, "r", newline='', encoding="utf-8") as csvfile:
            reader = csv.reader(csvfile, delimiter=',', quotechar='"')

            for row in reader:
                count = self.ui.tableWidget.rowCount()
                self.ui.tableWidget.insertRow(count)

                name = row[1]
                prename = row[0]
                course = row[2]

                self.ui.tableWidget.setItem(count, 0, QtWidgets.QTableWidgetItem(name))
                self.ui.tableWidget.setItem(count, 1, QtWidgets.QTableWidgetItem(prename))
                self.ui.tableWidget.setItem(count, 2, QtWidgets.QTableWidgetItem(course))

    def onCellChanged(self, row, col):
        print(row)
        print(col)
        output = self.ui.tableWidget.item(row, col)

        print(output.text())

    def onAddButtonClick(self):
        print("onAddButtonClick() gedrückt")

        count = self.ui.tableWidget.rowCount()
        self.ui.tableWidget.insertRow(count)

        # Nach Klick auf Neuer Eintrag soll der Cursor gleich in die neue Zeile springen, damit losgetippt werden kann
        self.ui.tableWidget.setItem(count, 0, QtWidgets.QTableWidgetItem(""))
        self.ui.tableWidget.setItem(count, 1, QtWidgets.QTableWidgetItem(""))
        self.ui.tableWidget.setItem(count, 2, QtWidgets.QTableWidgetItem(""))

        cell = self.ui.tableWidget.item(count, 0)
        self.ui.tableWidget.editItem(cell)
        print(cell)

    def onSaveButtonClick(self):
        print("onSaveButtonClick() gedrückt")

        count = self.ui.tableWidget.rowCount()

        with open('students.csv', 'w', newline='', encoding="utf-8") as file:
            writer = csv.writer(file, delimiter=',',
                                quotechar='"', quoting=csv.QUOTE_MINIMAL)

            for i in range(0, count):
                # name = self.ui.tableWidget.item(i, 0)
                # prename = self.ui.tableWidget.item(i, 1)
                # course = self.ui.tableWidget.item(i, 2)
                # print(prename.text() + "," + name.text() + "," + course.text())
                # writer.writerow([prename.text(), name.text(), course.text()])

                rowContent = [
                    self.ui.tableWidget.item(i, 0).text(),
                    self.ui.tableWidget.item(i, 1).text(),
                    self.ui.tableWidget.item(i, 2).text()
                ]

                writer.writerow(rowContent)

window = MainWindow()

window.show()

sys.exit(app.exec_())
