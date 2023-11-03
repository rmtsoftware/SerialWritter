from PySide6 import QtWidgets
import datetime
import sys
from cbprocessor import ComboBoxProcesser


class BtnsFunctionality(ComboBoxProcesser):
    def __init__(self):
        super().__init__()

        self.ui.btn_gps.clicked.connect(self._get_gps)
        self.ui.btn_imu.clicked.connect(self._get_imu)
        self.ui.btn_clean_textBrw.clicked.connect(self._clr_text_brw)

    def _cur_time(self):
        return datetime.datetime.now().strftime("%H:%M:%S.%f")[:-3]


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
        self.ser.write(b'D,s,4,GPS,*,\r\n')
        self.current_text += f'[{self._cur_time()}] - [SEND] - D,s,4,GPS,*,\r\n'
        self.ui.textBrowser.setText(self.current_text)


    def _get_imu(self):
        """
        Функция запроса координат IMU
        """
        self.ser.write(b'D,s,4,IMU,*,\r\n')
        self.current_text += f'[{self._cur_time()}] - [SEND] - D,s,4,IMU,*,\r\n'
        self.ui.textBrowser.setText(self.current_text)


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = BtnsFunctionality()
    window.mouseMoveEvent = window.mouseMoveEvent
    window.show()
    sys.exit(app.exec())
