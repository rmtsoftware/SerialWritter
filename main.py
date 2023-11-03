from PySide6 import QtWidgets
import sys
from cbprocessor import ComboBoxProcesser


class BtnsFunctionality(ComboBoxProcesser):
    def __init__(self):
        super().__init__()

        # кнопки запроса gps и imu
        self.ui.btn_gps.clicked.connect(self._get_gps)
        self.ui.btn_imu.clicked.connect(self._get_imu)

        # кнопки выбора режима управления
        self.ui.btn_mnl_mode.clicked.connect(self.manual_mode)
        self.ui.btn_auto_mode.clicked.connect(self.auto_mode)
        self.ui.btn_rmt_mode.clicked.connect(self.remote_mode)

        # кнопка запуска/остановки двигателя
        self.ui.btn_ctrl_mtr.clicked.connect(self.ctrl_motor)
        
        # кнопка очистки окна вывода текста
        self.ui.btn_clean_textBrw.clicked.connect(self._clr_text_brw)

    
    def manual_mode(self):
        """Ручной режим управления аппаратом"""
        pass

    def auto_mode(self):
        """Автоматический режим управления аппаратом"""
        pass

    def remote_mode(self):
        """Удаленый режим управления аппаратом (с пульта)"""
        pass

    def ctrl_motor(self):
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
        self.ser.write(b'D,s,4,GPS,*,\r\n')
        self.current_text = f'[{self._cur_time()}] - [SEND] - D,s,4,GPS,*,\r\n\n' + self.current_text
        self.ui.textBrowser.setText(self.current_text)


    def _get_imu(self):
        """
        Функция запроса координат IMU
        """
        self.ser.write(b'D,s,4,IMU,*,\r\n')
        self.current_text = f'[{self._cur_time()}] - [SEND] - D,s,4,IMU,*,\r\n\n' + self.current_text
        self.ui.textBrowser.setText(self.current_text)



if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = BtnsFunctionality()
    window.mouseMoveEvent = window.mouseMoveEvent
    window.show()
    sys.exit(app.exec())
