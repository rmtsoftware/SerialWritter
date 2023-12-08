from PySide6 import QtCore
from btnfunctionality import BtnsFunctionality
import logging


class ManualKeysCtrl(BtnsFunctionality):
    def __init__(self):
        super().__init__()
        
        # Ручное управление кнопками WASD
        self._manCS = 0
        self._w_flag = False
        self._a_flag = False
        self._s_flag = False
        self._d_flag = False
        self.msg_signals.get_man_perm.connect(self.actns_rcv_man_perm)
        self.msg_signals.mov_forw.connect(self.actns_press_w)
        self.msg_signals.mov_back.connect(self.actns_press_s)
        self.msg_signals.mov_left.connect(self.actns_press_a)
        self.msg_signals.mov_right.connect(self.actns_press_d)
        
    def write_manual(self, direction):
        cmd = f'D,s,3,{direction},{self.pwr_mnl},*\r\n'
        self.port.write(bytes(cmd, 'utf-8'))
        self._manCS = self.estimator.get_CS(cmd)
        
        self.current_text = f'[{self._cur_time()}] - [SEND] - {cmd}' + self.current_text
        self.ui.textBrowser.setText(self.current_text)
        
      
    @QtCore.Slot(object)
    def actns_rcv_man_perm(self, rcv_msg):
        try:
            _parsedCS = int(rcv_msg.split(',')[-1][1:-2])
 
        except Exception as e:
            print(e)

        if self._manCS != _parsedCS:
            print("Ошибка записи ручной команды")
            print(f"Получено: {rcv_msg}")
            return -1
        
        if self._manCS == _parsedCS:
            return 0
    
        
    def keyPressEvent(self, event):
        
        if self.port.isOpen() != True:
            return
        
        if self._fMan_mode == -1:
            return
        
        key_press = event.key()

        if key_press == QtCore.Qt.Key.Key_W:
            self.msg_signals.mov_forw.emit()
        if key_press == QtCore.Qt.Key.Key_S:
            self.msg_signals.mov_back.emit()
        if key_press == QtCore.Qt.Key.Key_A:
            self.msg_signals.mov_left.emit()
        if key_press == QtCore.Qt.Key.Key_D:
            self.msg_signals.mov_right.emit()
            
    
    def actns_press_w(self):

        def _reset_flag():
            self._w_flag = False

        if self._w_flag == True:
            return
        self._w_flag = True
        self.write_manual('F') # Forward
        print('Forward')
        QtCore.QTimer.singleShot(500, _reset_flag)


    def actns_press_s(self):

        def _reset_flag():
            self._s_flag = False

        if self._s_flag == True:
            return
        self._s_flag = True
        self.write_manual('B') # Back
        print('Back')
        QtCore.QTimer.singleShot(500, _reset_flag)


    def actns_press_a(self):

        def _reset_flag():
            self._a_flag = False

        if self._a_flag == True:
            return
        self._a_flag = True
        self.write_manual('L') # Left
        print('Left')
        QtCore.QTimer.singleShot(500, _reset_flag)


    def actns_press_d(self):

        def _reset_flag():
            self._d_flag = False

        if self._d_flag == True:
            return
        self._d_flag = True 
        self.write_manual('R') # Right
        print('Right')
        QtCore.QTimer.singleShot(500, _reset_flag)
        