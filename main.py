import sys
from qtpy import QtWidgets, QtCore

from ui.mainwindow import Ui_MainWindow

app = QtWidgets.QApplication(sys.argv)

class MainWindow(QtWidgets.QMainWindow):
    def __init__(self, parent = None):
        super().__init__(parent)

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.setWindowTitle("Studierendenverwaltung")

        self.ui.label_3.hide()
        self.ui.result.hide()

        self.ui.calculate.clicked.connect(self.on_button_click)

    def on_button_click(self):
        # self.ui.calculate.hide()

        weight = self.ui.weight.value()
        height = self.ui.height.value()

        if height != 0 and weight != 0:
            result = round(weight / (height ** 2), 2)

            self.ui.label_3.show()
            self.ui.label_3.setText("Dein BMI ist: ")
            self.ui.result.show()
            self.ui.result.setText(str(result))

            print("on_button_click: " + str(result))
        else:
            self.ui.label_3.show()
            self.ui.label_3.setText("Bitte gib gültige Werte ein!")
            self.ui.weight.setValue(0)
            self.ui.height.setValue(0.00)
            self.ui.result.hide()
window = MainWindow()

window.show()

sys.exit(app.exec_())
