from PySide6 import QtWidgets
from PySide6.QtCore import QTimer
from controlline import ControlDataInLineEdit

class ModeController(ControlDataInLineEdit):
    def __init__(self):
        super().__init__()
        
        self.modeTimer = QTimer()
        self.timer.timeout.connect(self._rmode)
        self.timer.start(500)
        
        
        # Кнопкка выбора ручного режима
        self.ui.btn_mnl_mode.clicked.connect(self._manual_mode)
        # Кнопка выбора автономного режима управления
        self.ui.btn_auto_mode.clicked.connect(self._auto_mode)
        # Кнопка выбора дистанционного режима управления
        self.ui.btn_rmt_mode.clicked.connect(self._remote_mode)
       
        
    def _rmode(self):
        if self._fMan_mode == -1 and self._fRmt_mode == -1:
            self.ui.lb_rmode_val.setText('Не выбрано')
            
        if self._fMan_mode == 1:
            self.ui.lb_rmode_val.setText('Ручной')
            
        if self._fRmt_mode == 1:
            self.ui.lb_rmode_val.setText('Дистанционный')
      
            
    def _manual_mode(self) -> None:
        """Ручной режим управления аппаратом (с ПО)""" 
        self._fMan_mode *= -1
        self._fRmt_mode = -1
     
        
    def _remote_mode(self) -> None:
        """Удаленый режим управления аппаратом (с пульта)"""
        self._fRmt_mode *= -1
        self._fMan_mode = -1 
        pass
    
    
    def _auto_mode(self) -> None:
        """Автоматический режим управления аппаратом"""
        pass
    