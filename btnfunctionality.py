from PySide6 import QtCore
from cbprocessor import ComboBoxProcesser
import logging


class BtnsFunctionality(ComboBoxProcesser):
    
    def __init__(self):
        super().__init__()
        
        ###############################################################
        # Кнопки запроса gps
        self.ui.btn_gps.clicked.connect(self._get_gps)
        # дейсвтия по получению ответа на запрос GPS
        self.msg_signals.get_gps.connect(self.actns_rcv_gps)
        self.msg_signals.set_gps_data_to_widget.connect(self._rcv_gps)
        

        ############################################################## 
        # Кнопки запроса IMU
        self.ui.btn_imu.clicked.connect(self._get_imu)
        # дейсвтия по получению ответа на запрос IMU
        self.msg_signals.get_imu.connect(self.actns_rcv_imu)
        self.msg_signals.set_imu_data_to_widget.connect(self._rcv_imu)
        
        
        self.ui.le_mnl_cmd.returnPressed.connect(self.send_mnl_cmd)

        # кнопки выбора режима управления
        self.ui.btn_auto_mode.clicked.connect(self._auto_mode)
        self.ui.btn_rmt_mode.clicked.connect(self._remote_mode)

        # кнопка запуска/остановки двигателя
        self.ui.btn_ctrl_mtr.clicked.connect(self._ctrl_motor)

        # кнопка отправки мануальной команды
        self.ui.btn_mnl_cmd.clicked.connect(self.send_mnl_cmd)

        # кнопка очистки окна вывода текста
        self.ui.btn_clean_textBrw.clicked.connect(self._clr_text_brw)
        

    def send_mnl_cmd(self):
        logging.info(f"function send_mnl_cmd was called")
        # Получение текста из QLineEdit
        if self.port.isOpen() != True:
            return
        
        msg = str(self.ui.le_mnl_cmd.text())
        
        if msg == "":
            return
        
        full_str = msg + '\r\n' 
        # Запись в порт
        self.port.write(QtCore.QByteArray(bytes(full_str, encoding='utf-8')))
        
        # Добавление записи в терминал
        self.current_text = f'[{self._cur_time()}] - [SEND] - {full_str}' + self.current_text
        self.ui.textBrowser.setText(self.current_text)
 
 
    def _auto_mode(self):
        """Автоматический режим управления аппаратом"""
        pass

    def _remote_mode(self):
        """Удаленый режим управления аппаратом (с пульта)"""
        pass

    def _ctrl_motor(self):
        """Запуск останов мотора"""
        pass


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
        cmd = 'D,s,4,GPS,*\r\n'.encode("utf-8")
        self.port.write(cmd)
        self.current_text = f'[{self._cur_time()}] - [SEND] - {cmd.decode("utf-8")}' + self.current_text
        self.ui.textBrowser.setText(self.current_text)
    
    
    @QtCore.Slot(object)
    def actns_rcv_gps(self, rcv_msg):
        _calculatedCS = self.estimator.get_CS(rcv_msg)
        _parsedCS =int(rcv_msg.split(',')[-1][1:-2])
    
        if _calculatedCS != _parsedCS:
            print("CRC error with GPS data")
            return -1
        
        if _calculatedCS == _parsedCS:
            print('GPS data received successfully')
            self.msg_signals.set_gps_data_to_widget.emit(rcv_msg)
            return 0    
    

    def _get_imu(self):
        """
        Функция запроса координат IMU
        """
        cmd = 'D,s,4,IMU,*\r\n'.encode("utf-8")
        self.port.write(cmd)
        self.current_text = f'[{self._cur_time()}] - [SEND] - {cmd.decode('utf-8')}' + self.current_text
        self.ui.textBrowser.setText(self.current_text)
           
    @QtCore.Slot(object)
    def actns_rcv_imu(self, rcv_msg):
        _calculatedCS = self.estimator.get_CS(rcv_msg)
        _parsedCS =int(rcv_msg.split(',')[-1][1:-2])

        if _calculatedCS != _parsedCS:
            print("CRC error with IMU data")
            return -1
        
        if _calculatedCS == _parsedCS:
            print('IMU data received successfully')
            self.msg_signals.set_imu_data_to_widget.emit(rcv_msg)
            return 0
    