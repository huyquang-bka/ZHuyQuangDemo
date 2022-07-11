from Widget_Layout.widget_search import Ui_Search
from PyQt5 import QtCore, QtWidgets

if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    self = QtWidgets.QWidget()
    ui = Ui_Search()
    ui.db = r"D:\Company\ZHuyQuang\Database\atin.db"
    ui.db_to_df()
    ui.show_table()
    ui.show()
    sys.exit(app.exec_())
