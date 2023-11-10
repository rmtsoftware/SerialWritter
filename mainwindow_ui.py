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
        MainWindow.resize(749, 740)
        MainWindow.setStyleSheet(u"background-color: qlineargradient(spread:pad, x1:0.506, y1:0, x2:0.494591, y2:1, stop:0 rgba(0, 0, 0, 255), stop:1 rgba(31, 56, 71, 255))")
        MainWindow.setAnimated(True)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.main_frame = QFrame(self.centralwidget)
        self.main_frame.setObjectName(u"main_frame")
        self.main_frame.setGeometry(QRect(20, 517, 331, 71))
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
        self.text_frame.setGeometry(QRect(360, 37, 381, 661))
        self.text_frame.setStyleSheet(u"border: 2px solid rgb(187, 195, 211);\n"
"border-radius: 5px;\n"
"background-color: none;")
        self.verticalLayout_4 = QVBoxLayout(self.text_frame)
        self.verticalLayout_4.setSpacing(3)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(-1, 5, -1, 5)
        self.label_2 = QLabel(self.text_frame)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setMaximumSize(QSize(16777215, 20))
        self.label_2.setStyleSheet(u"font-size: 12pt;\n"
"border: none;\n"
"font: bold;\n"
"color: rgb(187, 195, 211);")
        self.label_2.setAlignment(Qt.AlignCenter)

        self.verticalLayout_4.addWidget(self.label_2)

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
        self.req_frame.setGeometry(QRect(20, 157, 331, 111))
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
        self.mode_frame.setGeometry(QRect(20, 277, 331, 151))
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
        self.mtr_ctrl_frame.setGeometry(QRect(20, 437, 331, 71))
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
"}")

        self.verticalLayout_7.addWidget(self.btn_ctrl_mtr)


        self.horizontalLayout_3.addWidget(self.btn_mode_frame_2)

        self.main_conn_frame = QFrame(self.centralwidget)
        self.main_conn_frame.setObjectName(u"main_conn_frame")
        self.main_conn_frame.setGeometry(QRect(20, 37, 331, 111))
        self.main_conn_frame.setStyleSheet(u"border: 2px solid rgb(187, 195, 211);\n"
"border-radius: 5px;\n"
"background-color: none;")
        self.verticalLayout_5 = QVBoxLayout(self.main_conn_frame)
        self.verticalLayout_5.setSpacing(1)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.label = QLabel(self.main_conn_frame)
        self.label.setObjectName(u"label")
        self.label.setMaximumSize(QSize(16777215, 20))
        self.label.setStyleSheet(u"font-size: 12pt;\n"
"border: none;\n"
"font: bold;\n"
"color: rgb(187, 195, 211);")
        self.label.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.verticalLayout_5.addWidget(self.label)

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
        self.main_mnl_frame.setGeometry(QRect(20, 597, 331, 101))
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
"}")

        self.verticalLayout_8.addWidget(self.btn_mnl_cmd)


        self.verticalLayout_9.addWidget(self.frame)

        self.indicator_link = QLabel(self.centralwidget)
        self.indicator_link.setObjectName(u"indicator_link")
        self.indicator_link.setGeometry(QRect(260, 10, 71, 21))
        self.indicator_link.setStyleSheet(u"background-color: None;")
        self.indicator_crc = QLabel(self.centralwidget)
        self.indicator_crc.setObjectName(u"indicator_crc")
        self.indicator_crc.setGeometry(QRect(360, 10, 71, 21))
        self.indicator_crc.setStyleSheet(u"background-color: None;")
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
        self.btn_clean_textBrw.setText(QCoreApplication.translate("MainWindow", u"\u041e\u0447\u0438\u0441\u0442\u0438\u0442\u044c", None))
        self.lb_request.setText(QCoreApplication.translate("MainWindow", u"\u0417\u0430\u043f\u0440\u043e\u0441", None))
        self.btn_gps.setText(QCoreApplication.translate("MainWindow", u"GPS", None))
        self.btn_imu.setText(QCoreApplication.translate("MainWindow", u"IMU", None))
        self.lb_mode.setText(QCoreApplication.translate("MainWindow", u"\u0412\u044b\u0431\u043e\u0440 \u0440\u0435\u0436\u0438\u043c \u0440\u0430\u0431\u043e\u0442\u044b \u0430\u043f\u043f\u0430\u0440\u0430\u0442\u0430", None))
        self.btn_mnl_mode.setText(QCoreApplication.translate("MainWindow", u"\u0420\u0443\u0447\u043d\u043e\u0439", None))
        self.btn_auto_mode.setText(QCoreApplication.translate("MainWindow", u"\u0410\u0432\u0442\u043e\u043d\u043e\u043c\u043d\u044b\u0439", None))
        self.btn_rmt_mode.setText(QCoreApplication.translate("MainWindow", u"\u0414\u0438\u0441\u0442\u0430\u043d\u0446\u0438\u043e\u043d\u043d\u044b\u0439", None))
        self.lb_mode_2.setText(QCoreApplication.translate("MainWindow", u"\u0423\u043f\u0440\u0430\u0432\u043b\u0435\u043d\u0438\u0435 \u0434\u0432\u0438\u0433\u0430\u0442\u0435\u043b\u0435\u043c", None))
        self.btn_ctrl_mtr.setText(QCoreApplication.translate("MainWindow", u"\u0421\u0442\u0430\u0440\u0442", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"  \u041f\u043e\u0434\u043a\u043b\u044e\u0447\u0435\u043d\u0438\u0435 \u043a \u0443\u0441\u0442\u0440\u043e\u0439\u0441\u0442\u0432\u0443", None))
        self.cb_com_dev.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\u041d\u0435 \u0432\u044b\u0431\u0440\u0430\u043d\u043e", None))
        self.cb_baudrate.setItemText(0, QCoreApplication.translate("MainWindow", u"9600", None))
        self.cb_baudrate.setItemText(1, QCoreApplication.translate("MainWindow", u"115200", None))

        self.cb_baudrate.setPlaceholderText("")
        self.btn_disconnect.setText(QCoreApplication.translate("MainWindow", u"\u041e\u0442\u043a\u043b\u044e\u0447\u0438\u0442\u044c\u0441\u044f", None))
        self.btn_connect.setText(QCoreApplication.translate("MainWindow", u"\u041f\u043e\u0434\u043a\u043b\u044e\u0447\u0438\u0442\u044c\u0441\u044f", None))
        self.lb_mnl_cmd.setText(QCoreApplication.translate("MainWindow", u"\u0412\u0432\u043e\u0434 \u043a\u043e\u043c\u0430\u043d\u0434\u044b \u0432\u0440\u0443\u0447\u043d\u0443\u044e", None))
        self.le_mnl_cmd.setText("")
        self.btn_mnl_cmd.setText(QCoreApplication.translate("MainWindow", u"\u041e\u0442\u043f\u0440\u0430\u0432\u0438\u0442\u044c", None))
        self.indicator_link.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.indicator_crc.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
    # retranslateUi

