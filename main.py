from PySide6 import QtWidgets
import sys
import serial
import serial.tools.list_ports
import datetime
from PySide6.QtCore import QTimer

from reader import Reader
from messager import Messager
from base import Thread


class SerialConnector(Thread):
    def __init__(self):
        super().__init__()
        
        # Кнопки подключени/отключения в последовательному устройству
        self.ui.btn_connect.clicked.connect(self.connect_to_ser_dev)
        self.ui.btn_disconnect.clicked.connect(self.disconnect_from_ser_dev)

        # Получение и обновление доступных COM-портов каждую 1 с
        self.timer = QTimer()
        self.timer.timeout.connect(self._add_item_to_cb)
        self.timer.start(1000)


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
            # создаем объект серийного порта
            self.ser = serial.Serial(self.current_com, self.current_brate)

            # переоткрываем созданный порт
            self.ser.close() 
            self.ser.open()

            # создаем QRunnable объект и запускаем в отдельном потоке
            # возбежании блокировки основного потока программы
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
        self.reader.glob_stop = True

    
    def _rcv_data(self):
        """
        Добавление записи в окно вывода текста
        """
        if self.ser is not None:
            self.current_text += self.reader.glob_line
            self.ui.textBrowser.setText(self.current_text)


class ComboBoxProcesser(SerialConnector):
    def __init__(self):
        super().__init__()


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


class BtnsFunctionality(ComboBoxProcesser):
    def __init__(self):
        super().__init__()

        self.ui.btn_gps.clicked.connect(self._get_gps)
        self.ui.btn_imu.clicked.connect(self._get_imu)
        self.ui.btn_clean_textBrw.clicked.connect(self._clr_text_brw)

    
    def _cur_time(self):
        return datetime.datetime.now().strftime("%H:%M:%S.%f")[:-3]


    def _clr_text_brw(self):
        """
        Функция очистки окна вывода текста  
        """
        self.current_text = ''
        self.ui.textBrowser.setText(self.current_text)

    
    def _get_gps(self):
        """
        Функция запроса координат GPS
        """
        self.ser.write(b'D,s,4,GPS,*,\r\n')
        self.current_text += f'[{self._cur_time()}] - [SEND] - D,s,4,GPS,*,\r\n'
        self.ui.textBrowser.setText(self.current_text)


    def _get_imu(self):
        """
        Функция запроса координат IMU
        """
        self.ser.write(b'D,s,4,IMU,*,\r\n')
        self.current_text += f'[{self._cur_time()}] - [SEND] - D,s,4,IMU,*,\r\n'
        self.ui.textBrowser.setText(self.current_text)


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = BtnsFunctionality()
    window.mouseMoveEvent = window.mouseMoveEvent
    window.show()
    sys.exit(app.exec())
