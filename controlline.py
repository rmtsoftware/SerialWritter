from PySide6 import QtWidgets
from PySide6 import QtCore
import sys
from btnfunctionality import BtnsFunctionality

from messager import Messager

class ControlDataInLineEdit(BtnsFunctionality):
    def __init__(self):
        super().__init__()
        self.ui.le_pwr_mnl.editingFinished.connect(self._action_le_edited)
        self.ui.le_pwr_mnl.setText('0')
        self.pwr_mnl = int(self.ui.le_pwr_mnl.text())


    def _action_le_edited(self):
        """ Действия по окончанию изменения значения в lineEdit 'Задание мощности' """
        
        # Получение текста из области
        _text = self.ui.le_pwr_mnl.text()

        # Проверка, что текст не пустой
        if _text == '':
            self.ui.le_pwr_mnl.setText('0')
            self.pwr_mnl = int(self.ui.le_pwr_mnl.text())
            return

        # Преобразование str в int
        try:
            _val = int(_text)
        except ValueError as _:
            Messager._invalid_input()
            self.ui.le_pwr_mnl.setText('0')

        # Проверка принадлежности к диапазону [0, 100] введённого значения
        if _val > 100:
            Messager._invalid_input()
            self.ui.le_pwr_mnl.setText('100')

        if _val < 0:
            Messager._invalid_input()
            self.ui.le_pwr_mnl.setText('0')

        # Присвоение значения к глобальной переменной
        # которая формирует команду на mainBoard 
        self.pwr_mnl = int(self.ui.le_pwr_mnl.text())
        
        
if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = ControlDataInLineEdit()
    window.mouseMoveEvent = window.mouseMoveEvent
    window.show()
    sys.exit(app.exec())
