from PySide6 import QtWidgets
from mainwindow_ui import Ui_MainWindow
from PySide6.QtCore import QObject, Signal, QTimer
import sys
import serial
import serial.tools.list_ports

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

        self.item_in_cb = [] #порты доступные в комбобоксе

        # Получение и обновление доступных COM-портов каждую 1 с
        self.timer = QTimer()
        self.timer.timeout.connect( self._add_item_to_cb)
        self.timer.start(1000)

    def _cb_proc(self, in_cbox, actual):
        common = [x for x in in_cbox if x in actual]
        to_delete = list(set(in_cbox).difference(set(common)))
        to_add = list(set(actual).difference(set(common)))
        return common, to_delete, to_add
    
    def _avail_dev(self):
        res = []
        ports = serial.tools.list_ports.comports()
        for port in ports:
            res.append(port.name)
        return res
    
    def _add_item_to_cb(self):
        avail_ports = self._avail_dev()
        common, to_del, to_add = self._cb_proc(self.item_in_cb, avail_ports)
        for el in to_del:
            index = self.ui.cb_com_dev.findText(el)
            self.ui.cb_com_dev.removeItem(index)
        self.ui.cb_com_dev.addItems(to_add)
        self.item_in_cb = common
        self.item_in_cb += to_add


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
