from modectrl import ModeController
from PySide6.QtWidgets import QCheckBox
from PySide6.QtCore import Qt, QTimer
import time

class AutoRequest(ModeController):
    def __init__(self):
        super().__init__()
        
        self.ui.checkBox_auto_gps.stateChanged.connect(self._auto_gps_actions)
        self.ui.checkBox_auto_imu.stateChanged.connect(self._auto_imu_actions)
        
        self._fAuto_gps = 0
        self._fAuto_imu = 0
        
        self.AutoRqrTimer = QTimer()
        self.AutoRqrTimer.timeout.connect(self._auto_request)
        self.AutoRqrTimer.start(1000)
        
        
    def _auto_gps_actions(self):

        if self.ui.checkBox_auto_gps.checkState() == Qt.CheckState.Unchecked:
            self._fAuto_gps -= 1 
            
        if self.ui.checkBox_auto_gps.checkState() == Qt.CheckState.Checked:
            self._fAuto_gps += 1 
            
        print(f'Auto GPS {self._fAuto_gps}')
    
    def _auto_imu_actions(self):
        
        if self.ui.checkBox_auto_imu.checkState() == Qt.CheckState.Unchecked:
            self._fAuto_imu -= 1
            
        if self.ui.checkBox_auto_imu.checkState() == Qt.CheckState.Checked:
            self._fAuto_imu += 1
            
        print(f'Auto IMU {self._fAuto_imu}')
        
    def _auto_request(self):
        
        if self.port.isOpen():
            
            if self._fAuto_gps == 1 and self._fAuto_imu == 0:
                self._get_gps()
                self.ui.btn_gps.setEnabled(False)
            else:
                self.ui.btn_gps.setEnabled(True)


            if self._fAuto_imu == 1 and self._fAuto_gps == 0:
                self._get_imu()
                self.ui.btn_imu.setEnabled(False)
            else:
                self.ui.btn_imu.setEnabled(True)


            if self._fAuto_imu == 1 and self._fAuto_gps == 1:
                self.ui.btn_imu.setEnabled(False)
                self.ui.btn_gps.setEnabled(False)

                self._get_gps()
                QTimer.singleShot(200, self._get_imu)
                
            if self._fAuto_imu == 0 and self._fAuto_gps == 0:
                self.ui.btn_imu.setEnabled(True)
                self.ui.btn_gps.setEnabled(True)
