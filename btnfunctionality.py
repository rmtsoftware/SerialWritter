
from PySide6 import QtCore
import sys
from cbprocessor import ComboBoxProcesser
import ctypes
from messager import Messager
from PySide6.QtGui import QPixmap
from random import randint
import logging


class BtnsFunctionality(ComboBoxProcesser):
    
    def __init__(self):
        super().__init__()
        
        #############################################################
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
        
        
        ##############################################################
        # Ручное управление кнопками WASD 
        self._manCS = 0
        self._w_flag = False
        self._a_flag = False
        self._s_flag = False
        self._d_flag = False
        self.msg_signals.get_man_perm.connect(self.actns_rcv_man_perm)
        self.msg_signals.mov_forw.connect(self.actns_press_w)
        self.msg_signals.mov_back.connect(self.actns_press_s)
        self.msg_signals.mov_left.connect(self.actns_press_a)
        self.msg_signals.mov_right.connect(self.actns_press_d)


        # кнопки выбора режима управления
        self.ui.btn_mnl_mode.clicked.connect(self._manual_mode)
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
        msg = str(self.ui.le_mnl_cmd.text())

        full_str = msg + '\r\n' 
        # Запись в порт
        self.port.write(QtCore.QByteArray(bytes(full_str, encoding='utf-8')))
        
        # Добавление записи в терминал
        self.current_text = f'[{self._cur_time()}] - [SEND] - {full_str}' + self.current_text
        self.ui.textBrowser.setText(self.current_text)


    def _manual_mode(self):
        
        """Ручной режим управления аппаратом"""

        if self.man_mode_flag == True:
            return
        
        cmd = f'D,s,3,F,{self.pwr_mnl},*'
        cmd += ',\r\n'
        self.ser.write(bytes(cmd, encoding='utf-8'))
        self.current_text = f'[{self._cur_time()}] - [SEND] - {cmd}\n' + self.current_text
        self.ui.textBrowser.setText(self.current_text)

        # Установка флага ручная команда
        self.man_mode_flag = True

        # high-level software checksum
        # Контрольная сумма, рассчитанное GUI. Сравнивается с контрольной суммой, полученной от нижнего уровня.
        self.calculated_cs_man_mode = ord(self.test.calculateChecksum(cmd.encode('utf-8'))) + randint(0,1)
        QtCore.QTimer.singleShot(1000, self._manTimerActions)

    def _manTimerActions(self):
        
        def flags_reset():
            self.reader.glob_cs_man_mode = None
            self.calculated_cs_man_mode = None
            self.man_mode_flag = False
        
        print(self.reader.glob_cs_man_mode, self.calculated_cs_man_mode)
        
        try:
            if int(self.reader.glob_cs_man_mode) == int(self.calculated_cs_man_mode):
                flags_reset()
                self.counter_man_mode = 0
                self.crc_ok = True
            else:
                flags_reset()
                self.counter_man_mode += 1
                       
        except TypeError as e:
            print("Не полученно ответное сообщение на manual cmd")
            flags_reset()
            self.counter_man_mode += 1
            self.crc_ok = False
        
    def _link_indicator(self):

        link_on = QPixmap("./pictures/link_ok.png")
        link_off = QPixmap("./pictures/link_off.png")
        link_err = QPixmap("./pictures/link_err.png")
        link_err_1 = QPixmap("./pictures/link_err_1.png")

        crc_on = QPixmap("./pictures/crc_ok.png")
        crc_off = QPixmap("./pictures/crc_off.png")
        crc_err = QPixmap("./pictures/crc_err.png")
        crc_err_1 = QPixmap("./pictures/crc_err_1.png")

        try:

            if self.ser.is_open:

                if self.counter_man_mode == 0:
                    self.ui.indicator_link.setPixmap(link_on)
                    self.aux_var = 0

                    if self.crc_ok == True:
                        self.ui.indicator_crc.setPixmap(crc_on)

                else:
                    c_indicator = (self.aux_var // 5 ) % 2
                    if c_indicator == 0: 
                        self.ui.indicator_crc.setPixmap(crc_err)
                    if c_indicator == 1: 
                        self.ui.indicator_crc.setPixmap(crc_err_1)
                    self.aux_var += 1

            else:
                self.ui.indicator_link.setPixmap(link_off)
                self.ui.indicator_crc.setPixmap(crc_off)

        except AttributeError as e:
            self.ui.indicator_link.setPixmap(link_off)
            self.ui.indicator_crc.setPixmap(crc_off)

        except Exception as e:
            print(e)

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
        cmd = 'D,s,4,GPS,*,\r\n'.encode("utf-8")
        self.port.write(cmd)
        self.current_text = f'[{self._cur_time()}] - [SEND] - {cmd.decode('utf-8')}' + self.current_text
        self.ui.textBrowser.setText(self.current_text)
    
    
    @QtCore.Slot(object)
    def actns_rcv_gps(self, rcv_msg):
        _calculatedCS = self.estimator.get_CS(rcv_msg)
        _parsedCS = int(rcv_msg.split(',')[-3:-2][0])

        if _calculatedCS != _parsedCS:
            logging.error("CRC error with GPS data")
            return -1
        
        if _calculatedCS == _parsedCS:
            logging.info('GPS data received successfully ')
            self.msg_signals.set_gps_data_to_widget.emit(rcv_msg)
            return 0    
    

    def _get_imu(self):
        """
        Функция запроса координат IMU
        """
        self.port.write(QtCore.QByteArray(bytes('D,s,4,IMU,*,\r\n', 'utf-8')))
        self.current_text = f'[{self._cur_time()}] - [SEND] - D,s,4,IMU,*,\r\n\n' + self.current_text
        self.ui.textBrowser.setText(self.current_text)
    
           
    @QtCore.Slot(object)
    def actns_rcv_imu(self, rcv_msg):
        _calculatedCS = self.estimator.get_CS(rcv_msg)
        _parsedCS = int(rcv_msg.split(',')[-3:-2][0])

        if _calculatedCS != _parsedCS:
            print("Ошибка CRC данных IMU")
            return -1
        
        if _calculatedCS == _parsedCS:
            print('IMU данные получены успешно')
            self.msg_signals.set_imu_data_to_widget.emit(rcv_msg)
            return 0
    
    
    def write_manual(self, direction):
        cmd = f'D,s,3,{direction},{self.pwr_mnl},*,\r\n'
        self.port.write(bytes(cmd, 'utf-8'))
        self._manCS = self.estimator.get_CS(cmd)
        
        self.current_text = f'[{self._cur_time()}] - [SEND] - {cmd}' + self.current_text
        self.ui.textBrowser.setText(self.current_text)
        
      
    @QtCore.Slot(object)
    def actns_rcv_man_perm(self, rcv_msg):
        try:
            _parsedCS = int(rcv_msg.split(',')[-3:-2][0])
        except Exception as e:
            print(e)

        if self._manCS != _parsedCS:
            print("Ошибка записи ручной команды")
            print(f"Получено: {rcv_msg}")
            return -1
        
        if self._manCS == _parsedCS:
            return 0
        
        
    def keyPressEvent(self, event):
        key_press = event.key()

        if key_press == QtCore.Qt.Key.Key_W:
            self.msg_signals.mov_forw.emit()

        if key_press == QtCore.Qt.Key.Key_S:
            self.msg_signals.mov_back.emit()

        if key_press == QtCore.Qt.Key.Key_A:
            self.msg_signals.mov_left.emit()

        if key_press == QtCore.Qt.Key.Key_D:
            self.msg_signals.mov_right.emit()

    
    def actns_press_w(self):

        def _reset_flag():
            self._w_flag = False

        if self._w_flag == True:
            return
        self._w_flag = True
        self.write_manual('F') # Forward
        print('Forward')
        QtCore.QTimer.singleShot(500, _reset_flag)


    def actns_press_s(self):

        def _reset_flag():
            self._s_flag = False

        if self._s_flag == True:
            return
        self._s_flag = True
        self.write_manual('B') # Back
        print('Back')
        QtCore.QTimer.singleShot(500, _reset_flag)


    def actns_press_a(self):

        def _reset_flag():
            self._a_flag = False

        if self._a_flag == True:
            return
        self._a_flag = True
        self.write_manual('L') # Left
        print('Left')
        QtCore.QTimer.singleShot(500, _reset_flag)


    def actns_press_d(self):

        def _reset_flag():
            self._d_flag = False

        if self._d_flag == True:
            return
        self._d_flag = True 
        self.write_manual('R') # Right
        print('Right')
        QtCore.QTimer.singleShot(500, _reset_flag)
    