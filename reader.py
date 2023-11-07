from PySide6.QtCore import QObject, Signal, QRunnable
import datetime
import ctypes

class ReaderSignals(QObject):
    get_data = Signal()

    rcv_gps_data = Signal()
    fault_checksum_gps_data = Signal()


class Reader(QRunnable):
    def __init__(self, ser):
        super().__init__()
        self.ser = ser
        self.signals = ReaderSignals()
        self.glob_line = ''
        self.glob_stop = False

        # инициализация объекта подсчёта контрольной суммы на основе С-функции
        self.checkSum = ctypes.cdll.LoadLibrary('C:\\Users\\m.ishchenko\\Desktop\\Projects\\ANPA\\SerWritter\\c_module\\checksum.dll')
        self.checkSum.calculateChecksum.restype = ctypes.c_char
        self.checkSum.calculateChecksum.argtypes = [ctypes.POINTER(ctypes.c_char), ]
        
        self.glob_cs_man_mode = None

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

    def _gps_proccesor(self, sline):

        def parse_gps_data(raw_data):
            return raw_data.split(',')[4:-1]

        """ Обработка строки после запроса GPS """
        # Вычисление контрольной суммы полученного сообщения
        _cS = ord(self.checkSum.calculateChecksum(sline.encode('utf-8')))
        
        # Извлечение контрольной суммы и даты из полученного сообщения
        raw_data, raw_cs = sline.split('*')
        rcv_cs = int(raw_cs.split(',')[1]) - 1

        # Ошибка контрольной суммы
        if rcv_cs != _cS:
            self.signals.fault_checksum_gps_data.emit()
                    
        else:

            # Запись данных в атрибуты класса. Для получения в дальнейшем в глобальной области приложения
            Latitude, NS, Longitude, EW, Altitude, Year, Month, Day, Time, GrndSpeed = parse_gps_data(raw_data)
            self.Latitude = float(Latitude)
            self.NS: str = NS
            self.Longitude = float(Longitude)
            self.EW = EW
            self.Altitude = float(Altitude)
            self.Year = int(Year)
            self.Month = int(Month)
            self.Day = int(Day)
            self.Time = float(Time)
            self.GrndSpeed = float(GrndSpeed)

            # Сигнал успешно полученных данных
            self.signals.rcv_gps_data.emit()

    def run(self):
        while True:
            try:
                if self.ser.is_open:
                    line = self.ser.readline()
                    sline = str(line, 'UTF-8')
                    sline = "D,s,1,49,5949.08250,N,03019.66393,S,00155.5,2023,10,23,180723.00,0.004,*,$,\r,\n"

                    match sline[0:5]:
                        case 'D,s,1': self._gps_proccesor(sline) # Полученны данные GPS
                        case _: pass


                    #if sline[0:5] == 'D,s,3':
                    #     self.glob_cs_man_mode = 55

                    cut_time = datetime.datetime.now().strftime("%H:%M:%S.%f")[:-3]
                    self.glob_line = f'[{cut_time}] - [RECIEVED] - {sline}\n'
                    self.signals.get_data.emit()
                    
                if not self.ser.is_open:
                    return
            except:
                if self.glob_stop:
                    break
                pass
        return 0