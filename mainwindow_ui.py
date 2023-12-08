# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'devmain.ui'
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
from PySide6.QtWidgets import (QApplication, QCheckBox, QComboBox, QHBoxLayout,
    QLabel, QLineEdit, QMainWindow, QMenuBar,
    QPushButton, QSizePolicy, QStatusBar, QTextBrowser,
    QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(746, 600)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(10, 0, 151, 20))
        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(10, 80, 51, 20))
        self.label_3 = QLabel(self.centralwidget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(10, 170, 91, 20))
        self.textBrowser = QTextBrowser(self.centralwidget)
        self.textBrowser.setObjectName(u"textBrowser")
        self.textBrowser.setGeometry(QRect(210, 320, 531, 206))
        font = QFont()
        font.setFamilies([u"Segoe UI"])
        font.setPointSize(8)
        font.setBold(False)
        font.setItalic(False)
        font.setKerning(True)
        self.textBrowser.setFont(font)
        self.textBrowser.setStyleSheet(u"")
        self.label_7 = QLabel(self.centralwidget)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setGeometry(QRect(210, 300, 151, 20))
        self.btn_clean_textBrw = QPushButton(self.centralwidget)
        self.btn_clean_textBrw.setObjectName(u"btn_clean_textBrw")
        self.btn_clean_textBrw.setGeometry(QRect(210, 530, 111, 25))
        self.btn_clean_textBrw.setMinimumSize(QSize(0, 25))
        self.btn_clean_textBrw.setStyleSheet(u"")
        self.label_8 = QLabel(self.centralwidget)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setGeometry(QRect(470, 10, 131, 20))
        self.label_9 = QLabel(self.centralwidget)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setGeometry(QRect(610, 10, 131, 20))
        self.label_10 = QLabel(self.centralwidget)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setGeometry(QRect(280, 10, 131, 20))
        self.widget = QWidget(self.centralwidget)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(10, 290, 134, 49))
        self.verticalLayout_4 = QVBoxLayout(self.widget)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.label_4 = QLabel(self.widget)
        self.label_4.setObjectName(u"label_4")

        self.verticalLayout_4.addWidget(self.label_4)

        self.btn_ctrl_mtr = QPushButton(self.widget)
        self.btn_ctrl_mtr.setObjectName(u"btn_ctrl_mtr")
        self.btn_ctrl_mtr.setMinimumSize(QSize(0, 25))
        self.btn_ctrl_mtr.setStyleSheet(u"")

        self.verticalLayout_4.addWidget(self.btn_ctrl_mtr)

        self.widget1 = QWidget(self.centralwidget)
        self.widget1.setObjectName(u"widget1")
        self.widget1.setGeometry(QRect(470, 30, 131, 211))
        self.verticalLayout = QVBoxLayout(self.widget1)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.lb_latitude = QLabel(self.widget1)
        self.lb_latitude.setObjectName(u"lb_latitude")
        self.lb_latitude.setStyleSheet(u"")

        self.horizontalLayout.addWidget(self.lb_latitude)

        self.lb_latitude_val = QLabel(self.widget1)
        self.lb_latitude_val.setObjectName(u"lb_latitude_val")
        self.lb_latitude_val.setStyleSheet(u"")

        self.horizontalLayout.addWidget(self.lb_latitude_val)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.lb_NS = QLabel(self.widget1)
        self.lb_NS.setObjectName(u"lb_NS")
        self.lb_NS.setStyleSheet(u"")

        self.horizontalLayout_2.addWidget(self.lb_NS)

        self.lb_NS_val = QLabel(self.widget1)
        self.lb_NS_val.setObjectName(u"lb_NS_val")
        self.lb_NS_val.setStyleSheet(u"")

        self.horizontalLayout_2.addWidget(self.lb_NS_val)


        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.lb_longitude = QLabel(self.widget1)
        self.lb_longitude.setObjectName(u"lb_longitude")
        self.lb_longitude.setStyleSheet(u"")

        self.horizontalLayout_3.addWidget(self.lb_longitude)

        self.lb_longitude_val = QLabel(self.widget1)
        self.lb_longitude_val.setObjectName(u"lb_longitude_val")
        self.lb_longitude_val.setStyleSheet(u"")

        self.horizontalLayout_3.addWidget(self.lb_longitude_val)


        self.verticalLayout.addLayout(self.horizontalLayout_3)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.lb_EW = QLabel(self.widget1)
        self.lb_EW.setObjectName(u"lb_EW")
        self.lb_EW.setStyleSheet(u"")

        self.horizontalLayout_4.addWidget(self.lb_EW)

        self.lb_EW_val = QLabel(self.widget1)
        self.lb_EW_val.setObjectName(u"lb_EW_val")
        self.lb_EW_val.setStyleSheet(u"")

        self.horizontalLayout_4.addWidget(self.lb_EW_val)


        self.verticalLayout.addLayout(self.horizontalLayout_4)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.lb_altitude = QLabel(self.widget1)
        self.lb_altitude.setObjectName(u"lb_altitude")
        self.lb_altitude.setStyleSheet(u"")

        self.horizontalLayout_5.addWidget(self.lb_altitude)

        self.lb_altitude_val = QLabel(self.widget1)
        self.lb_altitude_val.setObjectName(u"lb_altitude_val")
        self.lb_altitude_val.setStyleSheet(u"")

        self.horizontalLayout_5.addWidget(self.lb_altitude_val)


        self.verticalLayout.addLayout(self.horizontalLayout_5)

        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.lb_time = QLabel(self.widget1)
        self.lb_time.setObjectName(u"lb_time")
        self.lb_time.setStyleSheet(u"")

        self.horizontalLayout_6.addWidget(self.lb_time)

        self.lb_time_val = QLabel(self.widget1)
        self.lb_time_val.setObjectName(u"lb_time_val")
        self.lb_time_val.setStyleSheet(u"")

        self.horizontalLayout_6.addWidget(self.lb_time_val)


        self.verticalLayout.addLayout(self.horizontalLayout_6)

        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.lb_grndSpeed = QLabel(self.widget1)
        self.lb_grndSpeed.setObjectName(u"lb_grndSpeed")
        self.lb_grndSpeed.setStyleSheet(u"")

        self.horizontalLayout_7.addWidget(self.lb_grndSpeed)

        self.lb_grndSpeed_val = QLabel(self.widget1)
        self.lb_grndSpeed_val.setObjectName(u"lb_grndSpeed_val")
        self.lb_grndSpeed_val.setStyleSheet(u"")

        self.horizontalLayout_7.addWidget(self.lb_grndSpeed_val)


        self.verticalLayout.addLayout(self.horizontalLayout_7)

        self.horizontalLayout_8 = QHBoxLayout()
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.lb_rmc_course = QLabel(self.widget1)
        self.lb_rmc_course.setObjectName(u"lb_rmc_course")
        self.lb_rmc_course.setStyleSheet(u"")

        self.horizontalLayout_8.addWidget(self.lb_rmc_course)

        self.lb_rmc_cource_val = QLabel(self.widget1)
        self.lb_rmc_cource_val.setObjectName(u"lb_rmc_cource_val")
        self.lb_rmc_cource_val.setStyleSheet(u"")

        self.horizontalLayout_8.addWidget(self.lb_rmc_cource_val)


        self.verticalLayout.addLayout(self.horizontalLayout_8)

        self.widget2 = QWidget(self.centralwidget)
        self.widget2.setObjectName(u"widget2")
        self.widget2.setGeometry(QRect(610, 30, 131, 271))
        self.verticalLayout_2 = QVBoxLayout(self.widget2)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_9 = QHBoxLayout()
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.lb_AXL_x = QLabel(self.widget2)
        self.lb_AXL_x.setObjectName(u"lb_AXL_x")
        self.lb_AXL_x.setStyleSheet(u"")

        self.horizontalLayout_9.addWidget(self.lb_AXL_x)

        self.lb_AXL_x_val = QLabel(self.widget2)
        self.lb_AXL_x_val.setObjectName(u"lb_AXL_x_val")
        self.lb_AXL_x_val.setStyleSheet(u"")

        self.horizontalLayout_9.addWidget(self.lb_AXL_x_val)


        self.verticalLayout_2.addLayout(self.horizontalLayout_9)

        self.horizontalLayout_10 = QHBoxLayout()
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.lb_AXL_y = QLabel(self.widget2)
        self.lb_AXL_y.setObjectName(u"lb_AXL_y")
        self.lb_AXL_y.setStyleSheet(u"")

        self.horizontalLayout_10.addWidget(self.lb_AXL_y)

        self.lb_AXL_y_val = QLabel(self.widget2)
        self.lb_AXL_y_val.setObjectName(u"lb_AXL_y_val")
        self.lb_AXL_y_val.setStyleSheet(u"")

        self.horizontalLayout_10.addWidget(self.lb_AXL_y_val)


        self.verticalLayout_2.addLayout(self.horizontalLayout_10)

        self.horizontalLayout_11 = QHBoxLayout()
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.lb_AXL_z = QLabel(self.widget2)
        self.lb_AXL_z.setObjectName(u"lb_AXL_z")
        self.lb_AXL_z.setStyleSheet(u"")

        self.horizontalLayout_11.addWidget(self.lb_AXL_z)

        self.lb_AXL_z_val = QLabel(self.widget2)
        self.lb_AXL_z_val.setObjectName(u"lb_AXL_z_val")
        self.lb_AXL_z_val.setStyleSheet(u"")

        self.horizontalLayout_11.addWidget(self.lb_AXL_z_val)


        self.verticalLayout_2.addLayout(self.horizontalLayout_11)

        self.horizontalLayout_12 = QHBoxLayout()
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.lb_MAG_x = QLabel(self.widget2)
        self.lb_MAG_x.setObjectName(u"lb_MAG_x")
        self.lb_MAG_x.setStyleSheet(u"")

        self.horizontalLayout_12.addWidget(self.lb_MAG_x)

        self.lb_MAG_x_val = QLabel(self.widget2)
        self.lb_MAG_x_val.setObjectName(u"lb_MAG_x_val")
        self.lb_MAG_x_val.setStyleSheet(u"")

        self.horizontalLayout_12.addWidget(self.lb_MAG_x_val)


        self.verticalLayout_2.addLayout(self.horizontalLayout_12)

        self.horizontalLayout_13 = QHBoxLayout()
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.lb_MAG_y = QLabel(self.widget2)
        self.lb_MAG_y.setObjectName(u"lb_MAG_y")
        self.lb_MAG_y.setStyleSheet(u"")

        self.horizontalLayout_13.addWidget(self.lb_MAG_y)

        self.lb_MAG_y_val = QLabel(self.widget2)
        self.lb_MAG_y_val.setObjectName(u"lb_MAG_y_val")
        self.lb_MAG_y_val.setStyleSheet(u"")

        self.horizontalLayout_13.addWidget(self.lb_MAG_y_val)


        self.verticalLayout_2.addLayout(self.horizontalLayout_13)

        self.horizontalLayout_14 = QHBoxLayout()
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
        self.lb_MAG_z = QLabel(self.widget2)
        self.lb_MAG_z.setObjectName(u"lb_MAG_z")
        self.lb_MAG_z.setStyleSheet(u"")

        self.horizontalLayout_14.addWidget(self.lb_MAG_z)

        self.lb_MAG_z_val = QLabel(self.widget2)
        self.lb_MAG_z_val.setObjectName(u"lb_MAG_z_val")
        self.lb_MAG_z_val.setStyleSheet(u"")

        self.horizontalLayout_14.addWidget(self.lb_MAG_z_val)


        self.verticalLayout_2.addLayout(self.horizontalLayout_14)

        self.horizontalLayout_15 = QHBoxLayout()
        self.horizontalLayout_15.setObjectName(u"horizontalLayout_15")
        self.lb_GYRO_x = QLabel(self.widget2)
        self.lb_GYRO_x.setObjectName(u"lb_GYRO_x")
        self.lb_GYRO_x.setStyleSheet(u"")

        self.horizontalLayout_15.addWidget(self.lb_GYRO_x)

        self.lb_GYRO_x_val = QLabel(self.widget2)
        self.lb_GYRO_x_val.setObjectName(u"lb_GYRO_x_val")
        self.lb_GYRO_x_val.setStyleSheet(u"")

        self.horizontalLayout_15.addWidget(self.lb_GYRO_x_val)


        self.verticalLayout_2.addLayout(self.horizontalLayout_15)

        self.horizontalLayout_16 = QHBoxLayout()
        self.horizontalLayout_16.setObjectName(u"horizontalLayout_16")
        self.lb_GYRO_y = QLabel(self.widget2)
        self.lb_GYRO_y.setObjectName(u"lb_GYRO_y")
        self.lb_GYRO_y.setStyleSheet(u"")

        self.horizontalLayout_16.addWidget(self.lb_GYRO_y)

        self.lb_GYRO_y_val = QLabel(self.widget2)
        self.lb_GYRO_y_val.setObjectName(u"lb_GYRO_y_val")
        self.lb_GYRO_y_val.setStyleSheet(u"")

        self.horizontalLayout_16.addWidget(self.lb_GYRO_y_val)


        self.verticalLayout_2.addLayout(self.horizontalLayout_16)

        self.horizontalLayout_17 = QHBoxLayout()
        self.horizontalLayout_17.setObjectName(u"horizontalLayout_17")
        self.lb_GYRO_z = QLabel(self.widget2)
        self.lb_GYRO_z.setObjectName(u"lb_GYRO_z")
        self.lb_GYRO_z.setStyleSheet(u"")

        self.horizontalLayout_17.addWidget(self.lb_GYRO_z)

        self.lb_GYRO_z_val = QLabel(self.widget2)
        self.lb_GYRO_z_val.setObjectName(u"lb_GYRO_z_val")
        self.lb_GYRO_z_val.setStyleSheet(u"")

        self.horizontalLayout_17.addWidget(self.lb_GYRO_z_val)


        self.verticalLayout_2.addLayout(self.horizontalLayout_17)

        self.horizontalLayout_18 = QHBoxLayout()
        self.horizontalLayout_18.setObjectName(u"horizontalLayout_18")
        self.lb_GndHeading = QLabel(self.widget2)
        self.lb_GndHeading.setObjectName(u"lb_GndHeading")
        self.lb_GndHeading.setStyleSheet(u"")

        self.horizontalLayout_18.addWidget(self.lb_GndHeading)

        self.lb_GndHeading_val = QLabel(self.widget2)
        self.lb_GndHeading_val.setObjectName(u"lb_GndHeading_val")
        self.lb_GndHeading_val.setStyleSheet(u"")

        self.horizontalLayout_18.addWidget(self.lb_GndHeading_val)


        self.verticalLayout_2.addLayout(self.horizontalLayout_18)

        self.widget3 = QWidget(self.centralwidget)
        self.widget3.setObjectName(u"widget3")
        self.widget3.setGeometry(QRect(10, 100, 221, 62))
        self.verticalLayout_3 = QVBoxLayout(self.widget3)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_20 = QHBoxLayout()
        self.horizontalLayout_20.setObjectName(u"horizontalLayout_20")
        self.btn_gps = QPushButton(self.widget3)
        self.btn_gps.setObjectName(u"btn_gps")
        self.btn_gps.setMinimumSize(QSize(0, 25))
        self.btn_gps.setStyleSheet(u"")

        self.horizontalLayout_20.addWidget(self.btn_gps)

        self.checkBox = QCheckBox(self.widget3)
        self.checkBox.setObjectName(u"checkBox")

        self.horizontalLayout_20.addWidget(self.checkBox)


        self.verticalLayout_3.addLayout(self.horizontalLayout_20)

        self.horizontalLayout_19 = QHBoxLayout()
        self.horizontalLayout_19.setObjectName(u"horizontalLayout_19")
        self.btn_imu = QPushButton(self.widget3)
        self.btn_imu.setObjectName(u"btn_imu")
        self.btn_imu.setMinimumSize(QSize(0, 25))
        self.btn_imu.setStyleSheet(u"")

        self.horizontalLayout_19.addWidget(self.btn_imu)

        self.checkBox_2 = QCheckBox(self.widget3)
        self.checkBox_2.setObjectName(u"checkBox_2")

        self.horizontalLayout_19.addWidget(self.checkBox_2)


        self.verticalLayout_3.addLayout(self.horizontalLayout_19)

        self.widget4 = QWidget(self.centralwidget)
        self.widget4.setObjectName(u"widget4")
        self.widget4.setGeometry(QRect(10, 20, 201, 27))
        self.horizontalLayout_21 = QHBoxLayout(self.widget4)
        self.horizontalLayout_21.setObjectName(u"horizontalLayout_21")
        self.horizontalLayout_21.setContentsMargins(0, 0, 0, 0)
        self.cb_com_dev = QComboBox(self.widget4)
        self.cb_com_dev.setObjectName(u"cb_com_dev")
        self.cb_com_dev.setMinimumSize(QSize(0, 25))
        self.cb_com_dev.setLayoutDirection(Qt.LeftToRight)
        self.cb_com_dev.setStyleSheet(u"")

        self.horizontalLayout_21.addWidget(self.cb_com_dev)

        self.cb_baudrate = QComboBox(self.widget4)
        self.cb_baudrate.addItem("")
        self.cb_baudrate.addItem("")
        self.cb_baudrate.setObjectName(u"cb_baudrate")
        self.cb_baudrate.setMinimumSize(QSize(0, 25))
        self.cb_baudrate.setStyleSheet(u"")

        self.horizontalLayout_21.addWidget(self.cb_baudrate)

        self.widget5 = QWidget(self.centralwidget)
        self.widget5.setObjectName(u"widget5")
        self.widget5.setGeometry(QRect(10, 50, 201, 27))
        self.horizontalLayout_22 = QHBoxLayout(self.widget5)
        self.horizontalLayout_22.setObjectName(u"horizontalLayout_22")
        self.horizontalLayout_22.setContentsMargins(0, 0, 0, 0)
        self.btn_disconnect = QPushButton(self.widget5)
        self.btn_disconnect.setObjectName(u"btn_disconnect")
        self.btn_disconnect.setMinimumSize(QSize(0, 25))
        self.btn_disconnect.setStyleSheet(u"")

        self.horizontalLayout_22.addWidget(self.btn_disconnect)

        self.btn_connect = QPushButton(self.widget5)
        self.btn_connect.setObjectName(u"btn_connect")
        self.btn_connect.setMinimumSize(QSize(0, 25))
        self.btn_connect.setStyleSheet(u"")

        self.horizontalLayout_22.addWidget(self.btn_connect)

        self.widget6 = QWidget(self.centralwidget)
        self.widget6.setObjectName(u"widget6")
        self.widget6.setGeometry(QRect(10, 410, 134, 80))
        self.verticalLayout_6 = QVBoxLayout(self.widget6)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.label_6 = QLabel(self.widget6)
        self.label_6.setObjectName(u"label_6")

        self.verticalLayout_6.addWidget(self.label_6)

        self.le_mnl_cmd = QLineEdit(self.widget6)
        self.le_mnl_cmd.setObjectName(u"le_mnl_cmd")
        self.le_mnl_cmd.setMinimumSize(QSize(0, 25))
        self.le_mnl_cmd.setMaximumSize(QSize(16777215, 16777215))
        self.le_mnl_cmd.setStyleSheet(u"")

        self.verticalLayout_6.addWidget(self.le_mnl_cmd)

        self.btn_mnl_cmd = QPushButton(self.widget6)
        self.btn_mnl_cmd.setObjectName(u"btn_mnl_cmd")
        self.btn_mnl_cmd.setMinimumSize(QSize(0, 25))
        self.btn_mnl_cmd.setStyleSheet(u"")

        self.verticalLayout_6.addWidget(self.btn_mnl_cmd)

        self.widget7 = QWidget(self.centralwidget)
        self.widget7.setObjectName(u"widget7")
        self.widget7.setGeometry(QRect(10, 350, 134, 49))
        self.verticalLayout_5 = QVBoxLayout(self.widget7)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.label_5 = QLabel(self.widget7)
        self.label_5.setObjectName(u"label_5")

        self.verticalLayout_5.addWidget(self.label_5)

        self.le_pwr_mnl = QLineEdit(self.widget7)
        self.le_pwr_mnl.setObjectName(u"le_pwr_mnl")
        self.le_pwr_mnl.setMinimumSize(QSize(0, 25))
        self.le_pwr_mnl.setMaximumSize(QSize(16777215, 16777215))
        self.le_pwr_mnl.setStyleSheet(u"")

        self.verticalLayout_5.addWidget(self.le_pwr_mnl)

        self.widget8 = QWidget(self.centralwidget)
        self.widget8.setObjectName(u"widget8")
        self.widget8.setGeometry(QRect(11, 191, 131, 89))
        self.verticalLayout_7 = QVBoxLayout(self.widget8)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.btn_mnl_mode = QPushButton(self.widget8)
        self.btn_mnl_mode.setObjectName(u"btn_mnl_mode")
        self.btn_mnl_mode.setMinimumSize(QSize(0, 25))
        self.btn_mnl_mode.setStyleSheet(u"")

        self.verticalLayout_7.addWidget(self.btn_mnl_mode)

        self.btn_auto_mode = QPushButton(self.widget8)
        self.btn_auto_mode.setObjectName(u"btn_auto_mode")
        self.btn_auto_mode.setMinimumSize(QSize(0, 25))
        self.btn_auto_mode.setStyleSheet(u"")

        self.verticalLayout_7.addWidget(self.btn_auto_mode)

        self.btn_rmt_mode = QPushButton(self.widget8)
        self.btn_rmt_mode.setObjectName(u"btn_rmt_mode")
        self.btn_rmt_mode.setMinimumSize(QSize(0, 25))
        self.btn_rmt_mode.setStyleSheet(u"")

        self.verticalLayout_7.addWidget(self.btn_rmt_mode)

        self.widget9 = QWidget(self.centralwidget)
        self.widget9.setObjectName(u"widget9")
        self.widget9.setGeometry(QRect(270, 40, 151, 18))
        self.horizontalLayout_23 = QHBoxLayout(self.widget9)
        self.horizontalLayout_23.setObjectName(u"horizontalLayout_23")
        self.horizontalLayout_23.setContentsMargins(0, 0, 0, 0)
        self.lb_rmode = QLabel(self.widget9)
        self.lb_rmode.setObjectName(u"lb_rmode")
        self.lb_rmode.setStyleSheet(u"")

        self.horizontalLayout_23.addWidget(self.lb_rmode)

        self.lb_rmode_val = QLabel(self.widget9)
        self.lb_rmode_val.setObjectName(u"lb_rmode_val")
        self.lb_rmode_val.setStyleSheet(u"")

        self.horizontalLayout_23.addWidget(self.lb_rmode_val)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 746, 22))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"\u041f\u043e\u0434\u043a\u043b\u044e\u0447\u0435\u043d\u0438\u0435", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"\u0417\u0430\u043f\u0440\u043e\u0441", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"\u0412\u044b\u0431\u043e\u0440 \u0440\u0435\u0436\u0438\u043c\u0430", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"\u0422\u0435\u0440\u043c\u0438\u043d\u0430\u043b\u0430", None))
        self.btn_clean_textBrw.setText(QCoreApplication.translate("MainWindow", u"\u041e\u0447\u0438\u0441\u0442\u0438\u0442\u044c", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"GPS Data", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"IMU Data", None))
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"\u0421\u0442\u0430\u0442\u0443\u0441 \u043f\u043e\u0434\u043a\u043b\u044e\u0447\u0435\u043d\u0438\u044f", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"\u0423\u043f\u0440\u0430\u0432\u043b\u0435\u043d\u0438\u0435 \u0434\u0432\u0438\u0433\u0430\u0442\u0435\u043b\u0435\u043c", None))
        self.btn_ctrl_mtr.setText(QCoreApplication.translate("MainWindow", u"\u0421\u0442\u0430\u0440\u0442/\u0441\u0442\u043e\u043f", None))
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
        self.btn_gps.setText(QCoreApplication.translate("MainWindow", u"GPS", None))
        self.checkBox.setText(QCoreApplication.translate("MainWindow", u"\u0410\u0432\u0442\u043e \u0437\u0430\u043f\u0440\u043e\u0441 GPS", None))
        self.btn_imu.setText(QCoreApplication.translate("MainWindow", u"IMU", None))
        self.checkBox_2.setText(QCoreApplication.translate("MainWindow", u"\u0410\u0432\u0442\u043e \u0437\u0430\u043f\u0440\u043e\u0441 IMU", None))
        self.cb_com_dev.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\u041d\u0435 \u0432\u044b\u0431\u0440\u0430\u043d\u043e", None))
        self.cb_baudrate.setItemText(0, QCoreApplication.translate("MainWindow", u"9600", None))
        self.cb_baudrate.setItemText(1, QCoreApplication.translate("MainWindow", u"115200", None))

        self.cb_baudrate.setPlaceholderText("")
        self.btn_disconnect.setText(QCoreApplication.translate("MainWindow", u"\u041e\u0442\u043a\u043b\u044e\u0447\u0438\u0442\u044c\u0441\u044f", None))
        self.btn_connect.setText(QCoreApplication.translate("MainWindow", u"\u041f\u043e\u0434\u043a\u043b\u044e\u0447\u0438\u0442\u044c\u0441\u044f", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"\u0412\u0432\u043e\u0434 \u043a\u043e\u043c\u0430\u043d\u0434\u044b \u0432\u0440\u0443\u0447\u043d\u0443\u044e", None))
        self.le_mnl_cmd.setText("")
        self.btn_mnl_cmd.setText(QCoreApplication.translate("MainWindow", u"\u041e\u0442\u043f\u0440\u0430\u0432\u0438\u0442\u044c", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"\u0417\u0430\u0434\u0430\u043d\u0438\u0435 \u043c\u043e\u0449\u043d\u043e\u0441\u0442\u0438", None))
        self.le_pwr_mnl.setText("")
        self.btn_mnl_mode.setText(QCoreApplication.translate("MainWindow", u"\u0420\u0443\u0447\u043d\u043e\u0439", None))
        self.btn_auto_mode.setText(QCoreApplication.translate("MainWindow", u"\u0410\u0432\u0442\u043e\u043d\u043e\u043c\u043d\u044b\u0439", None))
        self.btn_rmt_mode.setText(QCoreApplication.translate("MainWindow", u"\u0414\u0438\u0441\u0442\u0430\u043d\u0446\u0438\u043e\u043d\u043d\u044b\u0439", None))
        self.lb_rmode.setText(QCoreApplication.translate("MainWindow", u"\u0420\u0435\u0436\u0438\u043c", None))
        self.lb_rmode_val.setText(QCoreApplication.translate("MainWindow", u"\u0437\u043d\u0420\u0435\u0436\u0438\u043c", None))
    # retranslateUi

