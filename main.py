import sys
from qtpy import QtWidgets, QtCore

from ui.mainwindow import Ui_MainWindow

app = QtWidgets.QApplication(sys.argv)

class MainWindow(QtWidgets.QMainWindow):
    def __init__(self, parent = None):
        super().__init__(parent)

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # self.setWindowTitle("BMI-Rechner")

        self.ui.pushButton.clicked.connect(self.onPushButtonClick)

    def onPushButtonClick(self):
        self.ui.tableWidget.setItem(0, 0, QtWidgets.QTableWidgetItem("Budapest"))
        self.ui.tableWidget.setItem(0, 1, QtWidgets.QTableWidgetItem("9872345234"))
        print("Button wurde geklickt!")

window = MainWindow()

window.show()

sys.exit(app.exec_())
