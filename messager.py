from PySide6 import QtWidgets

class Messager():

    @staticmethod
    def _dev_connected(port):
        """ Вызов информацинного сообщения о успешном подключении к устройству """
        QtWidgets.QMessageBox.information(None, "Успешно", 
                                     f"Подключено устройство {port}",
                                      QtWidgets.QMessageBox.StandardButton.Ok)
    @staticmethod
    def _dev_disconnect(port):
        """ Вызов информацинного сообщения о успешном отключении от устройства """
        QtWidgets.QMessageBox.information(None, "Успешно", 
                                     f"Отключено устройство {port}",
                                      QtWidgets.QMessageBox.StandardButton.Ok)
        
    @staticmethod
    def _indefinite_dev(dev):
        """ Вызов сообщения ошибки -> устройство по заданному com-порту не доступно """
        QtWidgets.QMessageBox.critical(None, "Ошибка", 
                                     f"Устроство {dev} не доступно",
                                      QtWidgets.QMessageBox.StandardButton.Ok)
    
    @staticmethod
    def _not_selected_dev():
        """ Вызов сообщения ошибки -> устройство по заданному com-порту не доступно """
        QtWidgets.QMessageBox.warning(None, "Предупреждение", 
                                     f"Изделие не выбрано",
                                      QtWidgets.QMessageBox.StandardButton.Ok)
        

    @staticmethod
    def _gps_check_sum_error():
        """ Вызов сообщения ошибки -> Ошибка контрольной суммы при получении строки GPS """
        QtWidgets.QMessageBox.warning(None, "Предупреждение", 
                                     f"Ошибка контрольной суммы GPS",
                                      QtWidgets.QMessageBox.StandardButton.Ok)
        
    @staticmethod
    def _imu_check_sum_error():
        """ Вызов сообщения ошибки -> Ошибка контрольной суммы при получении строки IMU """
        QtWidgets.QMessageBox.warning(None, "Предупреждение", 
                                     f"Ошибка контрольной суммы IMU",
                                      QtWidgets.QMessageBox.StandardButton.Ok)
        
    
    @staticmethod
    def _invalid_input():
        """ Вызов сообщения ошибки -> Введены недопустимые символы"""
        QtWidgets.QMessageBox.warning(None, "Ошибка ввода", 
                                     f"Введите число от 0 до 100",
                                      QtWidgets.QMessageBox.StandardButton.Ok)