from PySide6 import QtWidgets
from mainwindow_ui import Ui_MainWindow
from PySide6.QtCore import QThreadPool

class Base(QtWidgets.QMainWindow):
    def __init__(self):

        super(Base, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # Для удобства собраны все кнопки в один лист
        self.all_btns = [self.ui.btn_imu, 
                        self.ui.btn_gps,
                        self.ui.btn_mnl_mode,
                        self.ui.btn_auto_mode,
                        self.ui.btn_rmt_mode,
                        self.ui.btn_ctrl_mtr,]
        
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
        if self.ser.is_open:
            for btn in self.all_btns:
                btn.setEnabled(True)

    def _deactivate_btns(self):
        """
        Функция деактивации кнопок управления
        """
        if not self.ser.is_open:
            for btn in self.all_btns:
                btn.setEnabled(False)
        
        

class Thread(Base):
    def __init__(self):
        super().__init__()
        self.pool = QThreadPool.globalInstance() # Создан пул потоков