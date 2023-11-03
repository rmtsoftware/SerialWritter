from PySide6.QtCore import QTimer

import serial

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
            self.current_text = self.reader.glob_line + self.current_text + '\n'
            self.ui.textBrowser.setText(self.current_text)

    # При закрытии приложениии автоматически закрывается открытый ранее порт
    def closeEvent(self, event):

        try:
            self.ser.close()
        except AttributeError as _ :
            pass
        
        event.accept()
