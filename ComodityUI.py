# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'd:\ArbitrageMonitor\ArbitrageDemo.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_ComodityMonitor(object):
    def setupUi(self, ComodityMonitor):
        ComodityMonitor.setObjectName("ComodityMonitor")
        ComodityMonitor.resize(1535, 575)
        ComodityMonitor.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
        self.centralwidget = QtWidgets.QWidget(ComodityMonitor)
        self.centralwidget.setObjectName("centralwidget")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(10, 10, 1521, 521))
        self.tabWidget.setObjectName("tabWidget")
        self.tab_1 = QtWidgets.QWidget()
        self.tab_1.setObjectName("tab_1")
        self.tableWidget = QtWidgets.QTableWidget(self.tab_1)
        self.tableWidget.setGeometry(QtCore.QRect(10, 10, 1491, 481))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(14)
        self.tableWidget.setRowCount(15)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(7, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(8, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(9, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(10, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(11, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(12, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(13, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(14, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(7, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(8, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(9, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(10, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(11, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(12, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(13, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(2, 1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(2, 4, item)
        self.tabWidget.addTab(self.tab_1, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.tableWidget_2 = QtWidgets.QTableWidget(self.tab_2)
        self.tableWidget_2.setGeometry(QtCore.QRect(10, 10, 1501, 481))
        self.tableWidget_2.setObjectName("tableWidget_2")
        self.tableWidget_2.setColumnCount(23)
        self.tableWidget_2.setRowCount(32)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setVerticalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setVerticalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setVerticalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setVerticalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setVerticalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setVerticalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setVerticalHeaderItem(7, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setVerticalHeaderItem(8, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setVerticalHeaderItem(9, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setVerticalHeaderItem(10, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setVerticalHeaderItem(11, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setVerticalHeaderItem(12, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setVerticalHeaderItem(13, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setVerticalHeaderItem(14, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setVerticalHeaderItem(15, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setVerticalHeaderItem(16, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setVerticalHeaderItem(17, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setVerticalHeaderItem(18, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setVerticalHeaderItem(19, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setVerticalHeaderItem(20, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setVerticalHeaderItem(21, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setVerticalHeaderItem(22, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setVerticalHeaderItem(23, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setVerticalHeaderItem(24, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setVerticalHeaderItem(25, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setVerticalHeaderItem(26, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setVerticalHeaderItem(27, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setVerticalHeaderItem(28, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setVerticalHeaderItem(29, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setVerticalHeaderItem(30, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setVerticalHeaderItem(31, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(7, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(8, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(9, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(10, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(11, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(12, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(13, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(14, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(15, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(16, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(17, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(18, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(19, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(20, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(21, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(22, item)
        self.tabWidget.addTab(self.tab_2, "")
        ComodityMonitor.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(ComodityMonitor)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1535, 23))
        self.menubar.setObjectName("menubar")
        self.menuAbout = QtWidgets.QMenu(self.menubar)
        self.menuAbout.setObjectName("menuAbout")
        ComodityMonitor.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(ComodityMonitor)
        self.statusbar.setObjectName("statusbar")
        ComodityMonitor.setStatusBar(self.statusbar)
        self.actionAbout_Me = QtWidgets.QAction(ComodityMonitor)
        self.actionAbout_Me.setObjectName("actionAbout_Me")
        self.actionExit = QtWidgets.QAction(ComodityMonitor)
        self.actionExit.setObjectName("actionExit")
        self.menuAbout.addAction(self.actionAbout_Me)
        self.menuAbout.addAction(self.actionExit)
        self.menubar.addAction(self.menuAbout.menuAction())

        self.retranslateUi(ComodityMonitor)
        self.tabWidget.setCurrentIndex(1)
        QtCore.QMetaObject.connectSlotsByName(ComodityMonitor)

    def retranslateUi(self, ComodityMonitor):
        _translate = QtCore.QCoreApplication.translate
        ComodityMonitor.setWindowTitle(_translate("ComodityMonitor", "ComodityMonitor"))
        item = self.tableWidget.verticalHeaderItem(0)
        item.setText(_translate("ComodityMonitor", "豆油/豆粕"))
        item = self.tableWidget.verticalHeaderItem(1)
        item.setText(_translate("ComodityMonitor", "豆粕-菜粕"))
        item = self.tableWidget.verticalHeaderItem(2)
        item.setText(_translate("ComodityMonitor", "豆油-棕榈油"))
        item = self.tableWidget.verticalHeaderItem(3)
        item.setText(_translate("ComodityMonitor", "菜油-豆油"))
        item = self.tableWidget.verticalHeaderItem(4)
        item.setText(_translate("ComodityMonitor", "菜油-棕榈油"))
        item = self.tableWidget.verticalHeaderItem(5)
        item.setText(_translate("ComodityMonitor", "菜油/菜粕"))
        item = self.tableWidget.verticalHeaderItem(6)
        item.setText(_translate("ComodityMonitor", "玉米淀粉-玉米"))
        item = self.tableWidget.verticalHeaderItem(7)
        item.setText(_translate("ComodityMonitor", "螺纹钢-热卷"))
        item = self.tableWidget.verticalHeaderItem(8)
        item.setText(_translate("ComodityMonitor", "螺纹钢/铁矿石"))
        item = self.tableWidget.verticalHeaderItem(9)
        item.setText(_translate("ComodityMonitor", "焦炭/焦煤"))
        item = self.tableWidget.verticalHeaderItem(10)
        item.setText(_translate("ComodityMonitor", "L-PP"))
        item = self.tableWidget.verticalHeaderItem(11)
        item.setText(_translate("ComodityMonitor", "PP-3*MA"))
        item = self.tableWidget.verticalHeaderItem(12)
        item.setText(_translate("ComodityMonitor", "铝/锌"))
        item = self.tableWidget.verticalHeaderItem(13)
        item.setText(_translate("ComodityMonitor", "铜/锌"))
        item = self.tableWidget.verticalHeaderItem(14)
        item.setText(_translate("ComodityMonitor", "金/银"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("ComodityMonitor", "起始时间"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("ComodityMonitor", "最后时间"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("ComodityMonitor", "价格1"))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("ComodityMonitor", "价格2"))
        item = self.tableWidget.horizontalHeaderItem(4)
        item.setText(_translate("ComodityMonitor", "现值"))
        item = self.tableWidget.horizontalHeaderItem(5)
        item.setText(_translate("ComodityMonitor", "前值"))
        item = self.tableWidget.horizontalHeaderItem(6)
        item.setText(_translate("ComodityMonitor", "前10个交易日"))
        item = self.tableWidget.horizontalHeaderItem(7)
        item.setText(_translate("ComodityMonitor", "前20个交易日"))
        item = self.tableWidget.horizontalHeaderItem(8)
        item.setText(_translate("ComodityMonitor", "前30个交易日"))
        item = self.tableWidget.horizontalHeaderItem(9)
        item.setText(_translate("ComodityMonitor", "最小值"))
        item = self.tableWidget.horizontalHeaderItem(10)
        item.setText(_translate("ComodityMonitor", "5%分位"))
        item = self.tableWidget.horizontalHeaderItem(11)
        item.setText(_translate("ComodityMonitor", "中位数"))
        item = self.tableWidget.horizontalHeaderItem(12)
        item.setText(_translate("ComodityMonitor", "95%分位"))
        item = self.tableWidget.horizontalHeaderItem(13)
        item.setText(_translate("ComodityMonitor", "最大值"))
        __sortingEnabled = self.tableWidget.isSortingEnabled()
        self.tableWidget.setSortingEnabled(False)
        self.tableWidget.setSortingEnabled(__sortingEnabled)
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_1), _translate("ComodityMonitor", "价差监控"))
        item = self.tableWidget_2.verticalHeaderItem(0)
        item.setText(_translate("ComodityMonitor", "豆一"))
        item = self.tableWidget_2.verticalHeaderItem(1)
        item.setText(_translate("ComodityMonitor", "豆油"))
        item = self.tableWidget_2.verticalHeaderItem(2)
        item.setText(_translate("ComodityMonitor", "豆粕"))
        item = self.tableWidget_2.verticalHeaderItem(3)
        item.setText(_translate("ComodityMonitor", "菜油"))
        item = self.tableWidget_2.verticalHeaderItem(4)
        item.setText(_translate("ComodityMonitor", "菜粕"))
        item = self.tableWidget_2.verticalHeaderItem(5)
        item.setText(_translate("ComodityMonitor", "棕榈油"))
        item = self.tableWidget_2.verticalHeaderItem(6)
        item.setText(_translate("ComodityMonitor", "玉米淀粉"))
        item = self.tableWidget_2.verticalHeaderItem(7)
        item.setText(_translate("ComodityMonitor", "玉米"))
        item = self.tableWidget_2.verticalHeaderItem(8)
        item.setText(_translate("ComodityMonitor", "苹果"))
        item = self.tableWidget_2.verticalHeaderItem(9)
        item.setText(_translate("ComodityMonitor", "白糖"))
        item = self.tableWidget_2.verticalHeaderItem(10)
        item.setText(_translate("ComodityMonitor", "棉花"))
        item = self.tableWidget_2.verticalHeaderItem(11)
        item.setText(_translate("ComodityMonitor", "鸡蛋"))
        item = self.tableWidget_2.verticalHeaderItem(12)
        item.setText(_translate("ComodityMonitor", "橡胶"))
        item = self.tableWidget_2.verticalHeaderItem(13)
        item.setText(_translate("ComodityMonitor", "螺纹钢"))
        item = self.tableWidget_2.verticalHeaderItem(14)
        item.setText(_translate("ComodityMonitor", "热卷"))
        item = self.tableWidget_2.verticalHeaderItem(15)
        item.setText(_translate("ComodityMonitor", "铁矿石"))
        item = self.tableWidget_2.verticalHeaderItem(16)
        item.setText(_translate("ComodityMonitor", "焦炭"))
        item = self.tableWidget_2.verticalHeaderItem(17)
        item.setText(_translate("ComodityMonitor", "焦煤"))
        item = self.tableWidget_2.verticalHeaderItem(18)
        item.setText(_translate("ComodityMonitor", "动力煤"))
        item = self.tableWidget_2.verticalHeaderItem(19)
        item.setText(_translate("ComodityMonitor", "玻璃"))
        item = self.tableWidget_2.verticalHeaderItem(20)
        item.setText(_translate("ComodityMonitor", "硅铁"))
        item = self.tableWidget_2.verticalHeaderItem(21)
        item.setText(_translate("ComodityMonitor", "锰硅"))
        item = self.tableWidget_2.verticalHeaderItem(22)
        item.setText(_translate("ComodityMonitor", "塑料"))
        item = self.tableWidget_2.verticalHeaderItem(23)
        item.setText(_translate("ComodityMonitor", "PVC"))
        item = self.tableWidget_2.verticalHeaderItem(24)
        item.setText(_translate("ComodityMonitor", "聚丙烯"))
        item = self.tableWidget_2.verticalHeaderItem(25)
        item.setText(_translate("ComodityMonitor", "PTA"))
        item = self.tableWidget_2.verticalHeaderItem(26)
        item.setText(_translate("ComodityMonitor", "甲醇"))
        item = self.tableWidget_2.verticalHeaderItem(27)
        item.setText(_translate("ComodityMonitor", "铝"))
        item = self.tableWidget_2.verticalHeaderItem(28)
        item.setText(_translate("ComodityMonitor", "锌"))
        item = self.tableWidget_2.verticalHeaderItem(29)
        item.setText(_translate("ComodityMonitor", "金"))
        item = self.tableWidget_2.verticalHeaderItem(30)
        item.setText(_translate("ComodityMonitor", "银"))
        item = self.tableWidget_2.verticalHeaderItem(31)
        item.setText(_translate("ComodityMonitor", "铜"))
        item = self.tableWidget_2.horizontalHeaderItem(0)
        item.setText(_translate("ComodityMonitor", "最新价格"))
        item = self.tableWidget_2.horizontalHeaderItem(1)
        item.setText(_translate("ComodityMonitor", "ATR"))
        item = self.tableWidget_2.horizontalHeaderItem(2)
        item.setText(_translate("ComodityMonitor", "5日涨幅"))
        item = self.tableWidget_2.horizontalHeaderItem(3)
        item.setText(_translate("ComodityMonitor", "10日涨幅"))
        item = self.tableWidget_2.horizontalHeaderItem(4)
        item.setText(_translate("ComodityMonitor", "30日涨幅"))
        item = self.tableWidget_2.horizontalHeaderItem(5)
        item.setText(_translate("ComodityMonitor", "60日涨幅"))
        item = self.tableWidget_2.horizontalHeaderItem(6)
        item.setText(_translate("ComodityMonitor", "120日涨幅"))
        item = self.tableWidget_2.horizontalHeaderItem(7)
        item.setText(_translate("ComodityMonitor", "RSI 14"))
        item = self.tableWidget_2.horizontalHeaderItem(8)
        item.setText(_translate("ComodityMonitor", "C/MA 5"))
        item = self.tableWidget_2.horizontalHeaderItem(9)
        item.setText(_translate("ComodityMonitor", "C/MA 10"))
        item = self.tableWidget_2.horizontalHeaderItem(10)
        item.setText(_translate("ComodityMonitor", "C/MA 30"))
        item = self.tableWidget_2.horizontalHeaderItem(11)
        item.setText(_translate("ComodityMonitor", "C/MA 60"))
        item = self.tableWidget_2.horizontalHeaderItem(12)
        item.setText(_translate("ComodityMonitor", "C/MA 120"))
        item = self.tableWidget_2.horizontalHeaderItem(13)
        item.setText(_translate("ComodityMonitor", "C/H 5"))
        item = self.tableWidget_2.horizontalHeaderItem(14)
        item.setText(_translate("ComodityMonitor", "C/H 10"))
        item = self.tableWidget_2.horizontalHeaderItem(15)
        item.setText(_translate("ComodityMonitor", "C/H 30"))
        item = self.tableWidget_2.horizontalHeaderItem(16)
        item.setText(_translate("ComodityMonitor", "C/H 60"))
        item = self.tableWidget_2.horizontalHeaderItem(17)
        item.setText(_translate("ComodityMonitor", "C/H 120"))
        item = self.tableWidget_2.horizontalHeaderItem(18)
        item.setText(_translate("ComodityMonitor", "C/L 5"))
        item = self.tableWidget_2.horizontalHeaderItem(19)
        item.setText(_translate("ComodityMonitor", "C/L 10"))
        item = self.tableWidget_2.horizontalHeaderItem(20)
        item.setText(_translate("ComodityMonitor", "C/L 30"))
        item = self.tableWidget_2.horizontalHeaderItem(21)
        item.setText(_translate("ComodityMonitor", "C/L 60"))
        item = self.tableWidget_2.horizontalHeaderItem(22)
        item.setText(_translate("ComodityMonitor", "C/L 120"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("ComodityMonitor", "趋势择时"))
        self.menuAbout.setTitle(_translate("ComodityMonitor", "About"))
        self.actionAbout_Me.setText(_translate("ComodityMonitor", "About Me"))
        self.actionExit.setText(_translate("ComodityMonitor", "Exit"))
        self.actionExit.setShortcut('Ctrl+Q')
        self.actionExit.setStatusTip('退出应用程序')
        self.actionExit.triggered.connect(QtWidgets.qApp.quit)

        self.actionAbout_Me.triggered.connect(self.do_btn25)

    def do_btn25(self, event):  # 消息：关于
        reply = QtWidgets.QMessageBox.about(self.centralwidget, "关于",
                                                "本软件遵循GPL协议，旨在监控商品期货价差和趋势。由于数据来源为新浪接口，所以会有所延迟，敬请见谅。作者：张逸辰，联系方式：ethan@yczhang.cn")

