from PySide6 import QtWidgets, QtGui
from PySide6.QtCore import QThreadPool
from mainwindow_ui import Ui_MainWindow
import datetime

import logging

class Base(QtWidgets.QMainWindow):
    def __init__(self):

        logging.basicConfig(level=logging.INFO, filename="py_log.log", filemode="a")
        
        super(Base, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.setFixedSize(self.size()) 
        self.setWindowTitle("Serial Write-Reader App") 
        self.setWindowIcon(QtGui.QIcon('logo_v2.png'))

        # Для удобства собраны все кнопки в один лист
        self.all_btns = [self.ui.btn_imu, 
                        self.ui.btn_gps,
                        self.ui.btn_mnl_mode,
                        self.ui.btn_auto_mode,
                        self.ui.btn_rmt_mode,
                        self.ui.btn_ctrl_mtr,
                        self.ui.btn_mnl_cmd,]
        
        # Инициализация объекта последовательного порта
        self.ser = None
        self.current_com = None
        for btn in self.all_btns:
                btn.setEnabled(False) # установка неактивного состояния кнопок
        self.ui.btn_disconnect.setEnabled(False) # доп.неакт кнопка "отключиться"

        self.item_in_cb: list = [] # порты доступные в комбобоксе

        self.current_text: str = "" # текст в textBrowser


    def _activate_btns(self):
        """
        Функция активации кнопок управления
        """
        for btn in self.all_btns:
            btn.setEnabled(True)

    def _deactivate_btns(self):
        """
        Функция деактивации кнопок управления
        """
        for btn in self.all_btns:
            btn.setEnabled(False)


    def _cur_time(self):
        return datetime.datetime.now().strftime("%H:%M:%S.%f")[:-3]
    
    
    def _rcv_gps(self, rcv_msg):
        """
            Функция вывода данных GPS в графический интерфейс 
        """

        raw_data, _ = rcv_msg.split('*')
        data = raw_data.split(',')[4:-1]

        self.ui.lb_latitude_val.setText(str(data[0]))
        self.ui.lb_NS_val.setText(str(data[1]))
        self.ui.lb_longitude_val.setText(str(data[2]))
        self.ui.lb_EW_val.setText(str(data[3]))
        self.ui.lb_altitude_val.setText(str(data[4]))
        self.ui.lb_year_val.setText(str(data[5]))
        self.ui.lb_month_val.setText(str(data[6]))
        self.ui.lb_day_val.setText(str(data[7]))
        self.ui.lb_time_val.setText(str(data[8]))
        self.ui.lb_grndSpeed_val.setText(str(data[9]))
        
    def _rcv_imu(self, rcv_msg):
        """
            Функция вывода данных GPS в графический интерфейс 
        """

        raw_data, _ = rcv_msg.split('*')
        data = raw_data.split(',')[4:-1]

        self.ui.lb_AXL_x_val.setText(str(data[0]))
        self.ui.lb_AXL_y_val.setText(str(data[1]))
        self.ui.lb_AXL_z_val.setText(str(data[2]))
        self.ui.lb_MAG_x_val.setText(str(data[3]))
        self.ui.lb_MAG_y_val.setText(str(data[4]))
        self.ui.lb_MAG_z_val.setText(str(data[5]))
        self.ui.lb_GYRO_x_val.setText(str(data[6]))
        self.ui.lb_GYRO_y_val.setText(str(data[7]))
        self.ui.lb_GYRO_z_val.setText(str(data[8]))
        self.ui.lb_GndHeading_val.setText(str(data[9]))
        
        

class Thread(Base):
    def __init__(self):
        super().__init__()
        self.pool = QThreadPool.globalInstance() # Создан пул потоков