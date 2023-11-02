from connector import SerialConnector
import serial
import serial.tools.list_ports


class ComboBoxProcesser(SerialConnector):
    def __init__(self):
        super().__init__()


    def _cb_proc(self, in_cbox, actual):
        """

        COMBO BOX PROCCESING\n

        Функция формирует три списка:\n
            1. актуальный (требуемый) список портов\n
            2. порты которые следует удалить из комбобокса\n
            3. порты которые следует добавить в комбобокс\n

        """
        common = [x for x in in_cbox if x in actual]
        to_delete = list(set(in_cbox).difference(set(common)))
        to_add = list(set(actual).difference(set(common)))
        return common, to_delete, to_add
    

    def _avail_dev(self):
        """
        Функция смотрит доступные последовательные порты в ОС
        """
        res = []
        ports = serial.tools.list_ports.comports()
        for port in ports:
            res.append(port.name)
        return res
    

    def _add_item_to_cb(self):
        """
        Функция добавления и удаления портов в комбобокс выбора портов
        """
        avail_ports = self._avail_dev()
        common, to_del, to_add = self._cb_proc(self.item_in_cb, avail_ports)

        # Проверка есть ли выбранный com-порт
        # в списке доступных com-портов
        if self.current_com is not None:
            if not self.current_com in common:
                self.disconnect_from_ser_dev()

        for el in to_del:
            index = self.ui.cb_com_dev.findText(el)
            self.ui.cb_com_dev.removeItem(index)
        self.ui.cb_com_dev.addItems(to_add)
        self.item_in_cb = common
        self.item_in_cb += to_add