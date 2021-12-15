from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QPushButton, QGridLayout, QLabel
import sys

EMPLOYEES = {
    'Kane':[],
    'Allan':[],
    'Fraser':[]
}
JOBS = {'0':[], }


class Window(QMainWindow):

    def __init__(self):
        super().__init__()
        self.UI()

    def UI(self):

        employee_name_labels = []

        for name in EMPLOYEES.keys():
            label = QLabel(self)
            label.setText(name)
            label.adjustSize()
            employee_name_labels.append(label)
            print('appended ' + name + '!')

        grid = QGridLayout()
        print('made grid')
        for i, label in enumerate(employee_name_labels):
            print(label, i)
            grid.addWidget(label, i, 0)

        self.setLayout(grid)
        self.setGeometry(300, 300, 500, 500)
        self.setWindowTitle('Timesheet application')
        self.show()

    def create_menu_bar(self):
        menu_bar = self.menuBar()
        file_menu = menu_bar.addMenu("&File")


def main():
    app = QApplication(sys.argv)
    window = Window()
    window.create_menu_bar()
    sys.exit(app.exec_())


main()
