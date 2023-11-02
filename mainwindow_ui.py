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
    QSizePolicy, QStatusBar, QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(401, 594)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.main_frame = QFrame(self.centralwidget)
        self.main_frame.setObjectName(u"main_frame")
        self.main_frame.setGeometry(QRect(10, 50, 381, 391))
        self.main_frame.setStyleSheet(u"font: bold;\n"
"")
        self.verticalLayout_3 = QVBoxLayout(self.main_frame)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.req_frame = QFrame(self.main_frame)
        self.req_frame.setObjectName(u"req_frame")
        self.horizontalLayout_4 = QHBoxLayout(self.req_frame)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.lb_request = QLabel(self.req_frame)
        self.lb_request.setObjectName(u"lb_request")
        self.lb_request.setStyleSheet(u"font-size: 12pt;")

        self.horizontalLayout_4.addWidget(self.lb_request)

        self.btn_req_frame = QFrame(self.req_frame)
        self.btn_req_frame.setObjectName(u"btn_req_frame")
        self.verticalLayout_2 = QVBoxLayout(self.btn_req_frame)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.btn_gps = QPushButton(self.btn_req_frame)
        self.btn_gps.setObjectName(u"btn_gps")

        self.verticalLayout_2.addWidget(self.btn_gps)

        self.btn_imu = QPushButton(self.btn_req_frame)
        self.btn_imu.setObjectName(u"btn_imu")

        self.verticalLayout_2.addWidget(self.btn_imu)


        self.horizontalLayout_4.addWidget(self.btn_req_frame)


        self.verticalLayout_3.addWidget(self.req_frame)

        self.mode_frame = QFrame(self.main_frame)
        self.mode_frame.setObjectName(u"mode_frame")
        self.horizontalLayout = QHBoxLayout(self.mode_frame)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.lb_mode = QLabel(self.mode_frame)
        self.lb_mode.setObjectName(u"lb_mode")
        self.lb_mode.setStyleSheet(u"font-size: 12pt;")

        self.horizontalLayout.addWidget(self.lb_mode)

        self.btn_mode_frame = QFrame(self.mode_frame)
        self.btn_mode_frame.setObjectName(u"btn_mode_frame")
        self.verticalLayout = QVBoxLayout(self.btn_mode_frame)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.btn_mnl_mode = QPushButton(self.btn_mode_frame)
        self.btn_mnl_mode.setObjectName(u"btn_mnl_mode")

        self.verticalLayout.addWidget(self.btn_mnl_mode)

        self.btn_auto_mode = QPushButton(self.btn_mode_frame)
        self.btn_auto_mode.setObjectName(u"btn_auto_mode")

        self.verticalLayout.addWidget(self.btn_auto_mode)

        self.btn_rmt_mode = QPushButton(self.btn_mode_frame)
        self.btn_rmt_mode.setObjectName(u"btn_rmt_mode")

        self.verticalLayout.addWidget(self.btn_rmt_mode)


        self.horizontalLayout.addWidget(self.btn_mode_frame)


        self.verticalLayout_3.addWidget(self.mode_frame)

        self.pwr_mtr_frame = QFrame(self.main_frame)
        self.pwr_mtr_frame.setObjectName(u"pwr_mtr_frame")
        self.horizontalLayout_2 = QHBoxLayout(self.pwr_mtr_frame)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.lb_pwr_mnl = QLabel(self.pwr_mtr_frame)
        self.lb_pwr_mnl.setObjectName(u"lb_pwr_mnl")
        self.lb_pwr_mnl.setStyleSheet(u"font-size: 12pt;")

        self.horizontalLayout_2.addWidget(self.lb_pwr_mnl)

        self.le_pwr_mnl = QLineEdit(self.pwr_mtr_frame)
        self.le_pwr_mnl.setObjectName(u"le_pwr_mnl")
        self.le_pwr_mnl.setMaximumSize(QSize(186, 16777215))

        self.horizontalLayout_2.addWidget(self.le_pwr_mnl)


        self.verticalLayout_3.addWidget(self.pwr_mtr_frame)

        self.ctrl_mtr_frame = QFrame(self.main_frame)
        self.ctrl_mtr_frame.setObjectName(u"ctrl_mtr_frame")
        self.horizontalLayout_3 = QHBoxLayout(self.ctrl_mtr_frame)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.lb_motor = QLabel(self.ctrl_mtr_frame)
        self.lb_motor.setObjectName(u"lb_motor")
        self.lb_motor.setStyleSheet(u"font-size: 12pt;")

        self.horizontalLayout_3.addWidget(self.lb_motor)

        self.btn_ctrl_mtr = QPushButton(self.ctrl_mtr_frame)
        self.btn_ctrl_mtr.setObjectName(u"btn_ctrl_mtr")

        self.horizontalLayout_3.addWidget(self.btn_ctrl_mtr)


        self.verticalLayout_3.addWidget(self.ctrl_mtr_frame)

        self.conn_frame_2 = QFrame(self.centralwidget)
        self.conn_frame_2.setObjectName(u"conn_frame_2")
        self.conn_frame_2.setGeometry(QRect(10, 0, 381, 61))
        self.conn_frame = QHBoxLayout(self.conn_frame_2)
        self.conn_frame.setObjectName(u"conn_frame")
        self.btn_connect = QPushButton(self.conn_frame_2)
        self.btn_connect.setObjectName(u"btn_connect")

        self.conn_frame.addWidget(self.btn_connect)

        self.btn_disconnect = QPushButton(self.conn_frame_2)
        self.btn_disconnect.setObjectName(u"btn_disconnect")

        self.conn_frame.addWidget(self.btn_disconnect)

        self.cb_com_dev = QComboBox(self.centralwidget)
        self.cb_com_dev.setObjectName(u"cb_com_dev")
        self.cb_com_dev.setGeometry(QRect(20, 460, 111, 22))
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.lb_request.setText(QCoreApplication.translate("MainWindow", u"\u0417\u0430\u043f\u0440\u043e\u0441", None))
        self.btn_gps.setText(QCoreApplication.translate("MainWindow", u"GPS", None))
        self.btn_imu.setText(QCoreApplication.translate("MainWindow", u"IMU", None))
        self.lb_mode.setText(QCoreApplication.translate("MainWindow", u"\u0420\u0435\u0436\u0438\u043c", None))
        self.btn_mnl_mode.setText(QCoreApplication.translate("MainWindow", u"\u0420\u0443\u0447\u043d\u043e\u0439", None))
        self.btn_auto_mode.setText(QCoreApplication.translate("MainWindow", u"\u0410\u0432\u0442\u043e\u043d\u043e\u043c\u043d\u044b\u0439", None))
        self.btn_rmt_mode.setText(QCoreApplication.translate("MainWindow", u"\u0414\u0438\u0441\u0442\u0430\u043d\u0446\u0438\u043e\u043d\u043d\u044b\u0439", None))
        self.lb_pwr_mnl.setText(QCoreApplication.translate("MainWindow", u"\u041c\u043e\u0449\u043d\u043e\u0441\u0442\u044c", None))
        self.lb_motor.setText(QCoreApplication.translate("MainWindow", u"\u0414\u0432\u0438\u0433\u0430\u0442\u0435\u043b\u044c", None))
        self.btn_ctrl_mtr.setText(QCoreApplication.translate("MainWindow", u"\u0421\u0442\u0430\u0440\u0442", None))
        self.btn_connect.setText(QCoreApplication.translate("MainWindow", u"\u041f\u043e\u0434\u043a\u043b\u044e\u0447\u0438\u0442\u044c\u0441\u044f", None))
        self.btn_disconnect.setText(QCoreApplication.translate("MainWindow", u"\u041e\u0442\u043a\u043b\u044e\u0447\u0438\u0442\u044c\u0441\u044f", None))
        self.cb_com_dev.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\u043d\u0435 \u0432\u044b\u0431\u0440\u0430\u043d\u043e", None))
    # retranslateUi

