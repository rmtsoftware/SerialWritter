from PySide6 import QtWidgets
from modectrl import ModeController
import sys

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = ModeController()
    window.mouseMoveEvent = window.mouseMoveEvent
    window.show()
    sys.exit(app.exec())
