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
        
        self.TESTGPSDATA =  ["D,s,1,49,5949.0825,N,3019.6630,S,155.5,2023,10,23,180723.00,0.004,*90\r\n",
                             "D,s,1,30,5519.9819,N,2047.4720,E,15.2,123736,38.000,48.000,*122\r\n",
                             "D,s,1,31,5519.9858,N,2047.4790,E,15.2,123737,38.000,48.000,*116\r\n",
                             "D,s,1,32,5519.9902,N,2047.4860,E,15.2,123738,38.000,48.000,*118\r\n",
                             "D,s,1,33,5519.9941,N,2047.4930,E,15.2,123739,38.000,48.000,*117\r\n",
                             "D,s,1,34,5519.9980,N,2047.5000,E,15.2,123740,38.000,48.000,*122\r\n",
                             "D,s,1,35,5520.0020,N,2047.5070,E,15.2,123741,38.000,48.000,*125\r\n",
                             "D,s,1,36,5520.0059,N,2047.5140,E,15.2,123742,38.000,48.000,*113\r\n",
                             "D,s,1,37,5520.0098,N,2047.5210,E,15.2,123743,38.000,48.000,*122\r\n",
                             "D,s,1,38,5520.0142,N,2047.5280,E,15.2,123744,38.000,48.000,*125\r\n",
                             "D,s,1,39,5520.0181,N,2047.5350,E,15.2,123745,38.000,48.000,*126\r\n",
                             "D,s,1,40,5520.0220,N,2047.5420,E,15.2,123746,38.000,48.000,*123\r\n",
                             "D,s,1,41,5520.0259,N,2047.5490,E,15.2,123747,38.000,48.000,*126\r\n",
                             "D,s,1,42,5520.0298,N,2047.5560,E,15.2,123748,38.000,48.000,*113\r\n",
                             "D,s,1,43,5520.0342,N,2047.5630,E,15.2,123749,38.000,48.000,*113\r\n",
                             "D,s,1,44,5520.0381,N,2047.5699,E,15.2,123750,38.000,48.000,*114\r\n",
                             "D,s,1,45,5520.0420,N,2047.5770,E,15.2,123751,38.000,48.000,*120\r\n",
                             "D,s,1,46,5520.0459,N,2047.5840,E,15.2,123752,38.000,48.000,*122\r\n"]
        
        self.TESTIMUDATA = ["D,s,1,2,546,21068,15139,11540,4355,8600,28862,20656,15206,168.000,*65\r\n",
                            "D,s,1,2,29991,19308,27712,3152,3457,30389,3007,17862,2765,127.750,*69\r\n",
                            "D,s,1,2,21525,29552,4778,7642,9433,15707,29108,23579,12797,112.000,*120\r\n",
                            "D,s,1,2,23128,4975,15973,27878,27700,18411,24176,20337,26680,165.900,*113\r\n",
                            "D,s,1,2,5950,438,23705,7642,18554,25740,24785,30412,5952,123.550,*122\r\n",
                            "D,s,1,2,4065,49,4945,8662,16179,15358,3197,21111,20204,30.800,*77\r\n",
                            "D,s,1,2,14740,15156,15384,14644,13385,12451,3804,6668,3410,309.050,*125\r\n",
                            "D,s,1,2,29546,12775,1050,11150,11547,24655,15619,26767,16825,246.750,*124\r\n",
                            "D,s,1,2,21466,3503,6915,828,1110,19558,15928,5122,21874,290.850,*69\r\n",
                            "D,s,1,2,29013,16276,14300,24836,9446,3511,17721,4593,12491,168.350,*116\r\n",
                            "D,s,1,2,23030,6376,27554,17160,3617,26250,24937,11266,25307,185.500,*71\r\n",
                            "D,s,1,2,31085,6233,19167,3377,333,24855,17178,20629,26180,277.200,*70\r\n",
                            "D,s,1,2,23591,5844,12034,1051,27863,21885,3281,19637,22307,66.850,*71\r\n",
                            "D,s,1,2,15370,16632,18545,30962,2653,2906,24326,4229,9533,8.050,*67\r\n",
                            "D,s,1,2,15584,21245,31428,5663,19367,10738,22455,1157,8613,1.400,*125\r\n",
                            "D,s,1,2,3511,27437,3336,20685,20406,1979,16648,26949,17425,303.800,*123\r\n",
                            "D,s,1,2,27633,13287,17832,22646,16137,31688,2549,11967,7989,222.600,*74\r\n",
                            "D,s,1,2,17966,17373,26156,13763,26134,29892,22576,23750,672,105.000,*64\r\n",
                            "D,s,1,2,12208,13449,17122,18039,4210,27267,25977,7017,21040,319.200,*68\r\n",
                            "D,s,1,2,19166,21460,22804,8206,23980,10523,27982,9724,19112,252.000,*78\r\n"]
        
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