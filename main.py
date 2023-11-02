from PySide6 import QtWidgets
from mainwindow_ui import Ui_MainWindow
from PySide6.QtCore import QObject, Signal, QTimer, QRunnable, QThreadPool
import sys
import serial
import serial.tools.list_ports
import datetime

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
    
    @staticmethod
    def _not_selected_dev():
        """ Вызов сообщения ошибки -> устройство по заданному com-порту не доступно """
        QtWidgets.QMessageBox.warning(None, "Предупреждение", 
                                     f"Изделие не выбрано",
                                      QtWidgets.QMessageBox.StandardButton.Ok)

class ReaderSignals(QObject):
    get_data = Signal()

class Reader(QRunnable):
    def __init__(self, ser):
        super().__init__()
        self.ser = ser
        self.signals = ReaderSignals()
        self.glob_line = ''

    def run(self):
        while True:
            try:
                if self.ser.is_open:
                    line = self.ser.readline()
                    sline = str(line, 'UTF-8')
                    cut_time = datetime.datetime.now().strftime("%H:%M:%S.%f")[:-3]
                    self.glob_line = f'[{cut_time}] - [RECIEVED] - {sline}\n'
                    self.signals.get_data.emit()
            except:
                pass

            
class Base(QtWidgets.QMainWindow):
    def __init__(self):

        super(Base, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.pool = QThreadPool.globalInstance() # Создан пул потоков

        self.ui.btn_connect.clicked.connect(self.connect_to_ser_dev)
        self.ui.btn_disconnect.clicked.connect(self.disconnect_from_ser_dev)

        self.ui.btn_clean_textBrw.clicked.connect(self._clr_text_brw) # Кнопка очистки окна ввода текста
        
        # Для удобства собраны все кнопки в один лист
        self.all_btns = [self.ui.btn_imu, 
                        self.ui.btn_gps,
                        self.ui.btn_mnl_mode,
                        self.ui.btn_auto_mode,
                        self.ui.btn_rmt_mode,
                        self.ui.btn_ctrl_mtr,]

        # Инициализация объекта последовательного порта
        self.ser = None
        self.current_com = None
        for btn in self.all_btns:
                btn.setEnabled(False) # установка неактивного состояния кнопок
        self.ui.btn_disconnect.setEnabled(False) # доп.неакт кнопка "отключиться"

        self.ui.btn_gps.clicked.connect(self._get_gps) # запрос gps
        self.ui.btn_imu.clicked.connect(self._get_imu) # запрос imu

        self.item_in_cb = [] #порты доступные в комбобоксе

        # Получение и обновление доступных COM-портов каждую 1 с
        self.timer = QTimer()
        self.timer.timeout.connect( self._add_item_to_cb)
        self.timer.start(1000)

        # текст в textBrowser
        self.current_text = ''

    def _rcv_data(self):
        """
        Добавление записи в окно вывода текста
        """
        self.current_text += self.reader.glob_line
        self.ui.textBrowser.setText(self.current_text)


    def _clr_text_brw(self):
        """
        Функция очистки окна вывода текста  
        """
        self.current_text = ''
        self.ui.textBrowser.setText(self.current_text)

    def _cb_proc(self, in_cbox, actual):
        """

        COMBO BOX PROCCESING\n

        Функция формирует три списка:\n
            1. актуальный (требуемый) список портов\n
            2. порты которые следует удалить из комбобокса\n
            3. порты которые следует добавить в комбобокс\n

        """
        common = [x for x in in_cbox if x in actual]
        to_delete = list(set(in_cbox).difference(set(common)))
        to_add = list(set(actual).difference(set(common)))
        return common, to_delete, to_add
    
    def _avail_dev(self):
        """
        Функция смотрит доступные последовательные порты в ОС
        """
        res = []
        ports = serial.tools.list_ports.comports()
        for port in ports:
            res.append(port.name)
        return res
    
    def _add_item_to_cb(self):
        """
        Функция добавления и удаления портов в комбобокс выбора портов
        """
        avail_ports = self._avail_dev()
        common, to_del, to_add = self._cb_proc(self.item_in_cb, avail_ports)

        # Проверка есть ли выбранный com-порт
        # в списке доступных com-портов
        if self.current_com is not None:
            if not self.current_com in common:
                self.disconnect_from_ser_dev()

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

        # если в combobox "не выбрано"
        if self.ui.cb_com_dev.currentIndex() == -1:
            Messager._not_selected_dev()
            return

        # Определяем текущие выбраные item в комбобоксах
        self.current_com = self.ui.cb_com_dev.currentText()
        self.current_brate = int(self.ui.cb_baudrate.currentText())

        try:
            self.ser = serial.Serial(self.current_com, self.current_brate)
            self.ser.close()
            self.ser.open()

            self.reader = Reader(self.ser)

            self.pool.start(self.reader)
        
        # Ошибка возникающая при недоустпности / неопределённости устройства
        # по указанному com-порту
        except serial.serialutil.SerialException as e:
            Messager._indefinite_dev(self.current_com)
            return
        
        # Вызов инф.сообщения
        Messager._dev_connected(self.ser)

        self.ui.btn_connect.setEnabled(False)
        self.ui.btn_disconnect.setEnabled(True)

        self._activate_btns() # Активация кнопок

        # Сигнал получения даты
        self.reader.signals.get_data.connect(self._rcv_data)

    def disconnect_from_ser_dev(self):
        """
        Отключение от последовательного устройства
        """
        self.ser.close() # закрытие порта
        Messager._dev_disconnect(self.ser) # вызов инф.сообщения
        self._deactivate_btns() # установка не активного состояния кнопок

        self.ui.btn_connect.setEnabled(True)
        self.ui.btn_disconnect.setEnabled(False)

        self.current_com = None
    
    def _get_gps(self):
        """
        Функция запроса координат GPS
        """
        cut_time = datetime.datetime.now().strftime("%H:%M:%S.%f")[:-3]
        self.ser.write(b'D,s,4,GPS,*,\r\n')
        self.current_text += f'[{cut_time}] - [SEND] - D,s,4,GPS,*,\r\n'
        self.ui.textBrowser.setText(self.current_text)


    def _get_imu(self):
        """
        Функция запроса координат IMU
        """
        cut_time = datetime.datetime.now().strftime("%H:%M:%S.%f")[:-3]
        self.ser.write(b'D,s,4,GPS,*,\r\n')
        self.current_text += f'[{cut_time}] - [SEND] - D,s,4,IMU,*,\r\n'
        self.ui.textBrowser.setText(self.current_text)

    
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
