
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

        # кнопки запроса gps и imu
        self.ui.btn_gps.clicked.connect(self._get_gps)
        self.ui.btn_imu.clicked.connect(self._get_imu)

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

        # инициализация объекта подсчёта контрольной суммы на основе С-функции
        self.test = ctypes.cdll.LoadLibrary('.\\c_module\\checksum.dll')
        self.test.calculateChecksum.restype = ctypes.c_char
        self.test.calculateChecksum.argtypes = [ctypes.POINTER(ctypes.c_char), ]

        self.man_mode_flag = False
        self.gps_mode_flag = False
        self.imu_mode_flag = False
        
        self.counter_man_mode = 0

        # Отображение статуса связи
        self.link_timer = QtCore.QTimer()
        self.link_timer.timeout.connect(self._link_indicator)
        self.link_timer.start(100)
        self.aux_var = 0
        self.crc_ok = False
        
        #Установка нулевых значений в фрейм "Данные GPS"
        self.ui.lb_latitude_val.setText('0')
        self.ui.lb_NS_val.setText('0')
        self.ui.lb_longitude_val.setText('0')
        self.ui.lb_EW_val.setText('0')
        self.ui.lb_altitude_val.setText('0')
        self.ui.lb_year_val.setText('0')
        self.ui.lb_month_val.setText('0')
        self.ui.lb_day_val.setText('0')
        self.ui.lb_time_val.setText('0')
        self.ui.lb_grndSpeed_val.setText('0')
        
        #Установка нулевых значений в фрейм "Данные IMU"
        self.ui.lb_AXL_x_val.setText('0')
        self.ui.lb_AXL_y_val.setText('0')
        self.ui.lb_AXL_z_val.setText('0')
        self.ui.lb_MAG_x_val.setText('0')
        self.ui.lb_MAG_y_val.setText('0')
        self.ui.lb_MAG_z_val.setText('0')
        self.ui.lb_GYRO_x_val.setText('0')
        self.ui.lb_GYRO_y_val.setText('0')
        self.ui.lb_GYRO_z_val.setText('0')
        self.ui.lb_GndHeading_val.setText('0')


    def send_mnl_cmd(self):
        logging.info(f"function send_mnl_cmd was called")
        # Получение текста из QLineEdit
        msg = str(self.ui.le_mnl_cmd.text())

        full_str = msg + '\r\n' 
        # Запись в порт
        self.ser.write(bytes(full_str, encoding='utf-8'))
        
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
        
        if self.gps_mode_flag == True:
            return
        
        self.ser.write(b'D,s,4,GPS,*,\r\n')
        self.current_text = f'[{self._cur_time()}] - [SEND] - D,s,4,GPS,*,\r\n\n' + self.current_text
        self.ui.textBrowser.setText(self.current_text)
        
        self.gps_mode_flag = True
        self.gpsTimer = QtCore.QTimer.singleShot(1000, self._gpsTimerActions)
        
    def _gpsTimerActions(self):
        if self.reader.gps_data_ok: print('GPS data ok')
        else: print('GPS data FAULT')
        self.gps_mode_flag = False
        self.reader.gps_data_ok = False


    def _get_imu(self):
        """
        Функция запроса координат IMU
        """
        
        if self.imu_mode_flag == True:
            return
        
        self.ser.write(b'D,s,4,IMU,*,\r\n')
        self.current_text = f'[{self._cur_time()}] - [SEND] - D,s,4,IMU,*,\r\n\n' + self.current_text
        self.ui.textBrowser.setText(self.current_text)
        
        self.imu_mode_flag = True
        
        self.imuTimer = QtCore.QTimer.singleShot(1000, self._imuTimerActions)

    def _imuTimerActions(self):
        if self.reader.imu_data_ok: pass
        else: pass
        self.imu_mode_flag = False
        self.reader.imu_data_ok = False

