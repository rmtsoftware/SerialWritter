from PySide6.QtCore import QObject, Signal, QRunnable
import datetime

class ReaderSignals(QObject):
    get_data = Signal()


class Reader(QRunnable):
    def __init__(self, ser):
        super().__init__()
        self.ser = ser
        self.signals = ReaderSignals()
        self.glob_line = ''
        self.glob_stop = False
        
        self.glob_cs_man_mode = None

    def run(self):
        while True:
            try:
                if self.ser.is_open:
                    line = self.ser.readline()
                    sline = str(line, 'UTF-8')


                    #if sline[0:5] == 'D,s,1':
                    if sline[0:5] == 'D,s,3':
                         self.glob_cs_man_mode = 55

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