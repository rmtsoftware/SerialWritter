from PySide6.QtCore import QIODevice, QTimer, Signal, QObject, Slot, QByteArray
from PySide6 import QtSerialPort
from messager import Messager
from estimator import EstimatorCS
from base import Thread
import logging
import random

class _nSignals(QObject):
    get_gps = Signal(object)
    get_imu = Signal(object)
    get_man_perm = Signal(object)
    mov_forw = Signal()
    mov_back = Signal()
    mov_left = Signal()
    mov_right = Signal()
    
    set_gps_data_to_widget = Signal(object)
    set_imu_data_to_widget = Signal(object)
    
    data_send = Signal(object)
    
    


class SerialConnector(Thread):
    def __init__(self):
        super().__init__()
        
        # Кнопки подключени/отключения в последовательному устройству
        self.ui.btn_connect.clicked.connect(self.connect_to_ser_dev)
        self.ui.btn_disconnect.clicked.connect(self.disconnect_from_ser_dev)
        
        # Создание объекта последовательного порта
        self.port = QtSerialPort.QSerialPort()
        self.port.readyRead.connect(self.readFromSerial)

        # Получение и обновление доступных COM-портов каждую 1 с
        self.timer = QTimer()
        self.timer.timeout.connect(self._add_item_to_cb)
        self.timer.start(1000)
        
        # Инициализация сигналов
        self.msg_signals = _nSignals()
        
        # Инициализация вычислителя контрольной суммы
        self.estimator = EstimatorCS()
        
        self.buffer = ''

        
    def __init_serial_port(self, current_port, current_brate):
        self.port.setPortName(current_port)
        
        if current_brate == 9600:
            self.port.setBaudRate(QtSerialPort.QSerialPort.BaudRate.Baud9600)
        
        if current_brate == 115200:
            self.port.setBaudRate(QtSerialPort.QSerialPort.BaudRate.Baud115200)
            
        self.port.setParity(QtSerialPort.QSerialPort.Parity.NoParity)
        self.port.setDataBits(QtSerialPort.QSerialPort.DataBits.Data8)
        self.port.setStopBits(QtSerialPort.QSerialPort.StopBits.OneStop)
     
        
    def start_listen(self, current_port, current_brate):
        self.__init_serial_port(current_port, current_brate)
        self.port.open(QIODevice.OpenModeFlag.ReadWrite)
        self.port.setDataTerminalReady(True)
        self._activate_btns()
        
        self.timer1 = QTimer()
        self.timer1.timeout.connect(self._get_imu)
        self.timer1.start(1000)
        
    
    
    def stop_listen(self):
        self.port.clear()
        self.port.close()
        self._deactivate_btns()
        self.timer1.stop()

    
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
            self.start_listen(self.current_com, self.current_brate)
             
        # Ошибка возникающая при недоустпности / неопределённости устройства
        # по указанному com-порту
        except Exception as e:
            print(e) 
        ####### except serial.serialutil.SerialException as e:
        #######     Messager._indefinite_dev(self.current_com)
        #######     return
        
        # Вызов инф.сообщения
        Messager._dev_connected(self.current_com)

        self.ui.btn_connect.setEnabled(False)
        self.ui.btn_disconnect.setEnabled(True)

        #self.reader.signals.rcv_gps_data.connect(self._rcv_gps) # Сигнал упешного получения gps данных
        #self.reader.signals.rcv_imu_data.connect(self._rcv_imu) # Сигнал упешного получения imu данных
        #self.reader.signals.fault_checksum_gps_data.connect(self._f_checksum_gps) # Сигнал ошибки контрольной суммы GPS
        #self.reader.signals.fault_checksum_imu_data.connect(self._f_checksum_imu) # Сигнал ошибки контрольной суммы IMU
        #self.reader.signals.get_data.connect(self._rcv_data) # Общий сигнал получения даты для записи в окно терминала
    
    def disconnect_from_ser_dev(self):
        """
        Отключение от последовательного устройства
        """
        self.stop_listen()
        Messager._dev_disconnect(self.current_com) # вызов инф.сообщения
        self.ui.btn_connect.setEnabled(True)
        self.ui.btn_disconnect.setEnabled(False)
        self.current_com = None
    
        
    def readFromSerial(self):
        try:
            """
            Основная функция чтения данных из последовательного порта
            """
            DEBUG = True

            _b_resp = self.port.readAll().data()
            _resp0 =  bytes(_b_resp).decode()

            self.buffer += _resp0

            coindence = 0
            for idx, sym in enumerate(self.buffer):
                if sym == '\r':
                    try:
                        if self.buffer[idx+1] == '\n':
                            _resp = self.buffer[0:idx+2]
                            self.buffer = self.buffer[idx+3:]
                            coindence += 1
                            break
                    except IndexError as e:
                        continue
                    
            if coindence == 0:
                return

            if DEBUG == True:                            
                if _resp == 'D,s,4,GPS,*\r\n': _resp = self.TESTGPSDATA[random.randint(0, len(self.TESTGPSDATA)-1)]
                #if _resp == 'D,s,4,GPS,*,\r\n': print('ya zdes')
                elif _resp == 'D,s,4,IMU,*\r\n': _resp = self.TESTIMUDATA[random.randint(0, len(self.TESTIMUDATA)-1)]
                elif _resp == 'D,s,3,F,100,*\r\n': _resp = 'D,s,3,*55\r\n'
                elif _resp == 'D,s,3,B,100,*\r\n': _resp = 'D,s,3,*51\r\n'
                elif _resp == 'D,s,3,R,100,*\r\n': _resp = 'D,s,3,*35\r\n'
                elif _resp == 'D,s,3,L,100,*\r\n': _resp = 'D,s,3,*61\r\n'
                else: pass
                
        except Exception as e:
            err = f'{[{self._cur_time()}]} - {e}'
            logging.error(err)
            
            
        self._add_to_textBrowser(_resp)
        
        if _resp[0:7] == 'D,s,1,1':
            self.msg_signals.get_gps.emit(_resp)
            
        if _resp[0:7] == 'D,s,1,2':
            self.msg_signals.get_imu.emit(_resp)
            
        if _resp[0:5] == 'D,s,3':
            self.msg_signals.get_man_perm.emit(_resp)
    
            
    def _add_to_textBrowser(self, data):
        """
        Добавление записи в окно вывода текста
        """
        self.current_text = f'[{self._cur_time()}] - [RCVD] -\t' + data + self.current_text
        self.ui.textBrowser.setText(self.current_text)
        to_log = f'[{self._cur_time()}] - [RCVD] -\t' + data
        logging.info(to_log[0:-2])
        
        
    # При закрытии приложениии автоматически закрывается открытый ранее порт
    # если какая то ошибка то записывается в log
    def closeEvent(self, event):
        try:
            self.stop_listen()
        except AttributeError as _ :
            pass
        except Exception as e:
            logging.error("Ошибка при закрытии: ↓↓↓↓↓↓")
            logging.error(e)
        finally:
            event.accept()
