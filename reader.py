from PySide6.QtCore import QObject, Signal, QRunnable
import datetime
import ctypes

class ReaderSignals(QObject):
    get_data = Signal()

    rcv_gps_data = Signal()
    rcv_imu_data = Signal()

    fault_checksum_gps_data = Signal()
    fault_checksum_imu_data = Signal()


class Reader(QRunnable):
    def __init__(self, ser):
        super().__init__()
        self.ser = ser
        self.signals = ReaderSignals()
        self.glob_line = ''
        self.glob_stop = False

        # Инициализация объекта подсчёта контрольной суммы на основе С-функции
        self.checkSum = ctypes.cdll.LoadLibrary('C:\\Users\\m.ishchenko\\Desktop\\Projects\\ANPA\\SerWritter\\c_module\\checksum.dll')
        self.checkSum.calculateChecksum.restype = ctypes.c_char
        self.checkSum.calculateChecksum.argtypes = [ctypes.POINTER(ctypes.c_char), ]

        # GPS
        self.Latitude: float = 0.0
        self.NS: str = 'N'
        self.Longitude: float = 0.0
        self.EW: str = 'E'
        self.Altitude: float = 0.0
        self.Year: int = 0
        self.Month: int = 0
        self.Day: int = 0
        self.Time: float = 0.0
        self.GrndSpeed: float = 0.0

        # IMU
        self.AXL_x: int = 0
        self.AXL_y: int = 0
        self.AXL_z: int = 0
        self.MAG_x: int = 0
        self.MAG_y: int = 0
        self.MAG_z: int = 0
        self.GYRO_x: int = 0
        self.GYRO_y: int = 0
        self.GYRO_z: int = 0
        self.Gnd_Heading: int = 0

        #MANUAL CMD
        self.glob_cs_man_mode = None


    def __base_proccesor(self, sline):
        """ Обработка полученной строки """
        def parse_gps_data(raw_data):
            """ Парсер """
            return raw_data.split(',')[4:-1]

        # Вычисление контрольной суммы полученного сообщения
        _cS = ord(self.checkSum.calculateChecksum(sline.encode('utf-8')))
        
        # Извлечение контрольной суммы и даты из полученного сообщения
        raw_data, raw_cs = sline.split('*')
        rcv_cs = int(raw_cs.split(',')[1])

        # Ошибка контрольной суммы
        if rcv_cs != _cS:
            if 'D,s,1':
                self.signals.fault_checksum_gps_data.emit()
                return
            if 'D,s,2':
                self.signals.fault_checksum_imu_data.emit()
                return    
        else:
            data = parse_gps_data(raw_data)
            return data


    def _gps_proccesor(self, sline):
        """
        Обработчик GPS строки
        """
        data = self.__base_proccesor(sline)
        # Запись в атрибуты класса
        self.Latitude = float(data[0])
        self.NS: str = data[1]
        self.Longitude = float(data[2])
        self.EW = data[3]
        self.Altitude = float(data[4])
        self.Year = int(data[5])
        self.Month = int(data[6])
        self.Day = int(data[7])
        self.Time = float(data[8])
        self.GrndSpeed = float(data[9])
        # Сигнал успешно полученны данные
        self.signals.rcv_gps_data.emit()
        


    def _imu_proccesor(self, sline):
        """
        Обработчик IMU строки
        """
        data = self.__base_proccesor(sline)
        # Запись в атрибуты класса
        self.AXL_x = int(data[0])
        self.AXL_y =  int(data[1])
        self.AXL_z = int(data[2])
        self.MAG_x = int(data[3])
        self.MAG_y = int(data[4])
        self.MAG_z = int(data[5])
        self.GYRO_x = int(data[6])
        self.GYRO_y = int(data[7])
        self.GYRO_z = int(data[8])
        self.Gnd_Heading = int(data[9])
        # Сигнал успешно полученны данные
        self.signals.rcv_imu_data.emit()

    def _man_cmd_request(self, sline):
        rcv_cs = sline.split('*')[1].split(',')[1]
        self.glob_cs_man_mode = rcv_cs


    def run(self):
        while True:
            try:

                if self.ser.is_open:
                    line = self.ser.readline()
                    sline = str(line, 'UTF-8')

                    sline = 'D,s,3,*,54,\r\n'

                    _msg_type = sline[0:5]
                    match _msg_type:
                        case 'D,s,1':
                            print('i m here') 
                            self._gps_proccesor(sline) # Полученны данные GPS
                        case 'D,s,2': 
                            self._imu_proccesor(sline) # Полученны данные IMU
                        case 'D,s,3':
                            self._man_cmd_request(sline) # Получен ответ на ручную команду управления
                        case _:
                            print('Undefined command') # Неизвестная команда

                    cut_time = datetime.datetime.now().strftime("%H:%M:%S.%f")[:-3]
                    self.glob_line = f'[{cut_time}] - [RECIEVED] - {sline}\n'
                    self.signals.get_data.emit()
                    
                if not self.ser.is_open:
                    return
                
            except:

                if self.glob_stop:
                    break

        return 0