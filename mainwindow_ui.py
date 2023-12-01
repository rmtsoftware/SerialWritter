# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainwindow.ui'
##
## Created by: Qt User Interface Compiler version 6.6.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QComboBox, QFrame, QHBoxLayout,
    QLabel, QLineEdit, QMainWindow, QPushButton,
    QSizePolicy, QStatusBar, QTextBrowser, QVBoxLayout,
    QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1432, 695)
        MainWindow.setStyleSheet(u"background-color: qlineargradient(spread:pad, x1:0.506, y1:0, x2:0.494591, y2:1, stop:0 rgba(0, 0, 0, 255), stop:1 rgba(31, 56, 71, 255))")
        MainWindow.setAnimated(True)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.main_frame = QFrame(self.centralwidget)
        self.main_frame.setObjectName(u"main_frame")
        self.main_frame.setGeometry(QRect(10, 490, 331, 71))
        self.main_frame.setStyleSheet(u"border: 2px solid rgb(187, 195, 211);\n"
"border-radius: 5px;\n"
"background-color: none;")
        self.verticalLayout_3 = QVBoxLayout(self.main_frame)
        self.verticalLayout_3.setSpacing(1)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(-1, 0, -1, 0)
        self.pwr_frame = QFrame(self.main_frame)
        self.pwr_frame.setObjectName(u"pwr_frame")
        self.pwr_frame.setStyleSheet(u"border: none;")
        self.verticalLayout_6 = QVBoxLayout(self.pwr_frame)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.lb_pwr_mnl = QLabel(self.pwr_frame)
        self.lb_pwr_mnl.setObjectName(u"lb_pwr_mnl")
        self.lb_pwr_mnl.setMaximumSize(QSize(16777215, 20))
        self.lb_pwr_mnl.setStyleSheet(u"border: none;\n"
"font: bold;\n"
"color: rgb(187, 195, 211);\n"
"font-size: 12pt;")
        self.lb_pwr_mnl.setInputMethodHints(Qt.ImhHiddenText|Qt.ImhUrlCharactersOnly)
        self.lb_pwr_mnl.setAlignment(Qt.AlignCenter)

        self.verticalLayout_6.addWidget(self.lb_pwr_mnl)

        self.le_pwr_mnl = QLineEdit(self.pwr_frame)
        self.le_pwr_mnl.setObjectName(u"le_pwr_mnl")
        self.le_pwr_mnl.setMinimumSize(QSize(0, 25))
        self.le_pwr_mnl.setMaximumSize(QSize(16777215, 16777215))
        self.le_pwr_mnl.setStyleSheet(u"QLineEdit{\n"
"	color: black;\n"
"	font-size: 10pt;\n"
"	background-color: rgb(211, 211, 211);\n"
"	border: 1px solid rgb(118, 118, 118);\n"
"	border-radius: 3px;\n"
"	font: bold;\n"
"}\n"
"QLineEdit:hover {\n"
"	border: 1px solid rgb(79, 175, 227);\n"
"	border-radius: 3px;\n"
"	background-color: rgb(187, 195, 211);\n"
"}")

        self.verticalLayout_6.addWidget(self.le_pwr_mnl)


        self.verticalLayout_3.addWidget(self.pwr_frame)

        self.text_frame = QFrame(self.centralwidget)
        self.text_frame.setObjectName(u"text_frame")
        self.text_frame.setGeometry(QRect(350, 10, 711, 661))
        self.text_frame.setStyleSheet(u"border: 2px solid rgb(187, 195, 211);\n"
"border-radius: 5px;\n"
"background-color: none;")
        self.verticalLayout_4 = QVBoxLayout(self.text_frame)
        self.verticalLayout_4.setSpacing(3)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(-1, 5, -1, 5)
        self.terminal_header = QFrame(self.text_frame)
        self.terminal_header.setObjectName(u"terminal_header")
        self.terminal_header.setStyleSheet(u"border: none;\n"
"border-radius: none;\n"
"background-color: none;")
        self.horizontalLayout_2 = QHBoxLayout(self.terminal_header)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label_2 = QLabel(self.terminal_header)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setMaximumSize(QSize(16777215, 20))
        self.label_2.setStyleSheet(u"font-size: 12pt;\n"
"border: none;\n"
"font: bold;\n"
"color: rgb(187, 195, 211);")
        self.label_2.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_2.addWidget(self.label_2)

        self.indicator_link = QLabel(self.terminal_header)
        self.indicator_link.setObjectName(u"indicator_link")
        self.indicator_link.setStyleSheet(u"background-color: rgba(255,255,255,0);")
        self.indicator_link.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_2.addWidget(self.indicator_link)

        self.indicator_crc = QLabel(self.terminal_header)
        self.indicator_crc.setObjectName(u"indicator_crc")
        self.indicator_crc.setStyleSheet(u"background-color: rgba(255,255,255,0);")
        self.indicator_crc.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_2.addWidget(self.indicator_crc)


        self.verticalLayout_4.addWidget(self.terminal_header)

        self.textBrowser = QTextBrowser(self.text_frame)
        self.textBrowser.setObjectName(u"textBrowser")
        font = QFont()
        font.setFamilies([u"Segoe UI"])
        font.setPointSize(10)
        font.setBold(True)
        font.setItalic(False)
        font.setKerning(True)
        self.textBrowser.setFont(font)
        self.textBrowser.setStyleSheet(u"QTextBrowser{\n"
"	color: black;\n"
"	font-size: 10pt;\n"
"	background-color: rgb(211, 211, 211);\n"
"	border: 1px solid rgb(118, 118, 118);\n"
"	border-radius: 3px;\n"
"	font: bold;\n"
"}")

        self.verticalLayout_4.addWidget(self.textBrowser)

        self.btn_clean_textBrw = QPushButton(self.text_frame)
        self.btn_clean_textBrw.setObjectName(u"btn_clean_textBrw")
        self.btn_clean_textBrw.setMinimumSize(QSize(0, 25))
        self.btn_clean_textBrw.setStyleSheet(u"QPushButton{\n"
"	color: black;\n"
"	font-size: 10pt;\n"
"	background-color: rgb(211, 211, 211);\n"
"	border: 1px solid rgb(118, 118, 118);\n"
"	border-radius: 3px;\n"
"	font: bold;\n"
"}\n"
"QPushButton:hover {\n"
"	border: 1px solid rgb(79, 175, 227);\n"
"	border-radius: 3px;\n"
"	background-color: rgb(187, 195, 211);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"	background-color:rgba(79, 175, 227,70);\n"
"	border: 1px solid rgb(79, 175, 227);\n"
"	border-radius: 3px;\n"
"	color: rgb(0,122,217);\n"
"}")

        self.verticalLayout_4.addWidget(self.btn_clean_textBrw)

        self.req_frame = QFrame(self.centralwidget)
        self.req_frame.setObjectName(u"req_frame")
        self.req_frame.setGeometry(QRect(10, 130, 331, 111))
        self.req_frame.setStyleSheet(u"border: 2px solid rgb(187, 195, 211);\n"
"border-radius: 5px;\n"
"background-color: none;")
        self.horizontalLayout_4 = QHBoxLayout(self.req_frame)
        self.horizontalLayout_4.setSpacing(1)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(-1, 0, -1, -1)
        self.btn_req_frame = QFrame(self.req_frame)
        self.btn_req_frame.setObjectName(u"btn_req_frame")
        self.btn_req_frame.setStyleSheet(u"border: none;")
        self.verticalLayout_2 = QVBoxLayout(self.btn_req_frame)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(-1, 0, -1, 0)
        self.lb_request = QLabel(self.btn_req_frame)
        self.lb_request.setObjectName(u"lb_request")
        self.lb_request.setMinimumSize(QSize(0, 20))
        self.lb_request.setMaximumSize(QSize(16777215, 20))
        self.lb_request.setStyleSheet(u"font-size: 12pt;\n"
"border: none;\n"
"font: bold;\n"
"color: rgb(187, 195, 211);")
        self.lb_request.setAlignment(Qt.AlignCenter)

        self.verticalLayout_2.addWidget(self.lb_request)

        self.btn_gps = QPushButton(self.btn_req_frame)
        self.btn_gps.setObjectName(u"btn_gps")
        self.btn_gps.setMinimumSize(QSize(0, 25))
        self.btn_gps.setStyleSheet(u"QPushButton{\n"
"	color: black;\n"
"	font-size: 10pt;\n"
"	background-color: rgb(211, 211, 211);\n"
"	border: 1px solid rgb(118, 118, 118);\n"
"	border-radius: 3px;\n"
"	font: bold;\n"
"}\n"
"QPushButton:hover {\n"
"	border: 1px solid rgb(79, 175, 227);\n"
"	border-radius: 3px;\n"
"	background-color: rgb(187, 195, 211);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"	background-color:rgba(79, 175, 227,70);\n"
"	border: 1px solid rgb(79, 175, 227);\n"
"	border-radius: 3px;\n"
"	color: rgb(0,122,217);\n"
"}\n"
"\n"
"QPushButton:disabled {\n"
"	background-color: rgb(113, 113, 113);\n"
"}")

        self.verticalLayout_2.addWidget(self.btn_gps)

        self.btn_imu = QPushButton(self.btn_req_frame)
        self.btn_imu.setObjectName(u"btn_imu")
        self.btn_imu.setMinimumSize(QSize(0, 25))
        self.btn_imu.setStyleSheet(u"QPushButton{\n"
"	color: black;\n"
"	font-size: 10pt;\n"
"	background-color: rgb(211, 211, 211);\n"
"	border: 1px solid rgb(118, 118, 118);\n"
"	border-radius: 3px;\n"
"	font: bold;\n"
"}\n"
"QPushButton:hover {\n"
"	border: 1px solid rgb(79, 175, 227);\n"
"	border-radius: 3px;\n"
"	background-color: rgb(187, 195, 211);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"	background-color:rgba(79, 175, 227,70);\n"
"	border: 1px solid rgb(79, 175, 227);\n"
"	border-radius: 3px;\n"
"	color: rgb(0,122,217);\n"
"}\n"
"QPushButton:disabled {\n"
"	background-color: rgb(113, 113, 113);\n"
"}")

        self.verticalLayout_2.addWidget(self.btn_imu)


        self.horizontalLayout_4.addWidget(self.btn_req_frame)

        self.mode_frame = QFrame(self.centralwidget)
        self.mode_frame.setObjectName(u"mode_frame")
        self.mode_frame.setGeometry(QRect(10, 250, 331, 151))
        self.mode_frame.setStyleSheet(u"border: 2px solid rgb(187, 195, 211);\n"
"border-radius: 5px;\n"
"background-color: none;")
        self.horizontalLayout = QHBoxLayout(self.mode_frame)
        self.horizontalLayout.setSpacing(1)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(-1, 0, -1, 0)
        self.btn_mode_frame = QFrame(self.mode_frame)
        self.btn_mode_frame.setObjectName(u"btn_mode_frame")
        self.btn_mode_frame.setStyleSheet(u"border: none;")
        self.verticalLayout = QVBoxLayout(self.btn_mode_frame)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(-1, 0, -1, 0)
        self.lb_mode = QLabel(self.btn_mode_frame)
        self.lb_mode.setObjectName(u"lb_mode")
        self.lb_mode.setMaximumSize(QSize(16777215, 20))
        self.lb_mode.setStyleSheet(u"border: none;\n"
"font: bold;\n"
"color: rgb(187, 195, 211);font-size: 12pt;")
        self.lb_mode.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.lb_mode)

        self.btn_mnl_mode = QPushButton(self.btn_mode_frame)
        self.btn_mnl_mode.setObjectName(u"btn_mnl_mode")
        self.btn_mnl_mode.setMinimumSize(QSize(0, 25))
        self.btn_mnl_mode.setStyleSheet(u"QPushButton{\n"
"	color: black;\n"
"	font-size: 10pt;\n"
"	background-color: rgb(211, 211, 211);\n"
"	border: 1px solid rgb(118, 118, 118);\n"
"	border-radius: 3px;\n"
"	font: bold;\n"
"}\n"
"QPushButton:hover {\n"
"	border: 1px solid rgb(79, 175, 227);\n"
"	border-radius: 3px;\n"
"	background-color: rgb(187, 195, 211);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"	background-color:rgba(79, 175, 227,70);\n"
"	border: 1px solid rgb(79, 175, 227);\n"
"	border-radius: 3px;\n"
"	color: rgb(0,122,217);\n"
"}\n"
"\n"
"QPushButton:disabled {\n"
"	background-color: rgb(113, 113, 113);\n"
"}")

        self.verticalLayout.addWidget(self.btn_mnl_mode)

        self.btn_auto_mode = QPushButton(self.btn_mode_frame)
        self.btn_auto_mode.setObjectName(u"btn_auto_mode")
        self.btn_auto_mode.setMinimumSize(QSize(0, 25))
        self.btn_auto_mode.setStyleSheet(u"QPushButton{\n"
"	color: black;\n"
"	font-size: 10pt;\n"
"	background-color: rgb(211, 211, 211);\n"
"	border: 1px solid rgb(118, 118, 118);\n"
"	border-radius: 3px;\n"
"	font: bold;\n"
"}\n"
"QPushButton:hover {\n"
"	border: 1px solid rgb(79, 175, 227);\n"
"	border-radius: 3px;\n"
"	background-color: rgb(187, 195, 211);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"	background-color:rgba(79, 175, 227,70);\n"
"	border: 1px solid rgb(79, 175, 227);\n"
"	border-radius: 3px;\n"
"	color: rgb(0,122,217);\n"
"}\n"
"\n"
"QPushButton:disabled {\n"
"	background-color: rgb(113, 113, 113);\n"
"}")

        self.verticalLayout.addWidget(self.btn_auto_mode)

        self.btn_rmt_mode = QPushButton(self.btn_mode_frame)
        self.btn_rmt_mode.setObjectName(u"btn_rmt_mode")
        self.btn_rmt_mode.setMinimumSize(QSize(0, 25))
        self.btn_rmt_mode.setStyleSheet(u"QPushButton{\n"
"	color: black;\n"
"	font-size: 10pt;\n"
"	background-color: rgb(211, 211, 211);\n"
"	border: 1px solid rgb(118, 118, 118);\n"
"	border-radius: 3px;\n"
"	font: bold;\n"
"}\n"
"QPushButton:hover {\n"
"	border: 1px solid rgb(79, 175, 227);\n"
"	border-radius: 3px;\n"
"	background-color: rgb(187, 195, 211);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"	background-color:rgba(79, 175, 227,70);\n"
"	border: 1px solid rgb(79, 175, 227);\n"
"	border-radius: 3px;\n"
"	color: rgb(0,122,217);\n"
"}\n"
"\n"
"QPushButton:disabled {\n"
"	background-color: rgb(113, 113, 113);\n"
"}")

        self.verticalLayout.addWidget(self.btn_rmt_mode)


        self.horizontalLayout.addWidget(self.btn_mode_frame)

        self.mtr_ctrl_frame = QFrame(self.centralwidget)
        self.mtr_ctrl_frame.setObjectName(u"mtr_ctrl_frame")
        self.mtr_ctrl_frame.setGeometry(QRect(10, 410, 331, 71))
        self.mtr_ctrl_frame.setStyleSheet(u"border: 2px solid rgb(187, 195, 211);\n"
"border-radius: 5px;\n"
"background-color: none;")
        self.horizontalLayout_3 = QHBoxLayout(self.mtr_ctrl_frame)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.btn_mode_frame_2 = QFrame(self.mtr_ctrl_frame)
        self.btn_mode_frame_2.setObjectName(u"btn_mode_frame_2")
        self.btn_mode_frame_2.setStyleSheet(u"border: none;")
        self.verticalLayout_7 = QVBoxLayout(self.btn_mode_frame_2)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalLayout_7.setContentsMargins(-1, 0, -1, 0)
        self.lb_mode_2 = QLabel(self.btn_mode_frame_2)
        self.lb_mode_2.setObjectName(u"lb_mode_2")
        self.lb_mode_2.setMaximumSize(QSize(16777215, 20))
        self.lb_mode_2.setStyleSheet(u"border: none;\n"
"font: bold;\n"
"color: rgb(187, 195, 211);font-size: 12pt;")
        self.lb_mode_2.setAlignment(Qt.AlignCenter)

        self.verticalLayout_7.addWidget(self.lb_mode_2)

        self.btn_ctrl_mtr = QPushButton(self.btn_mode_frame_2)
        self.btn_ctrl_mtr.setObjectName(u"btn_ctrl_mtr")
        self.btn_ctrl_mtr.setMinimumSize(QSize(0, 25))
        self.btn_ctrl_mtr.setStyleSheet(u"QPushButton{\n"
"	color: black;\n"
"	font-size: 10pt;\n"
"	background-color: rgb(211, 211, 211);\n"
"	border: 1px solid rgb(118, 118, 118);\n"
"	border-radius: 3px;\n"
"	font: bold;\n"
"}\n"
"QPushButton:hover {\n"
"	border: 1px solid rgb(79, 175, 227);\n"
"	border-radius: 3px;\n"
"	background-color: rgb(187, 195, 211);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"	background-color:rgba(79, 175, 227,70);\n"
"	border: 1px solid rgb(79, 175, 227);\n"
"	border-radius: 3px;\n"
"	color: rgb(0,122,217);\n"
"}\n"
"\n"
"QPushButton:disabled {\n"
"	background-color: rgb(113, 113, 113);\n"
"}")

        self.verticalLayout_7.addWidget(self.btn_ctrl_mtr)


        self.horizontalLayout_3.addWidget(self.btn_mode_frame_2)

        self.main_conn_frame = QFrame(self.centralwidget)
        self.main_conn_frame.setObjectName(u"main_conn_frame")
        self.main_conn_frame.setGeometry(QRect(10, 10, 331, 111))
        self.main_conn_frame.setStyleSheet(u"border: 2px solid rgb(187, 195, 211);\n"
"border-radius: 5px;\n"
"background-color: none;")
        self.verticalLayout_5 = QVBoxLayout(self.main_conn_frame)
        self.verticalLayout_5.setSpacing(1)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.lb_main_connection = QLabel(self.main_conn_frame)
        self.lb_main_connection.setObjectName(u"lb_main_connection")
        self.lb_main_connection.setMaximumSize(QSize(16777215, 20))
        self.lb_main_connection.setStyleSheet(u"font-size: 12pt;\n"
"border: none;\n"
"font: bold;\n"
"color: rgb(187, 195, 211);")
        self.lb_main_connection.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.verticalLayout_5.addWidget(self.lb_main_connection)

        self.select_params_com_frame = QFrame(self.main_conn_frame)
        self.select_params_com_frame.setObjectName(u"select_params_com_frame")
        self.select_params_com_frame.setMaximumSize(QSize(16777215, 40))
        self.select_params_com_frame.setStyleSheet(u"border: none;")
        self.horizontalLayout_5 = QHBoxLayout(self.select_params_com_frame)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.cb_com_dev = QComboBox(self.select_params_com_frame)
        self.cb_com_dev.setObjectName(u"cb_com_dev")
        self.cb_com_dev.setMinimumSize(QSize(0, 25))
        self.cb_com_dev.setLayoutDirection(Qt.LeftToRight)
        self.cb_com_dev.setStyleSheet(u"QComboBox{\n"
"	color: black;\n"
"	font-size: 10pt;\n"
"	background-color: rgb(211, 211, 211);\n"
"	border: 1px solid rgb(118, 118, 118);\n"
"	border-radius: 3px;\n"
"	font: bold;\n"
"}\n"
"QComboBox:hover {\n"
"	border: 1px solid rgb(79, 175, 227);\n"
"	border-radius: 3px;\n"
"	background-color: rgb(187, 195, 211);\n"
"}")

        self.horizontalLayout_5.addWidget(self.cb_com_dev)

        self.cb_baudrate = QComboBox(self.select_params_com_frame)
        self.cb_baudrate.addItem("")
        self.cb_baudrate.addItem("")
        self.cb_baudrate.setObjectName(u"cb_baudrate")
        self.cb_baudrate.setMinimumSize(QSize(0, 25))
        self.cb_baudrate.setStyleSheet(u"QComboBox{\n"
"	color: black;\n"
"	font-size: 10pt;\n"
"	background-color: rgb(211, 211, 211);\n"
"	border: 1px solid rgb(118, 118, 118);\n"
"	border-radius: 3px;\n"
"	font: bold;\n"
"}\n"
"QComboBox:hover {\n"
"	border: 1px solid rgb(79, 175, 227);\n"
"	border-radius: 3px;\n"
"	background-color: rgb(187, 195, 211);\n"
"}\n"
"\n"
"QComboBox:pressed {\n"
"	background-color:rgba(79, 175, 227,70);\n"
"	border: 1px solid rgb(79, 175, 227);\n"
"	border-radius: 3px;\n"
"	color: rgb(0,122,217);\n"
"}")

        self.horizontalLayout_5.addWidget(self.cb_baudrate)


        self.verticalLayout_5.addWidget(self.select_params_com_frame)

        self.conn_frame_2 = QFrame(self.main_conn_frame)
        self.conn_frame_2.setObjectName(u"conn_frame_2")
        self.conn_frame_2.setMaximumSize(QSize(16777215, 40))
        self.conn_frame_2.setStyleSheet(u"border: none;")
        self.conn_frame = QHBoxLayout(self.conn_frame_2)
        self.conn_frame.setObjectName(u"conn_frame")
        self.btn_disconnect = QPushButton(self.conn_frame_2)
        self.btn_disconnect.setObjectName(u"btn_disconnect")
        self.btn_disconnect.setMinimumSize(QSize(0, 25))
        self.btn_disconnect.setStyleSheet(u"QPushButton{\n"
"	color: black;\n"
"	font-size: 10pt;\n"
"	background-color: rgb(211, 211, 211);\n"
"	border: 1px solid rgb(118, 118, 118);\n"
"	border-radius: 3px;\n"
"	font: bold;\n"
"}\n"
"QPushButton:hover {\n"
"	border: 1px solid rgb(79, 175, 227);\n"
"	border-radius: 3px;\n"
"	background-color: rgb(187, 195, 211);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"	background-color:rgba(79, 175, 227,70);\n"
"	border: 1px solid rgb(79, 175, 227);\n"
"	border-radius: 3px;\n"
"	color: rgb(0,122,217);\n"
"}\n"
"\n"
"QPushButton:disabled {\n"
"	background-color: rgb(113, 113, 113);\n"
"}")

        self.conn_frame.addWidget(self.btn_disconnect)

        self.btn_connect = QPushButton(self.conn_frame_2)
        self.btn_connect.setObjectName(u"btn_connect")
        self.btn_connect.setMinimumSize(QSize(0, 25))
        self.btn_connect.setStyleSheet(u"QPushButton{\n"
"	color: black;\n"
"	font-size: 10pt;\n"
"	background-color: rgb(211, 211, 211);\n"
"	border: 1px solid rgb(118, 118, 118);\n"
"	border-radius: 3px;\n"
"	font: bold;\n"
"}\n"
"QPushButton:hover {\n"
"	border: 1px solid rgb(79, 175, 227);\n"
"	border-radius: 3px;\n"
"	background-color: rgb(187, 195, 211);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"	background-color:rgba(79, 175, 227,70);\n"
"	border: 1px solid rgb(79, 175, 227);\n"
"	border-radius: 3px;\n"
"	color: rgb(0,122,217);\n"
"}\n"
"\n"
"QPushButton:disabled {\n"
"	background-color: rgb(113, 113, 113);\n"
"}")

        self.conn_frame.addWidget(self.btn_connect)


        self.verticalLayout_5.addWidget(self.conn_frame_2)

        self.main_mnl_frame = QFrame(self.centralwidget)
        self.main_mnl_frame.setObjectName(u"main_mnl_frame")
        self.main_mnl_frame.setGeometry(QRect(10, 570, 331, 101))
        self.main_mnl_frame.setStyleSheet(u"border: 2px solid rgb(187, 195, 211);\n"
"border-radius: 5px;\n"
"background-color: none;")
        self.verticalLayout_9 = QVBoxLayout(self.main_mnl_frame)
        self.verticalLayout_9.setSpacing(1)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.verticalLayout_9.setContentsMargins(-1, 0, -1, 0)
        self.frame = QFrame(self.main_mnl_frame)
        self.frame.setObjectName(u"frame")
        self.frame.setStyleSheet(u"border:none;")
        self.verticalLayout_8 = QVBoxLayout(self.frame)
        self.verticalLayout_8.setSpacing(1)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.verticalLayout_8.setContentsMargins(-1, 0, -1, 0)
        self.lb_mnl_cmd = QLabel(self.frame)
        self.lb_mnl_cmd.setObjectName(u"lb_mnl_cmd")
        self.lb_mnl_cmd.setMaximumSize(QSize(16777215, 20))
        self.lb_mnl_cmd.setStyleSheet(u"border: none;\n"
"font: bold;\n"
"color: rgb(187, 195, 211);font-size: 12pt;")
        self.lb_mnl_cmd.setAlignment(Qt.AlignCenter)

        self.verticalLayout_8.addWidget(self.lb_mnl_cmd)

        self.le_mnl_cmd = QLineEdit(self.frame)
        self.le_mnl_cmd.setObjectName(u"le_mnl_cmd")
        self.le_mnl_cmd.setMinimumSize(QSize(0, 25))
        self.le_mnl_cmd.setMaximumSize(QSize(16777215, 16777215))
        self.le_mnl_cmd.setStyleSheet(u"QLineEdit{\n"
"	color: black;\n"
"	font-size: 10pt;\n"
"	background-color: rgb(211, 211, 211);\n"
"	border: 1px solid rgb(118, 118, 118);\n"
"	border-radius: 3px;\n"
"	font: bold;\n"
"}\n"
"QLineEdit:hover {\n"
"	border: 1px solid rgb(79, 175, 227);\n"
"	border-radius: 3px;\n"
"	background-color: rgb(187, 195, 211);\n"
"}")

        self.verticalLayout_8.addWidget(self.le_mnl_cmd)

        self.btn_mnl_cmd = QPushButton(self.frame)
        self.btn_mnl_cmd.setObjectName(u"btn_mnl_cmd")
        self.btn_mnl_cmd.setMinimumSize(QSize(0, 25))
        self.btn_mnl_cmd.setStyleSheet(u"QPushButton{\n"
"	color: black;\n"
"	font-size: 10pt;\n"
"	background-color: rgb(211, 211, 211);\n"
"	border: 1px solid rgb(118, 118, 118);\n"
"	border-radius: 3px;\n"
"	font: bold;\n"
"}\n"
"QPushButton:hover {\n"
"	border: 1px solid rgb(79, 175, 227);\n"
"	border-radius: 3px;\n"
"	background-color: rgb(187, 195, 211);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"	background-color:rgba(79, 175, 227,70);\n"
"	border: 1px solid rgb(79, 175, 227);\n"
"	border-radius: 3px;\n"
"	color: rgb(0,122,217);\n"
"}\n"
"\n"
"QPushButton:disabled {\n"
"	background-color: rgb(113, 113, 113);\n"
"}")

        self.verticalLayout_8.addWidget(self.btn_mnl_cmd)


        self.verticalLayout_9.addWidget(self.frame)

        self.frame_main_gps_data = QFrame(self.centralwidget)
        self.frame_main_gps_data.setObjectName(u"frame_main_gps_data")
        self.frame_main_gps_data.setGeometry(QRect(1070, 10, 171, 391))
        self.frame_main_gps_data.setStyleSheet(u"border: 2px solid rgb(187, 195, 211);\n"
"border-radius: 5px;\n"
"background-color: none;")
        self.verticalLayout_11 = QVBoxLayout(self.frame_main_gps_data)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.lb_title_gps_data = QLabel(self.frame_main_gps_data)
        self.lb_title_gps_data.setObjectName(u"lb_title_gps_data")
        self.lb_title_gps_data.setMaximumSize(QSize(16777215, 20))
        self.lb_title_gps_data.setStyleSheet(u"font-size: 12pt;\n"
"border: none;\n"
"font: bold;\n"
"color: rgb(187, 195, 211);")
        self.lb_title_gps_data.setAlignment(Qt.AlignCenter)

        self.verticalLayout_11.addWidget(self.lb_title_gps_data)

        self.frame_gps_data = QFrame(self.frame_main_gps_data)
        self.frame_gps_data.setObjectName(u"frame_gps_data")
        self.frame_gps_data.setStyleSheet(u"border: none;")
        self.verticalLayout_10 = QVBoxLayout(self.frame_gps_data)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.frame_latitude = QFrame(self.frame_gps_data)
        self.frame_latitude.setObjectName(u"frame_latitude")
        self.horizontalLayout_6 = QHBoxLayout(self.frame_latitude)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.lb_latitude = QLabel(self.frame_latitude)
        self.lb_latitude.setObjectName(u"lb_latitude")
        self.lb_latitude.setStyleSheet(u"font-size: 10pt;\n"
"border: none;\n"
"color: rgb(187, 195, 211);")

        self.horizontalLayout_6.addWidget(self.lb_latitude)

        self.lb_latitude_val = QLabel(self.frame_latitude)
        self.lb_latitude_val.setObjectName(u"lb_latitude_val")
        self.lb_latitude_val.setStyleSheet(u"font-size: 10pt;\n"
"border: none;\n"
"color: rgb(187, 195, 211);")

        self.horizontalLayout_6.addWidget(self.lb_latitude_val)


        self.verticalLayout_10.addWidget(self.frame_latitude)

        self.frame_NS = QFrame(self.frame_gps_data)
        self.frame_NS.setObjectName(u"frame_NS")
        self.horizontalLayout_7 = QHBoxLayout(self.frame_NS)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.lb_NS = QLabel(self.frame_NS)
        self.lb_NS.setObjectName(u"lb_NS")
        self.lb_NS.setStyleSheet(u"font-size: 10pt;\n"
"border: none;\n"
"color: rgb(187, 195, 211);")

        self.horizontalLayout_7.addWidget(self.lb_NS)

        self.lb_NS_val = QLabel(self.frame_NS)
        self.lb_NS_val.setObjectName(u"lb_NS_val")
        self.lb_NS_val.setStyleSheet(u"font-size: 10pt;\n"
"border: none;\n"
"color: rgb(187, 195, 211);")

        self.horizontalLayout_7.addWidget(self.lb_NS_val)


        self.verticalLayout_10.addWidget(self.frame_NS)

        self.frame_longitude = QFrame(self.frame_gps_data)
        self.frame_longitude.setObjectName(u"frame_longitude")
        self.horizontalLayout_8 = QHBoxLayout(self.frame_longitude)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.lb_longitude = QLabel(self.frame_longitude)
        self.lb_longitude.setObjectName(u"lb_longitude")
        self.lb_longitude.setStyleSheet(u"font-size: 10pt;\n"
"border: none;\n"
"color: rgb(187, 195, 211);")

        self.horizontalLayout_8.addWidget(self.lb_longitude)

        self.lb_longitude_val = QLabel(self.frame_longitude)
        self.lb_longitude_val.setObjectName(u"lb_longitude_val")
        self.lb_longitude_val.setStyleSheet(u"font-size: 10pt;\n"
"border: none;\n"
"color: rgb(187, 195, 211);")

        self.horizontalLayout_8.addWidget(self.lb_longitude_val)


        self.verticalLayout_10.addWidget(self.frame_longitude)

        self.frame_EW = QFrame(self.frame_gps_data)
        self.frame_EW.setObjectName(u"frame_EW")
        self.horizontalLayout_9 = QHBoxLayout(self.frame_EW)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.lb_EW = QLabel(self.frame_EW)
        self.lb_EW.setObjectName(u"lb_EW")
        self.lb_EW.setStyleSheet(u"font-size: 10pt;\n"
"border: none;\n"
"color: rgb(187, 195, 211);")

        self.horizontalLayout_9.addWidget(self.lb_EW)

        self.lb_EW_val = QLabel(self.frame_EW)
        self.lb_EW_val.setObjectName(u"lb_EW_val")
        self.lb_EW_val.setStyleSheet(u"font-size: 10pt;\n"
"border: none;\n"
"color: rgb(187, 195, 211);")

        self.horizontalLayout_9.addWidget(self.lb_EW_val)


        self.verticalLayout_10.addWidget(self.frame_EW)

        self.frame_altitude = QFrame(self.frame_gps_data)
        self.frame_altitude.setObjectName(u"frame_altitude")
        self.horizontalLayout_10 = QHBoxLayout(self.frame_altitude)
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.lb_altitude = QLabel(self.frame_altitude)
        self.lb_altitude.setObjectName(u"lb_altitude")
        self.lb_altitude.setStyleSheet(u"font-size: 10pt;\n"
"border: none;\n"
"color: rgb(187, 195, 211);")

        self.horizontalLayout_10.addWidget(self.lb_altitude)

        self.lb_altitude_val = QLabel(self.frame_altitude)
        self.lb_altitude_val.setObjectName(u"lb_altitude_val")
        self.lb_altitude_val.setStyleSheet(u"font-size: 10pt;\n"
"border: none;\n"
"color: rgb(187, 195, 211);")

        self.horizontalLayout_10.addWidget(self.lb_altitude_val)


        self.verticalLayout_10.addWidget(self.frame_altitude)

        self.frame_time = QFrame(self.frame_gps_data)
        self.frame_time.setObjectName(u"frame_time")
        self.horizontalLayout_14 = QHBoxLayout(self.frame_time)
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
        self.lb_time = QLabel(self.frame_time)
        self.lb_time.setObjectName(u"lb_time")
        self.lb_time.setStyleSheet(u"font-size: 10pt;\n"
"border: none;\n"
"color: rgb(187, 195, 211);")

        self.horizontalLayout_14.addWidget(self.lb_time)

        self.lb_time_val = QLabel(self.frame_time)
        self.lb_time_val.setObjectName(u"lb_time_val")
        self.lb_time_val.setStyleSheet(u"font-size: 10pt;\n"
"border: none;\n"
"color: rgb(187, 195, 211);")

        self.horizontalLayout_14.addWidget(self.lb_time_val)


        self.verticalLayout_10.addWidget(self.frame_time)

        self.frame_grndSpeed = QFrame(self.frame_gps_data)
        self.frame_grndSpeed.setObjectName(u"frame_grndSpeed")
        self.horizontalLayout_15 = QHBoxLayout(self.frame_grndSpeed)
        self.horizontalLayout_15.setObjectName(u"horizontalLayout_15")
        self.lb_grndSpeed = QLabel(self.frame_grndSpeed)
        self.lb_grndSpeed.setObjectName(u"lb_grndSpeed")
        self.lb_grndSpeed.setStyleSheet(u"font-size: 10pt;\n"
"border: none;\n"
"color: rgb(187, 195, 211);")

        self.horizontalLayout_15.addWidget(self.lb_grndSpeed)

        self.lb_grndSpeed_val = QLabel(self.frame_grndSpeed)
        self.lb_grndSpeed_val.setObjectName(u"lb_grndSpeed_val")
        self.lb_grndSpeed_val.setStyleSheet(u"font-size: 10pt;\n"
"border: none;\n"
"color: rgb(187, 195, 211);")

        self.horizontalLayout_15.addWidget(self.lb_grndSpeed_val)


        self.verticalLayout_10.addWidget(self.frame_grndSpeed)

        self.frame_grndSpeed_2 = QFrame(self.frame_gps_data)
        self.frame_grndSpeed_2.setObjectName(u"frame_grndSpeed_2")
        self.horizontalLayout_16 = QHBoxLayout(self.frame_grndSpeed_2)
        self.horizontalLayout_16.setObjectName(u"horizontalLayout_16")
        self.lb_rmc_course = QLabel(self.frame_grndSpeed_2)
        self.lb_rmc_course.setObjectName(u"lb_rmc_course")
        self.lb_rmc_course.setStyleSheet(u"font-size: 10pt;\n"
"border: none;\n"
"color: rgb(187, 195, 211);")

        self.horizontalLayout_16.addWidget(self.lb_rmc_course)

        self.lb_rmc_cource_val = QLabel(self.frame_grndSpeed_2)
        self.lb_rmc_cource_val.setObjectName(u"lb_rmc_cource_val")
        self.lb_rmc_cource_val.setStyleSheet(u"font-size: 10pt;\n"
"border: none;\n"
"color: rgb(187, 195, 211);")

        self.horizontalLayout_16.addWidget(self.lb_rmc_cource_val)


        self.verticalLayout_10.addWidget(self.frame_grndSpeed_2)


        self.verticalLayout_11.addWidget(self.frame_gps_data)

        self.frame_main_imu_data = QFrame(self.centralwidget)
        self.frame_main_imu_data.setObjectName(u"frame_main_imu_data")
        self.frame_main_imu_data.setGeometry(QRect(1250, 10, 171, 471))
        self.frame_main_imu_data.setStyleSheet(u"border: 2px solid rgb(187, 195, 211);\n"
"border-radius: 5px;\n"
"background-color: none;")
        self.verticalLayout_15 = QVBoxLayout(self.frame_main_imu_data)
        self.verticalLayout_15.setObjectName(u"verticalLayout_15")
        self.lb_title_imu_data = QLabel(self.frame_main_imu_data)
        self.lb_title_imu_data.setObjectName(u"lb_title_imu_data")
        self.lb_title_imu_data.setMaximumSize(QSize(16777215, 20))
        self.lb_title_imu_data.setStyleSheet(u"font-size: 12pt;\n"
"border: none;\n"
"font: bold;\n"
"color: rgb(187, 195, 211);")
        self.lb_title_imu_data.setAlignment(Qt.AlignCenter)

        self.verticalLayout_15.addWidget(self.lb_title_imu_data)

        self.frame_imu_data = QFrame(self.frame_main_imu_data)
        self.frame_imu_data.setObjectName(u"frame_imu_data")
        self.frame_imu_data.setStyleSheet(u"border: none;")
        self.verticalLayout_14 = QVBoxLayout(self.frame_imu_data)
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.frame_AXL_X = QFrame(self.frame_imu_data)
        self.frame_AXL_X.setObjectName(u"frame_AXL_X")
        self.horizontalLayout_26 = QHBoxLayout(self.frame_AXL_X)
        self.horizontalLayout_26.setObjectName(u"horizontalLayout_26")
        self.lb_AXL_x = QLabel(self.frame_AXL_X)
        self.lb_AXL_x.setObjectName(u"lb_AXL_x")
        self.lb_AXL_x.setStyleSheet(u"font-size: 10pt;\n"
"border: none;\n"
"color: rgb(187, 195, 211);")

        self.horizontalLayout_26.addWidget(self.lb_AXL_x)

        self.lb_AXL_x_val = QLabel(self.frame_AXL_X)
        self.lb_AXL_x_val.setObjectName(u"lb_AXL_x_val")
        self.lb_AXL_x_val.setStyleSheet(u"font-size: 10pt;\n"
"border: none;\n"
"color: rgb(187, 195, 211);")

        self.horizontalLayout_26.addWidget(self.lb_AXL_x_val)


        self.verticalLayout_14.addWidget(self.frame_AXL_X)

        self.frame_AXL_y = QFrame(self.frame_imu_data)
        self.frame_AXL_y.setObjectName(u"frame_AXL_y")
        self.horizontalLayout_27 = QHBoxLayout(self.frame_AXL_y)
        self.horizontalLayout_27.setObjectName(u"horizontalLayout_27")
        self.lb_AXL_y = QLabel(self.frame_AXL_y)
        self.lb_AXL_y.setObjectName(u"lb_AXL_y")
        self.lb_AXL_y.setStyleSheet(u"font-size: 10pt;\n"
"border: none;\n"
"color: rgb(187, 195, 211);")

        self.horizontalLayout_27.addWidget(self.lb_AXL_y)

        self.lb_AXL_y_val = QLabel(self.frame_AXL_y)
        self.lb_AXL_y_val.setObjectName(u"lb_AXL_y_val")
        self.lb_AXL_y_val.setStyleSheet(u"font-size: 10pt;\n"
"border: none;\n"
"color: rgb(187, 195, 211);")

        self.horizontalLayout_27.addWidget(self.lb_AXL_y_val)


        self.verticalLayout_14.addWidget(self.frame_AXL_y)

        self.frame_AXL_z = QFrame(self.frame_imu_data)
        self.frame_AXL_z.setObjectName(u"frame_AXL_z")
        self.horizontalLayout_28 = QHBoxLayout(self.frame_AXL_z)
        self.horizontalLayout_28.setObjectName(u"horizontalLayout_28")
        self.lb_AXL_z = QLabel(self.frame_AXL_z)
        self.lb_AXL_z.setObjectName(u"lb_AXL_z")
        self.lb_AXL_z.setStyleSheet(u"font-size: 10pt;\n"
"border: none;\n"
"color: rgb(187, 195, 211);")

        self.horizontalLayout_28.addWidget(self.lb_AXL_z)

        self.lb_AXL_z_val = QLabel(self.frame_AXL_z)
        self.lb_AXL_z_val.setObjectName(u"lb_AXL_z_val")
        self.lb_AXL_z_val.setStyleSheet(u"font-size: 10pt;\n"
"border: none;\n"
"color: rgb(187, 195, 211);")

        self.horizontalLayout_28.addWidget(self.lb_AXL_z_val)


        self.verticalLayout_14.addWidget(self.frame_AXL_z)

        self.frame_MAG_x = QFrame(self.frame_imu_data)
        self.frame_MAG_x.setObjectName(u"frame_MAG_x")
        self.horizontalLayout_29 = QHBoxLayout(self.frame_MAG_x)
        self.horizontalLayout_29.setObjectName(u"horizontalLayout_29")
        self.lb_MAG_x = QLabel(self.frame_MAG_x)
        self.lb_MAG_x.setObjectName(u"lb_MAG_x")
        self.lb_MAG_x.setStyleSheet(u"font-size: 10pt;\n"
"border: none;\n"
"color: rgb(187, 195, 211);")

        self.horizontalLayout_29.addWidget(self.lb_MAG_x)

        self.lb_MAG_x_val = QLabel(self.frame_MAG_x)
        self.lb_MAG_x_val.setObjectName(u"lb_MAG_x_val")
        self.lb_MAG_x_val.setStyleSheet(u"font-size: 10pt;\n"
"border: none;\n"
"color: rgb(187, 195, 211);")

        self.horizontalLayout_29.addWidget(self.lb_MAG_x_val)


        self.verticalLayout_14.addWidget(self.frame_MAG_x)

        self.frame_MAG_y = QFrame(self.frame_imu_data)
        self.frame_MAG_y.setObjectName(u"frame_MAG_y")
        self.horizontalLayout_30 = QHBoxLayout(self.frame_MAG_y)
        self.horizontalLayout_30.setObjectName(u"horizontalLayout_30")
        self.lb_MAG_y = QLabel(self.frame_MAG_y)
        self.lb_MAG_y.setObjectName(u"lb_MAG_y")
        self.lb_MAG_y.setStyleSheet(u"font-size: 10pt;\n"
"border: none;\n"
"color: rgb(187, 195, 211);")

        self.horizontalLayout_30.addWidget(self.lb_MAG_y)

        self.lb_MAG_y_val = QLabel(self.frame_MAG_y)
        self.lb_MAG_y_val.setObjectName(u"lb_MAG_y_val")
        self.lb_MAG_y_val.setStyleSheet(u"font-size: 10pt;\n"
"border: none;\n"
"color: rgb(187, 195, 211);")

        self.horizontalLayout_30.addWidget(self.lb_MAG_y_val)


        self.verticalLayout_14.addWidget(self.frame_MAG_y)

        self.frame_MAG_z = QFrame(self.frame_imu_data)
        self.frame_MAG_z.setObjectName(u"frame_MAG_z")
        self.horizontalLayout_31 = QHBoxLayout(self.frame_MAG_z)
        self.horizontalLayout_31.setObjectName(u"horizontalLayout_31")
        self.lb_MAG_z = QLabel(self.frame_MAG_z)
        self.lb_MAG_z.setObjectName(u"lb_MAG_z")
        self.lb_MAG_z.setStyleSheet(u"font-size: 10pt;\n"
"border: none;\n"
"color: rgb(187, 195, 211);")

        self.horizontalLayout_31.addWidget(self.lb_MAG_z)

        self.lb_MAG_z_val = QLabel(self.frame_MAG_z)
        self.lb_MAG_z_val.setObjectName(u"lb_MAG_z_val")
        self.lb_MAG_z_val.setStyleSheet(u"font-size: 10pt;\n"
"border: none;\n"
"color: rgb(187, 195, 211);")

        self.horizontalLayout_31.addWidget(self.lb_MAG_z_val)


        self.verticalLayout_14.addWidget(self.frame_MAG_z)

        self.frame_GYRO_x = QFrame(self.frame_imu_data)
        self.frame_GYRO_x.setObjectName(u"frame_GYRO_x")
        self.horizontalLayout_32 = QHBoxLayout(self.frame_GYRO_x)
        self.horizontalLayout_32.setObjectName(u"horizontalLayout_32")
        self.lb_GYRO_x = QLabel(self.frame_GYRO_x)
        self.lb_GYRO_x.setObjectName(u"lb_GYRO_x")
        self.lb_GYRO_x.setStyleSheet(u"font-size: 10pt;\n"
"border: none;\n"
"color: rgb(187, 195, 211);")

        self.horizontalLayout_32.addWidget(self.lb_GYRO_x)

        self.lb_GYRO_x_val = QLabel(self.frame_GYRO_x)
        self.lb_GYRO_x_val.setObjectName(u"lb_GYRO_x_val")
        self.lb_GYRO_x_val.setStyleSheet(u"font-size: 10pt;\n"
"border: none;\n"
"color: rgb(187, 195, 211);")

        self.horizontalLayout_32.addWidget(self.lb_GYRO_x_val)


        self.verticalLayout_14.addWidget(self.frame_GYRO_x)

        self.frame_GYRO_y = QFrame(self.frame_imu_data)
        self.frame_GYRO_y.setObjectName(u"frame_GYRO_y")
        self.horizontalLayout_33 = QHBoxLayout(self.frame_GYRO_y)
        self.horizontalLayout_33.setObjectName(u"horizontalLayout_33")
        self.lb_GYRO_y = QLabel(self.frame_GYRO_y)
        self.lb_GYRO_y.setObjectName(u"lb_GYRO_y")
        self.lb_GYRO_y.setStyleSheet(u"font-size: 10pt;\n"
"border: none;\n"
"color: rgb(187, 195, 211);")

        self.horizontalLayout_33.addWidget(self.lb_GYRO_y)

        self.lb_GYRO_y_val = QLabel(self.frame_GYRO_y)
        self.lb_GYRO_y_val.setObjectName(u"lb_GYRO_y_val")
        self.lb_GYRO_y_val.setStyleSheet(u"font-size: 10pt;\n"
"border: none;\n"
"color: rgb(187, 195, 211);")

        self.horizontalLayout_33.addWidget(self.lb_GYRO_y_val)


        self.verticalLayout_14.addWidget(self.frame_GYRO_y)

        self.frame_GYRO_z = QFrame(self.frame_imu_data)
        self.frame_GYRO_z.setObjectName(u"frame_GYRO_z")
        self.horizontalLayout_34 = QHBoxLayout(self.frame_GYRO_z)
        self.horizontalLayout_34.setObjectName(u"horizontalLayout_34")
        self.lb_GYRO_z = QLabel(self.frame_GYRO_z)
        self.lb_GYRO_z.setObjectName(u"lb_GYRO_z")
        self.lb_GYRO_z.setStyleSheet(u"font-size: 10pt;\n"
"border: none;\n"
"color: rgb(187, 195, 211);")

        self.horizontalLayout_34.addWidget(self.lb_GYRO_z)

        self.lb_GYRO_z_val = QLabel(self.frame_GYRO_z)
        self.lb_GYRO_z_val.setObjectName(u"lb_GYRO_z_val")
        self.lb_GYRO_z_val.setStyleSheet(u"font-size: 10pt;\n"
"border: none;\n"
"color: rgb(187, 195, 211);")

        self.horizontalLayout_34.addWidget(self.lb_GYRO_z_val)


        self.verticalLayout_14.addWidget(self.frame_GYRO_z)

        self.frame_GndHeading = QFrame(self.frame_imu_data)
        self.frame_GndHeading.setObjectName(u"frame_GndHeading")
        self.horizontalLayout_35 = QHBoxLayout(self.frame_GndHeading)
        self.horizontalLayout_35.setObjectName(u"horizontalLayout_35")
        self.lb_GndHeading = QLabel(self.frame_GndHeading)
        self.lb_GndHeading.setObjectName(u"lb_GndHeading")
        self.lb_GndHeading.setStyleSheet(u"font-size: 10pt;\n"
"border: none;\n"
"color: rgb(187, 195, 211);")

        self.horizontalLayout_35.addWidget(self.lb_GndHeading)

        self.lb_GndHeading_val = QLabel(self.frame_GndHeading)
        self.lb_GndHeading_val.setObjectName(u"lb_GndHeading_val")
        self.lb_GndHeading_val.setStyleSheet(u"font-size: 10pt;\n"
"border: none;\n"
"color: rgb(187, 195, 211);")

        self.horizontalLayout_35.addWidget(self.lb_GndHeading_val)


        self.verticalLayout_14.addWidget(self.frame_GndHeading)


        self.verticalLayout_15.addWidget(self.frame_imu_data)

        self.lb_alfa_X = QLabel(self.centralwidget)
        self.lb_alfa_X.setObjectName(u"lb_alfa_X")
        self.lb_alfa_X.setGeometry(QRect(1275, 500, 49, 17))
        self.lb_alfa_X.setStyleSheet(u"font-size: 10pt;\n"
"border: none;\n"
"color: rgb(187, 195, 211);")
        self.lb_alfa_X_val = QLabel(self.centralwidget)
        self.lb_alfa_X_val.setObjectName(u"lb_alfa_X_val")
        self.lb_alfa_X_val.setGeometry(QRect(1330, 500, 58, 17))
        self.lb_alfa_X_val.setStyleSheet(u"font-size: 10pt;\n"
"border: none;\n"
"color: rgb(187, 195, 211);")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.lb_pwr_mnl.setText(QCoreApplication.translate("MainWindow", u"\u0417\u0430\u0434\u0430\u043d\u0438\u0435 \u043c\u043e\u0449\u043d\u043e\u0441\u0442\u0438", None))
        self.le_pwr_mnl.setText("")
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"\u0412\u044b\u0432\u043e\u0434 \u0442\u0435\u0440\u043c\u0438\u043d\u0430\u043b\u0430", None))
        self.indicator_link.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.indicator_crc.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.btn_clean_textBrw.setText(QCoreApplication.translate("MainWindow", u"\u041e\u0447\u0438\u0441\u0442\u0438\u0442\u044c", None))
        self.lb_request.setText(QCoreApplication.translate("MainWindow", u"\u0417\u0430\u043f\u0440\u043e\u0441", None))
        self.btn_gps.setText(QCoreApplication.translate("MainWindow", u"GPS", None))
        self.btn_imu.setText(QCoreApplication.translate("MainWindow", u"IMU", None))
        self.lb_mode.setText(QCoreApplication.translate("MainWindow", u"\u0412\u044b\u0431\u043e\u0440 \u0440\u0435\u0436\u0438\u043c \u0440\u0430\u0431\u043e\u0442\u044b \u0430\u043f\u043f\u0430\u0440\u0430\u0442\u0430", None))
        self.btn_mnl_mode.setText(QCoreApplication.translate("MainWindow", u"\u0420\u0443\u0447\u043d\u043e\u0439", None))
        self.btn_auto_mode.setText(QCoreApplication.translate("MainWindow", u"\u0410\u0432\u0442\u043e\u043d\u043e\u043c\u043d\u044b\u0439", None))
        self.btn_rmt_mode.setText(QCoreApplication.translate("MainWindow", u"\u0414\u0438\u0441\u0442\u0430\u043d\u0446\u0438\u043e\u043d\u043d\u044b\u0439", None))
        self.lb_mode_2.setText(QCoreApplication.translate("MainWindow", u"\u0423\u043f\u0440\u0430\u0432\u043b\u0435\u043d\u0438\u0435 \u0434\u0432\u0438\u0433\u0430\u0442\u0435\u043b\u0435\u043c", None))
        self.btn_ctrl_mtr.setText(QCoreApplication.translate("MainWindow", u"\u0421\u0442\u0430\u0440\u0442/\u0441\u0442\u043e\u043f", None))
        self.lb_main_connection.setText(QCoreApplication.translate("MainWindow", u"  \u041f\u043e\u0434\u043a\u043b\u044e\u0447\u0435\u043d\u0438\u0435 \u043a \u0443\u0441\u0442\u0440\u043e\u0439\u0441\u0442\u0432\u0443", None))
        self.cb_com_dev.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\u041d\u0435 \u0432\u044b\u0431\u0440\u0430\u043d\u043e", None))
        self.cb_baudrate.setItemText(0, QCoreApplication.translate("MainWindow", u"9600", None))
        self.cb_baudrate.setItemText(1, QCoreApplication.translate("MainWindow", u"115200", None))

        self.cb_baudrate.setPlaceholderText("")
        self.btn_disconnect.setText(QCoreApplication.translate("MainWindow", u"\u041e\u0442\u043a\u043b\u044e\u0447\u0438\u0442\u044c\u0441\u044f", None))
        self.btn_connect.setText(QCoreApplication.translate("MainWindow", u"\u041f\u043e\u0434\u043a\u043b\u044e\u0447\u0438\u0442\u044c\u0441\u044f", None))
        self.lb_mnl_cmd.setText(QCoreApplication.translate("MainWindow", u"\u0412\u0432\u043e\u0434 \u043a\u043e\u043c\u0430\u043d\u0434\u044b \u0432\u0440\u0443\u0447\u043d\u0443\u044e", None))
        self.le_mnl_cmd.setText("")
        self.btn_mnl_cmd.setText(QCoreApplication.translate("MainWindow", u"\u041e\u0442\u043f\u0440\u0430\u0432\u0438\u0442\u044c", None))
        self.lb_title_gps_data.setText(QCoreApplication.translate("MainWindow", u"\u0414\u0430\u043d\u043d\u044b\u0435 GPS", None))
        self.lb_latitude.setText(QCoreApplication.translate("MainWindow", u"Latitude", None))
        self.lb_latitude_val.setText(QCoreApplication.translate("MainWindow", u"Latitude", None))
        self.lb_NS.setText(QCoreApplication.translate("MainWindow", u"NS", None))
        self.lb_NS_val.setText(QCoreApplication.translate("MainWindow", u"NS", None))
        self.lb_longitude.setText(QCoreApplication.translate("MainWindow", u"Longitude", None))
        self.lb_longitude_val.setText(QCoreApplication.translate("MainWindow", u"Longitude", None))
        self.lb_EW.setText(QCoreApplication.translate("MainWindow", u"EW", None))
        self.lb_EW_val.setText(QCoreApplication.translate("MainWindow", u"EW", None))
        self.lb_altitude.setText(QCoreApplication.translate("MainWindow", u"Altitude", None))
        self.lb_altitude_val.setText(QCoreApplication.translate("MainWindow", u"Altitude", None))
        self.lb_time.setText(QCoreApplication.translate("MainWindow", u"Time", None))
        self.lb_time_val.setText(QCoreApplication.translate("MainWindow", u"Time", None))
        self.lb_grndSpeed.setText(QCoreApplication.translate("MainWindow", u"Speed", None))
        self.lb_grndSpeed_val.setText(QCoreApplication.translate("MainWindow", u"GndSpeed", None))
        self.lb_rmc_course.setText(QCoreApplication.translate("MainWindow", u"Course", None))
        self.lb_rmc_cource_val.setText(QCoreApplication.translate("MainWindow", u"Course", None))
        self.lb_title_imu_data.setText(QCoreApplication.translate("MainWindow", u"\u0414\u0430\u043d\u043d\u044b\u0435 IMU", None))
        self.lb_AXL_x.setText(QCoreApplication.translate("MainWindow", u"AXL_x", None))
        self.lb_AXL_x_val.setText(QCoreApplication.translate("MainWindow", u"AXL_x", None))
        self.lb_AXL_y.setText(QCoreApplication.translate("MainWindow", u"AXL_y", None))
        self.lb_AXL_y_val.setText(QCoreApplication.translate("MainWindow", u"AXL_y", None))
        self.lb_AXL_z.setText(QCoreApplication.translate("MainWindow", u"AXL_z", None))
        self.lb_AXL_z_val.setText(QCoreApplication.translate("MainWindow", u"AXL_z", None))
        self.lb_MAG_x.setText(QCoreApplication.translate("MainWindow", u"MAG_x", None))
        self.lb_MAG_x_val.setText(QCoreApplication.translate("MainWindow", u"MAG_x", None))
        self.lb_MAG_y.setText(QCoreApplication.translate("MainWindow", u"MAG_y", None))
        self.lb_MAG_y_val.setText(QCoreApplication.translate("MainWindow", u"MAG_y", None))
        self.lb_MAG_z.setText(QCoreApplication.translate("MainWindow", u"MAG_z", None))
        self.lb_MAG_z_val.setText(QCoreApplication.translate("MainWindow", u"MAG_z", None))
        self.lb_GYRO_x.setText(QCoreApplication.translate("MainWindow", u"GYRO_x", None))
        self.lb_GYRO_x_val.setText(QCoreApplication.translate("MainWindow", u"GYRO_x", None))
        self.lb_GYRO_y.setText(QCoreApplication.translate("MainWindow", u"GYRO_y", None))
        self.lb_GYRO_y_val.setText(QCoreApplication.translate("MainWindow", u"GYRO_y", None))
        self.lb_GYRO_z.setText(QCoreApplication.translate("MainWindow", u"GYRO_z", None))
        self.lb_GYRO_z_val.setText(QCoreApplication.translate("MainWindow", u"GYRO_z", None))
        self.lb_GndHeading.setText(QCoreApplication.translate("MainWindow", u"Heading", None))
        self.lb_GndHeading_val.setText(QCoreApplication.translate("MainWindow", u"GndHeading", None))
        self.lb_alfa_X.setText(QCoreApplication.translate("MainWindow", u"Alfa X", None))
        self.lb_alfa_X_val.setText(QCoreApplication.translate("MainWindow", u"GndHeading", None))
    # retranslateUi

