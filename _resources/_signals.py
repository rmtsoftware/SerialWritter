from PySide6.QtCore import Signal, QObject

class _nSignals(QObject):
    get_gps = Signal(object)
    get_imu = Signal(object)
    get_man_perm = Signal(object)
    mov_forw = Signal()
    mov_back = Signal()
    mov_left = Signal()
    mov_right = Signal()
    set_gps_data_to_widget = Signal(object)
    set_imu_data_to_widget = Signal(object)
    data_send = Signal(object)