#client socket
import sys

from PySide6.QtCore import QSize, Qt
from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton, QLabel

import socket
import time

import random
import json

import serial
import serial.tools.list_ports

from PySide6.QtCore import Signal, QThread


class ClientThread(QThread):

    def __init__(self):
        super().__init__()
        self._run_flag = True
        self.snd_msg = {'status': None, 'available_ports': None, 'msg_data': None}
        

    def run(self):
        while self._run_flag:
            try: # пробуем подключиться 
                # если все ок , то далее ... если нет то к <_икслючение № 1>

                client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                client.settimeout(5)
                client.connect(('localhost', 12345))
                self.snd_msg['status'] = "CONNECTEDTOSERVER"
                self.snd_msg['msg_data'] = [socket.gethostbyname(socket.gethostname())]
                data_to_resp = json.dumps(self.snd_msg).encode()
                try:
                    client.sendall(data_to_resp)
                except ConnectionResetError as e:
                    print(e)
                    break
                while True:
                    try:
                        raw_data = client.recv(1024).decode()
                        data = json.loads(raw_data)
                        print(data)
                    # когда не получен ответ
                    except ConnectionAbortedError as e:
                        print(e)
                    except ConnectionResetError as e:
                        print(e)
                        break
                    
                    if data['cmd'] == "TELEMETRY":
                        self.snd_msg['status'] = "RESPONSETOTELEMETRY"
                        self.snd_msg['msg_data'] = self._rand_data()

                    elif data['cmd'] == "SETPOINTS":
                        cpoints = len(data['msg_data']["features"])

                        (print(f"\nПолучено точек: {len(data['msg_data']['features'])}"))
                        for idx, el in enumerate(data['msg_data']["features"]):
                            print('\n')
                            print(idx)
                            print(el)
                        print('\n')
                        self.snd_msg['status'] = "POINTSDATARECEIVED"
                        self.snd_msg['msg_data'] = cpoints
                        # создал ошибку
                    else:
                        self.snd_msg['status'] = "UNKNOWNCMD"
                        self.snd_msg['msg_data'] = []


                    self.snd_msg['available_ports'] = self._avail_dev()

                    try:
                        data_to_resp = json.dumps(self.snd_msg).encode()
                        client.sendall(data_to_resp)
                    except ConnectionResetError as e:
                        print(e)
                        break
                    
                    QThread.sleep(1)

            # <_икслючение № 1>
            # когда не видит хост
            except ConnectionRefusedError as e:
                print('im here')
                print(e)

            except socket.timeout as e:
                print('prevysheno vremya ozhidanyay')
                print(e)
                pass


    def stop(self):
        self._run_flag = False
        self.wait()
    
        
    def _avail_dev(self):
        """
        Функция смотрит доступные последовательные порты в ОС
        """
        res = []
        ports = serial.tools.list_ports.comports()
        for port in ports:
            res.append(port.name)
        return res
    
    
    def _rand_data(pr=False):

        speed = str(float(random.randint(0, 20)) / 10.0)
        pitch = str(float(random.randint(-900, 900)) / 10.0)
        roll = str(float(random.randint(-900, 900)) / 10.0)
        yaw = str(float(random.randint(-900, 900)) / 10.0)

        if pr:
            print(f'Speed: {speed}')
            print(f'Pitch: {pitch}')
            print(f'Roll: {roll}')
            print(f'Yaw: {yaw}\n')
    
        return (speed, pitch, roll, yaw)


# Subclass QMainWindow to customize your application's main window
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Client")
        label = QLabel()
        label.setText('Client is activated')
        self.setCentralWidget(label)
        
        self.HOST = "localhost"
        self.PORT = 12345
        
        self.clientthread = ClientThread()
        self.clientthread.start()
        
        
    


app = QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec_()


