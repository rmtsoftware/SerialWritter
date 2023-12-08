from PySide6 import QtWidgets
from autorequests import AutoRequest
import sys

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = AutoRequest()
    window.mouseMoveEvent = window.mouseMoveEvent
    window.show()
    sys.exit(app.exec())
