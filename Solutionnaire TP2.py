import sys

from PyQt6 import QtWidgets
from PyQt6.QtSql import QSqlTableModel
import sqlite3
from test_rt_sql import Ui_MainWindow

class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.model = QSqlTableModel()
        self.model.setTable('user')
        self.model.select()
        self.ui.comboBox.setModel(self.model)
        self.ui.comboBox.addItems(self.comboBox_val)

        self.show()

    def comboBox_val(self):
        global data1
        conn = sqlite3.connect('C:/sqlite/test.db')
        c = conn.cursor()
        c.execute('SELECT name FROM user')
        data1 = []

        for row in c.fetchall():
            data1.append(str(row))

        return data1



if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec()
