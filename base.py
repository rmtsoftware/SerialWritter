from PySide6 import QtWidgets, QtGui
from estimator import EstimatorCS
from mainwindow_ui import Ui_MainWindow
import datetime
import logging
from _resources import _signals, _my_test_data

class Base(QtWidgets.QMainWindow):
    def __init__(self):

        # Конфиг логгирования
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
        
        # Значение режима
        self.ui.lb_rmode_val.setText('Не выбран')
        
        # Инициализация объекта последовательного порта
        self.ser = None
        self.current_com = None
        for btn in self.all_btns:
            btn.setEnabled(False) # установка неактивного состояния кнопок
        self.ui.btn_disconnect.setEnabled(False) # доп.неакт кнопка "отключиться"
        self.ui.le_pwr_mnl.setReadOnly(True) # при запуске ПО, до подключения к клиенту, запись в лайнЭдит недоступна
        self.ui.le_mnl_cmd.setReadOnly(True) # при запуске ПО, до подключения к клиенту, запись в лайнЭдит недоступна
        
        self.item_in_cb: list = [] # порты доступные в комбобоксе

        self.current_text: str = "" # текст в textBrowser

        self._set_zeros_gps() # установить "0" в вывод данных gps
        self._set_zeros_imu() # установить "0" в вывод данных imu
        
        # Набор тестовых данных GPS
        self.TESTGPSDATA = _my_test_data.TESTGPSDATA
        
        # Набор тестовых данных IMU
        self.TESTIMUDATA = _my_test_data.TESTIMUDATA
        
        # Инициализация сигналов
        self.msg_signals = _signals._nSignals()
        
        # Инициализация вычислителя контрольной суммы
        self.estimator = EstimatorCS()
        
        self.buffer = ''
        
        self._fMan_mode = -1 # флаг выбора ручного режима
        self._fRmt_mode = -1 # флаг выбора дистанционного режима
    
        
    def _set_zeros_gps(self):    
         #Установка нулевых значений в фрейм "Данные GPS"
        self.ui.lb_latitude_val.setText('0')
        self.ui.lb_NS_val.setText('0')
        self.ui.lb_longitude_val.setText('0')
        self.ui.lb_EW_val.setText('0')
        self.ui.lb_altitude_val.setText('0')
        self.ui.lb_time_val.setText('0')
        self.ui.lb_grndSpeed_val.setText('0')
        self.ui.lb_rmc_cource_val.setText('0')

    
    def _set_zeros_imu(self):
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
 
     
    def _activate_btns(self):
        """
        Функция активации кнопок управления
        """
        for btn in self.all_btns:
            btn.setEnabled(True)
        self.ui.le_pwr_mnl.setReadOnly(False)
        self.ui.le_mnl_cmd.setReadOnly(False)


    def _deactivate_btns(self):
        """
        Функция деактивации кнопок управления
        """
        for btn in self.all_btns:
            btn.setEnabled(False)
        self.ui.le_pwr_mnl.setReadOnly(True)
        self.ui.le_mnl_cmd.setReadOnly(True)
        

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
        self.ui.lb_time_val.setText(str(data[5]))
        self.ui.lb_grndSpeed_val.setText(str(data[6]))
        self.ui.lb_rmc_cource_val.setText(str(data[7]))
        
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
        
    def _reset_modes(self):
        self._fMan_mode = -1
        self._fRmt_mode = -1
