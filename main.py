from PySide6 import QtWidgets
from controlline import ControlDataInLineEdit
import sys

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = ControlDataInLineEdit()
    window.mouseMoveEvent = window.mouseMoveEvent
    window.show()
    sys.exit(app.exec())