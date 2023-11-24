from PySide6.QtCore import QObject, Signal, QRunnable
import datetime
import ctypes
from random import randint

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
        self.checkSum = ctypes.cdll.LoadLibrary('.\\c_module\\checksum.dll')
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
        
        self.gps_data_ok = False
        self.imu_data_ok = False
        

    def  __base_proccesor(self, sline):
        """ Обработка полученной строки """
        def parse_gps_data(raw_data):
            """ Парсер """
            return raw_data.split(',')[4:-1]

        # Вычисление контрольной суммы полученного сообщения
        _cS = ord(self.checkSum.calculateChecksum(sline.encode('utf-8')))

        # Извлечение контрольной суммы и даты из полученного сообщения
        raw_data, raw_cs = sline.split('*')
        rcv_cs = int(raw_cs.split(',')[1])

        
        print(_cS, rcv_cs)
        print(type(_cS), type(rcv_cs))
        # Ошибка контрольной суммы
        if rcv_cs != _cS:
            if 'D,s,1':
                self.signals.fault_checksum_gps_data.emit()
                return [0 for _ in range(10)]
            if 'D,s,2':
                self.signals.fault_checksum_imu_data.emit()
                return [0 for _ in range(10)]
        else:
            data = parse_gps_data(raw_data)
            return data


    def _gps_proccesor(self, sline):
        
        self.gps_data_ok = False
        
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
        
        self.gps_data_ok = True
        


    def _imu_proccesor(self, sline):
        
        self.imu_data_ok = False
        
        def unpack(val):
            try:
                return int(val)
            except Exception as e:
                print(val)
                print(e)
                return 0
  
        """
        Обработчик IMU строки
        """
        
        _c = 0
        
        data = self.__base_proccesor(sline)
        # Запись в атрибуты класса
        
        try:
            self.AXL_x = unpack(data[0])
        except Exception as e:
            print("Ошибка запис AXL_x")
            _c += 1

        try:    
            self.AXL_y =  unpack(data[1])
        except Exception as e:
            print("Ошибка записи AXL_y")
            _c += 1

        try:    
            self.AXL_z = unpack(data[2])
        except Exception as e:
            print("Ошибка записи AXL_Z")
            _c += 1

        try:    
            self.MAG_x = unpack(data[3])
        except Exception as e:
            print("Ошибка записи MAG_x")
            _c += 1

        try:    
            self.MAG_y = unpack(data[4])
        except Exception as e:
            print("Ошибка записи MAG_y")
            _c += 1

        try:    
            self.MAG_z = unpack(data[5])
        except Exception as e:
            print("Ошибка записи MAG_z")
            _c += 1

        try:    
            self.GYRO_x = unpack(data[6])
        except Exception as e:
            print("Ошибка записи GYRO_x")
            _c += 1

        try:   
            self.GYRO_y = unpack(data[7])
        except Exception as e:
            print("Ошибка записи GYRO_y")
            _c += 1

        try:    
            self.GYRO_z = unpack(data[8])
        except Exception as e:
            print("Ошибка записи GYRO_z")
            _c += 1

        try:
            self.Gnd_Heading = unpack(data[9])
        except Exception as e:
            print("Ошибка записи Gnd_Heading")
            _c += 1
            
        # Сигнал успешно полученны данные
        self.signals.rcv_imu_data.emit()

        if _c == 0:
            self.imu_data_ok = True
        else:
            _c = 0

    def _man_cmd_request(self, sline):
        rcv_cs = sline.split('*')[1].split(',')[1]
        self.glob_cs_man_mode = rcv_cs


    def run(self):
        while True:
            try:

                if self.ser.is_open:
                    line = self.ser.readline()
                    sline = str(line, 'UTF-8')

                    #sline = 'D,s,1,49,5949.08250,N,03019.66393,S,00155.5,2023,10,23,180723.00,0.004,*,96,\r,\n'
                    #sline = 'D,s,1,49,5949.08250,N00155.5,2023,10,23,180723.00,0.004,*,96,\r,\n'
                    #sline = f'D,s,1,49,5949.08250,N,03019.66393,S,00155.5,2023,10,23,180723.00,0.004,*,{96 + randint(0,1)},\r,\n'
                    
                    sline = "D,s,2,65535,65535,65535,65535,65535,65535,65535,65535,65535,65535,185,*,81,\r,\n"
                    _msg_type = sline[0:5]
                    match _msg_type:
                        case 'D,s,1':
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