from PySide6 import QtWidgets
from mainwindow_ui import Ui_MainWindow
from PySide6.QtCore import QObject, Signal
import sys
import serial

class Messager():

    @staticmethod
    def _dev_connected(dev):
        """ Вызов информацинного сообщения о успешном подключении к устройству """
        QtWidgets.QMessageBox.information(None, "Успешно", 
                                     f"Подключено устройство {dev.name}",
                                      QtWidgets.QMessageBox.StandardButton.Ok)
    @staticmethod
    def _dev_disconnect(dev):
        """ Вызов информацинного сообщения о успешном отключении от устройства """
        QtWidgets.QMessageBox.information(None, "Успешно", 
                                     f"Отключено устройство {dev.name}",
                                      QtWidgets.QMessageBox.StandardButton.Ok)
        
    @staticmethod
    def _indefinite_dev(dev):
        """ Вызов сообщения ошибки -> устройство по заданному com-порту не доступно """
        QtWidgets.QMessageBox.critical(None, "Ошибка", 
                                     f"Устроство {dev} не доступно",
                                      QtWidgets.QMessageBox.StandardButton.Ok)
        
    

class Base(QtWidgets.QMainWindow):
    def __init__(self):

        super(Base, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.btn_connect.clicked.connect(self.connect_to_ser_dev)
        self.ui.btn_disconnect.clicked.connect(self.disconnect_from_ser_dev)

        # Для удобства собраны все кнопки в один лист
        self.all_btns = [self.ui.btn_imu, 
                        self.ui.btn_gps,
                        self.ui.btn_mnl_mode,
                        self.ui.btn_auto_mode,
                        self.ui.btn_rmt_mode,
                        self.ui.btn_ctrl_mtr,]

        # Инициализация объекта последовательного порта
        self.ser = None
        for btn in self.all_btns:
                btn.setEnabled(False) # установка неактивного состояния кнопок
        self.ui.btn_disconnect.setEnabled(False) # доп.неакт кнопка "отключиться"

        self.ui.btn_gps.clicked.connect(self._get_imu)
        

    def connect_to_ser_dev(self):
        """
        Логика и действия при нажатии кнопки "Подключиться"
        """

        _com = "COM3"

        try:
            self.ser = serial.Serial(_com, 9600)
            self.ser.close()
            self.ser.open()
        
        # Ошибка возникающая при недоустпности / неопределённости устройства
        # по указанному com-порту
        except serial.serialutil.SerialException as e:
            Messager._indefinite_dev(_com)
            return
        
        # Вызов инф.сообщения
        Messager._dev_connected(self.ser)

        self.ui.btn_connect.setEnabled(False)
        self.ui.btn_disconnect.setEnabled(True)

        self._activate_btns() # Активация кнопок
        self.ser.write(b'aaaa')


    def disconnect_from_ser_dev(self):
        self.ser.close() # закрытие порта
        Messager._dev_disconnect(self.ser) # вызов инф.сообщения
        self._deactivate_btns() # установка не активного состояния кнопок

        self.ui.btn_connect.setEnabled(True)
        self.ui.btn_disconnect.setEnabled(False)

    
    def _get_imu(self):
        self.ser.write(b'D,s,4,GPS,*,\r,\n')

    
    def _activate_btns(self):
        """
        Функция активации кнопок управления
        """
        if self.ser.is_open:
            for btn in self.all_btns:
                btn.setEnabled(True)

    def _deactivate_btns(self):
        """
        Функция деактивации кнопок управления
        """
        if not self.ser.is_open:
            for btn in self.all_btns:
                btn.setEnabled(False)


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = Base()
    window.mouseMoveEvent = window.mouseMoveEvent
    window.show()
    sys.exit(app.exec())
