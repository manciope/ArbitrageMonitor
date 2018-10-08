import _thread
import sys

import cal_func as cf
from ComodityUI import *


def update_tab1(ui):
    def insert_table1(i, min_time, max_time, price1, price2, latest_diff, pre_diff, diff_10, diff_20, diff_30, min_diff,
                      percentile5, mid_diff, percentile95, max_diff):
        ui.tableWidget.setItem(i, 0, QtWidgets.QTableWidgetItem(str(min_time)))
        ui.tableWidget.setItem(i, 1, QtWidgets.QTableWidgetItem(str(max_time)))
        ui.tableWidget.setItem(i, 2, QtWidgets.QTableWidgetItem(str(price1)))
        ui.tableWidget.setItem(i, 3, QtWidgets.QTableWidgetItem(str(price2)))
        if latest_diff <= percentile5 or latest_diff >= percentile95:
            newItem = QtWidgets.QTableWidgetItem(str(latest_diff))
            newItem.setForeground(QtGui.QColor(200, 111, 30))
            ui.tableWidget.setItem(i, 4, newItem)
        else:
            ui.tableWidget.setItem(i, 4, QtWidgets.QTableWidgetItem(str(latest_diff)))
        ui.tableWidget.setItem(i, 5, QtWidgets.QTableWidgetItem(str(pre_diff)))
        ui.tableWidget.setItem(i, 6, QtWidgets.QTableWidgetItem(str(diff_10)))
        ui.tableWidget.setItem(i, 7, QtWidgets.QTableWidgetItem(str(diff_20)))
        ui.tableWidget.setItem(i, 8, QtWidgets.QTableWidgetItem(str(diff_30)))
        ui.tableWidget.setItem(i, 9, QtWidgets.QTableWidgetItem(str(min_diff)))
        ui.tableWidget.setItem(i, 10, QtWidgets.QTableWidgetItem(str(percentile5)))
        ui.tableWidget.setItem(i, 11, QtWidgets.QTableWidgetItem(str(mid_diff)))
        ui.tableWidget.setItem(i, 12, QtWidgets.QTableWidgetItem(str(percentile95)))
        ui.tableWidget.setItem(i, 13, QtWidgets.QTableWidgetItem(str(max_diff)))

    def f0():
        i = 0  # 豆油/豆粕
        min_time, max_time, price1, price2, latest_diff, pre_diff, diff_10, diff_20, diff_30, min_diff, percentile5, mid_diff, percentile95, max_diff = cf.difference(
            'y0', 'm0', method='divide')
        insert_table1(i, min_time, max_time, price1, price2, latest_diff, pre_diff, diff_10, diff_20, diff_30, min_diff,
                      percentile5, mid_diff, percentile95, max_diff)
        # print("y0 and  m0 done")

    def f1():
        i = 1  # 豆粕-菜粕
        min_time, max_time, price1, price2, latest_diff, pre_diff, diff_10, diff_20, diff_30, min_diff, percentile5, mid_diff, percentile95, max_diff = cf.difference(
            'm0', 'rm0', method='minus')
        insert_table1(i, min_time, max_time, price1, price2, latest_diff, pre_diff, diff_10, diff_20, diff_30, min_diff,
                      percentile5, mid_diff, percentile95, max_diff)
        # print("m0 and  rm0 done")

    def f2():
        i = 2  # 豆油-棕榈油
        min_time, max_time, price1, price2, latest_diff, pre_diff, diff_10, diff_20, diff_30, min_diff, percentile5, mid_diff, percentile95, max_diff = cf.difference(
            'y0', 'p0', method='minus')
        insert_table1(i, min_time, max_time, price1, price2, latest_diff, pre_diff, diff_10, diff_20, diff_30, min_diff,
                      percentile5, mid_diff, percentile95, max_diff)
        # print("y0 and  p0 done")

    def f3():
        i = 3  # 菜油-豆油
        min_time, max_time, price1, price2, latest_diff, pre_diff, diff_10, diff_20, diff_30, min_diff, percentile5, mid_diff, percentile95, max_diff = cf.difference(
            'oi0', 'y0', method='minus')
        insert_table1(i, min_time, max_time, price1, price2, latest_diff, pre_diff, diff_10, diff_20, diff_30, min_diff,
                      percentile5, mid_diff, percentile95, max_diff)
        # print("oi0 and  y0 done")

    def f4():
        i = 4  # 菜油-棕榈油
        min_time, max_time, price1, price2, latest_diff, pre_diff, diff_10, diff_20, diff_30, min_diff, percentile5, mid_diff, percentile95, max_diff = cf.difference(
            'oi0', 'p0', method='minus')
        insert_table1(i, min_time, max_time, price1, price2, latest_diff, pre_diff, diff_10, diff_20, diff_30, min_diff,
                      percentile5, mid_diff, percentile95, max_diff)
        # print("oi0 and  p0 done")

    def f5():
        i = 5  # 菜油/菜粕
        min_time, max_time, price1, price2, latest_diff, pre_diff, diff_10, diff_20, diff_30, min_diff, percentile5, mid_diff, percentile95, max_diff = cf.difference(
            'oi0', 'rm0', method='divide')
        insert_table1(i, min_time, max_time, price1, price2, latest_diff, pre_diff, diff_10, diff_20, diff_30, min_diff,
                      percentile5, mid_diff, percentile95, max_diff)
        # print("oi0 and  rm0 done")

    def f6():
        i = 6  # 玉米淀粉-玉米
        min_time, max_time, price1, price2, latest_diff, pre_diff, diff_10, diff_20, diff_30, min_diff, percentile5, mid_diff, percentile95, max_diff = cf.difference(
            'cs0', 'c0', method='minus')
        insert_table1(i, min_time, max_time, price1, price2, latest_diff, pre_diff, diff_10, diff_20, diff_30, min_diff,
                      percentile5, mid_diff, percentile95, max_diff)
        # print("cs0 and  c0 done")

    def f7():
        i = 7  # 螺纹钢-热卷
        min_time, max_time, price1, price2, latest_diff, pre_diff, diff_10, diff_20, diff_30, min_diff, percentile5, mid_diff, percentile95, max_diff = cf.difference(
            'rb0', 'hc0', method='minus')
        insert_table1(i, min_time, max_time, price1, price2, latest_diff, pre_diff, diff_10, diff_20, diff_30, min_diff,
                      percentile5, mid_diff, percentile95, max_diff)
        # print("rb0 and  hc0 done")

    def f8():
        i = 8  # 螺纹钢/铁矿石
        min_time, max_time, price1, price2, latest_diff, pre_diff, diff_10, diff_20, diff_30, min_diff, percentile5, mid_diff, percentile95, max_diff = cf.difference(
            'rb0', 'i0', method='divide')
        insert_table1(i, min_time, max_time, price1, price2, latest_diff, pre_diff, diff_10, diff_20, diff_30, min_diff,
                      percentile5, mid_diff, percentile95, max_diff)
        # print("rb0 and  i0 done")

    def f9():
        i = 9  # 焦炭/焦煤
        min_time, max_time, price1, price2, latest_diff, pre_diff, diff_10, diff_20, diff_30, min_diff, percentile5, mid_diff, percentile95, max_diff = cf.difference(
            'j0', 'jm0', method='divide')
        insert_table1(i, min_time, max_time, price1, price2, latest_diff, pre_diff, diff_10, diff_20, diff_30, min_diff,
                      percentile5, mid_diff, percentile95, max_diff)
        # print("j0 and  jm0 done")

    def f10():
        i = 10  # L-PP
        min_time, max_time, price1, price2, latest_diff, pre_diff, diff_10, diff_20, diff_30, min_diff, percentile5, mid_diff, percentile95, max_diff = cf.difference(
            'l0', 'pp0', method='minus')
        insert_table1(i, min_time, max_time, price1, price2, latest_diff, pre_diff, diff_10, diff_20, diff_30, min_diff,
                      percentile5, mid_diff, percentile95, max_diff)
        # print("l0 and  pp0 done")

    def f11():
        i = 11  # PP-3MA
        min_time, max_time, price1, price2, latest_diff, pre_diff, diff_10, diff_20, diff_30, min_diff, percentile5, mid_diff, percentile95, max_diff = cf.difference(
            'pp0', 'ma0', method='minus', quant2=3)
        insert_table1(i, min_time, max_time, price1, price2, latest_diff, pre_diff, diff_10, diff_20, diff_30, min_diff,
                      percentile5, mid_diff, percentile95, max_diff)
        # print("pp0 and  ma0 done")

    def f12():
        i = 12  # 铝/锌
        min_time, max_time, price1, price2, latest_diff, pre_diff, diff_10, diff_20, diff_30, min_diff, percentile5, mid_diff, percentile95, max_diff = cf.difference(
            'al0', 'zn0', method='divide')
        insert_table1(i, min_time, max_time, price1, price2, latest_diff, pre_diff, diff_10, diff_20, diff_30, min_diff,
                      percentile5, mid_diff, percentile95, max_diff)
        # print("al0 and  zn0 done")

    def f13():
        i = 13  # 铜/锌
        min_time, max_time, price1, price2, latest_diff, pre_diff, diff_10, diff_20, diff_30, min_diff, percentile5, mid_diff, percentile95, max_diff = cf.difference(
            'cu0', 'zn0', method='divide')
        insert_table1(i, min_time, max_time, price1, price2, latest_diff, pre_diff, diff_10, diff_20, diff_30, min_diff,
                      percentile5, mid_diff, percentile95, max_diff)
        # print("cu0 and  zn0 done")

    def f14():
        i = 14  # 金/银
        min_time, max_time, price1, price2, latest_diff, pre_diff, diff_10, diff_20, diff_30, min_diff, percentile5, mid_diff, percentile95, max_diff = cf.difference(
            'au0', 'ag0', method='divide', quant1=15)
        insert_table1(i, min_time, max_time, price1, price2, latest_diff, pre_diff, diff_10, diff_20, diff_30, min_diff,
                      percentile5, mid_diff, percentile95, max_diff)
        # print("au0 and  ag0 done")

    try:
        _thread.start_new_thread(f0, ())
        _thread.start_new_thread(f1, ())
        _thread.start_new_thread(f2, ())
        _thread.start_new_thread(f3, ())
        _thread.start_new_thread(f4, ())
        _thread.start_new_thread(f5, ())
        _thread.start_new_thread(f6, ())
        _thread.start_new_thread(f7, ())
        _thread.start_new_thread(f8, ())
        _thread.start_new_thread(f9, ())
        _thread.start_new_thread(f10, ())
        _thread.start_new_thread(f11, ())
        _thread.start_new_thread(f12, ())
        _thread.start_new_thread(f13, ())
        _thread.start_new_thread(f14, ())

    except:
        pass


def update_tab2(ui):
    def insert_table2(i, price, atr, change5, change10, change30, change60, change120,
                      rsi, cma5, cma10, cma30, cma60, cma120, ch5, ch10, ch30, ch60, ch120, cl5, cl10, cl30, cl60,
                      cl120):
        ui.tableWidget_2.setItem(i, 0, QtWidgets.QTableWidgetItem(str(price)))
        ui.tableWidget_2.setItem(i, 1, QtWidgets.QTableWidgetItem(str(atr)))
        ui.tableWidget_2.setItem(i, 2, QtWidgets.QTableWidgetItem(str(change5)))
        ui.tableWidget_2.setItem(i, 3, QtWidgets.QTableWidgetItem(str(change10)))
        ui.tableWidget_2.setItem(i, 4, QtWidgets.QTableWidgetItem(str(change30)))
        ui.tableWidget_2.setItem(i, 5, QtWidgets.QTableWidgetItem(str(change60)))
        ui.tableWidget_2.setItem(i, 6, QtWidgets.QTableWidgetItem(str(change120)))
        if rsi <= 20 or rsi >= 80:
            newItem = QtWidgets.QTableWidgetItem(str(rsi))
            newItem.setForeground(QtGui.QColor(200, 111, 30))
            ui.tableWidget_2.setItem(i, 7, newItem)
        else:
            ui.tableWidget_2.setItem(i, 7, QtWidgets.QTableWidgetItem(str(rsi)))
        ui.tableWidget_2.setItem(i, 8, QtWidgets.QTableWidgetItem(str(cma5)))
        ui.tableWidget_2.setItem(i, 9, QtWidgets.QTableWidgetItem(str(cma10)))
        ui.tableWidget_2.setItem(i, 10, QtWidgets.QTableWidgetItem(str(cma30)))
        ui.tableWidget_2.setItem(i, 11, QtWidgets.QTableWidgetItem(str(cma60)))
        ui.tableWidget_2.setItem(i, 12, QtWidgets.QTableWidgetItem(str(cma120)))

        if ch5 >= -1:
            newItem = QtWidgets.QTableWidgetItem(str(ch5))
            newItem.setForeground(QtGui.QColor(200, 111, 30))
            ui.tableWidget_2.setItem(i, 13, newItem)
        else:
            ui.tableWidget_2.setItem(i, 13, QtWidgets.QTableWidgetItem(str(ch5)))

        if ch10 >= -1:
            newItem = QtWidgets.QTableWidgetItem(str(ch10))
            newItem.setForeground(QtGui.QColor(200, 111, 30))
            ui.tableWidget_2.setItem(i, 14, newItem)
        else:
            ui.tableWidget_2.setItem(i, 14, QtWidgets.QTableWidgetItem(str(ch10)))

        if ch30 >= -1:
            newItem = QtWidgets.QTableWidgetItem(str(ch30))
            newItem.setForeground(QtGui.QColor(200, 111, 30))
            ui.tableWidget_2.setItem(i, 15, newItem)
        else:
            ui.tableWidget_2.setItem(i, 15, QtWidgets.QTableWidgetItem(str(ch30)))

        if ch60 >= -1:
            newItem = QtWidgets.QTableWidgetItem(str(ch60))
            newItem.setForeground(QtGui.QColor(200, 111, 30))
            ui.tableWidget_2.setItem(i, 16, newItem)
        else:
            ui.tableWidget_2.setItem(i, 16, QtWidgets.QTableWidgetItem(str(ch60)))

        if ch120 >= -1:
            newItem = QtWidgets.QTableWidgetItem(str(ch120))
            newItem.setForeground(QtGui.QColor(200, 111, 30))
            ui.tableWidget_2.setItem(i, 17, newItem)
        else:
            ui.tableWidget_2.setItem(i, 17, QtWidgets.QTableWidgetItem(str(ch120)))

        if cl5 <= 1:
            newItem = QtWidgets.QTableWidgetItem(str(cl5))
            newItem.setForeground(QtGui.QColor(200, 111, 30))
            ui.tableWidget_2.setItem(i, 18, newItem)
        else:
            ui.tableWidget_2.setItem(i, 18, QtWidgets.QTableWidgetItem(str(cl5)))

        if cl10 <= 1:
            newItem = QtWidgets.QTableWidgetItem(str(cl10))
            newItem.setForeground(QtGui.QColor(200, 111, 30))
            ui.tableWidget_2.setItem(i, 19, newItem)
        else:
            ui.tableWidget_2.setItem(i, 19, QtWidgets.QTableWidgetItem(str(cl10)))

        if cl30 <= 1:
            newItem = QtWidgets.QTableWidgetItem(str(cl30))
            newItem.setForeground(QtGui.QColor(200, 111, 30))
            ui.tableWidget_2.setItem(i, 20, newItem)
        else:
            ui.tableWidget_2.setItem(i, 20, QtWidgets.QTableWidgetItem(str(cl30)))

        if cl60 <= 1:
            newItem = QtWidgets.QTableWidgetItem(str(cl60))
            newItem.setForeground(QtGui.QColor(200, 111, 30))
            ui.tableWidget_2.setItem(i, 21, newItem)
        else:
            ui.tableWidget_2.setItem(i, 21, QtWidgets.QTableWidgetItem(str(cl60)))

        if cl120 <= 1:
            newItem = QtWidgets.QTableWidgetItem(str(cl120))
            newItem.setForeground(QtGui.QColor(200, 111, 30))
            ui.tableWidget_2.setItem(i, 22, newItem)
        else:
            ui.tableWidget_2.setItem(i, 22, QtWidgets.QTableWidgetItem(str(cl120)))

    def f0():
        i = 0  # 豆一
        price, atr, change5, change10, change30, change60, change120, rsi, cma5, cma10, \
        cma30, cma60, cma120, ch5, ch10, ch30, ch60, ch120, cl5, cl10, cl30, cl60, cl120 \
            = cf.trend('a0')
        insert_table2(i, price, atr, change5, change10, change30, change60, change120, rsi, cma5, cma10,
                      cma30, cma60, cma120, ch5, ch10, ch30, ch60, ch120, cl5, cl10, cl30, cl60, cl120)
        # print("a0 done")

    def f1():
        i = 1  # 豆油
        price, atr, change5, change10, change30, change60, change120, rsi, cma5, cma10, \
        cma30, cma60, cma120, ch5, ch10, ch30, ch60, ch120, cl5, cl10, cl30, cl60, cl120 \
            = cf.trend('y0')
        insert_table2(i, price, atr, change5, change10, change30, change60, change120, rsi, cma5, cma10,
                      cma30, cma60, cma120, ch5, ch10, ch30, ch60, ch120, cl5, cl10, cl30, cl60, cl120)
        # print("y0 done")

    def f2():
        i = 2  # 豆粕
        price, atr, change5, change10, change30, change60, change120, rsi, cma5, cma10, \
        cma30, cma60, cma120, ch5, ch10, ch30, ch60, ch120, cl5, cl10, cl30, cl60, cl120 \
            = cf.trend('m0')
        insert_table2(i, price, atr, change5, change10, change30, change60, change120, rsi, cma5, cma10,
                      cma30, cma60, cma120, ch5, ch10, ch30, ch60, ch120, cl5, cl10, cl30, cl60, cl120)
        # print("m0 done")

    def f3():
        i = 3  # 菜油
        price, atr, change5, change10, change30, change60, change120, rsi, cma5, cma10, \
        cma30, cma60, cma120, ch5, ch10, ch30, ch60, ch120, cl5, cl10, cl30, cl60, cl120 \
            = cf.trend('oi0')
        insert_table2(i, price, atr, change5, change10, change30, change60, change120, rsi, cma5, cma10,
                      cma30, cma60, cma120, ch5, ch10, ch30, ch60, ch120, cl5, cl10, cl30, cl60, cl120)
        # print("oi0 done")

    def f4():
        i = 4  # 菜粕
        price, atr, change5, change10, change30, change60, change120, rsi, cma5, cma10, \
        cma30, cma60, cma120, ch5, ch10, ch30, ch60, ch120, cl5, cl10, cl30, cl60, cl120 \
            = cf.trend('rm0')
        insert_table2(i, price, atr, change5, change10, change30, change60, change120, rsi, cma5, cma10,
                      cma30, cma60, cma120, ch5, ch10, ch30, ch60, ch120, cl5, cl10, cl30, cl60, cl120)
        # print("rm0 done")

    def f5():
        i = 5  # 棕榈油
        price, atr, change5, change10, change30, change60, change120, rsi, cma5, cma10, \
        cma30, cma60, cma120, ch5, ch10, ch30, ch60, ch120, cl5, cl10, cl30, cl60, cl120 \
            = cf.trend('p0')
        insert_table2(i, price, atr, change5, change10, change30, change60, change120, rsi, cma5, cma10,
                      cma30, cma60, cma120, ch5, ch10, ch30, ch60, ch120, cl5, cl10, cl30, cl60, cl120)
        # print("p0 done")

    def f6():
        i = 6  # 玉米淀粉
        price, atr, change5, change10, change30, change60, change120, rsi, cma5, cma10, \
        cma30, cma60, cma120, ch5, ch10, ch30, ch60, ch120, cl5, cl10, cl30, cl60, cl120 \
            = cf.trend('cs0')
        insert_table2(i, price, atr, change5, change10, change30, change60, change120, rsi, cma5, cma10,
                      cma30, cma60, cma120, ch5, ch10, ch30, ch60, ch120, cl5, cl10, cl30, cl60, cl120)
        # print("cs0 done")

    def f7():
        i = 7  # 玉米
        price, atr, change5, change10, change30, change60, change120, rsi, cma5, cma10, \
        cma30, cma60, cma120, ch5, ch10, ch30, ch60, ch120, cl5, cl10, cl30, cl60, cl120 \
            = cf.trend('c0')
        insert_table2(i, price, atr, change5, change10, change30, change60, change120, rsi, cma5, cma10,
                      cma30, cma60, cma120, ch5, ch10, ch30, ch60, ch120, cl5, cl10, cl30, cl60, cl120)
        # print("c0 done")

    def f8():
        i = 8  # 苹果
        price, atr, change5, change10, change30, change60, change120, rsi, cma5, cma10, \
        cma30, cma60, cma120, ch5, ch10, ch30, ch60, ch120, cl5, cl10, cl30, cl60, cl120 \
            = cf.trend('ap0')
        insert_table2(i, price, atr, change5, change10, change30, change60, change120, rsi, cma5, cma10,
                      cma30, cma60, cma120, ch5, ch10, ch30, ch60, ch120, cl5, cl10, cl30, cl60, cl120)
        # print("ap0 done")

    def f9():
        i = 9  # 白糖
        price, atr, change5, change10, change30, change60, change120, rsi, cma5, cma10, \
        cma30, cma60, cma120, ch5, ch10, ch30, ch60, ch120, cl5, cl10, cl30, cl60, cl120 \
            = cf.trend('sr0')
        insert_table2(i, price, atr, change5, change10, change30, change60, change120, rsi, cma5, cma10,
                      cma30, cma60, cma120, ch5, ch10, ch30, ch60, ch120, cl5, cl10, cl30, cl60, cl120)
        # print("sr0 done")

    def f10():
        i = 10  # 棉花
        price, atr, change5, change10, change30, change60, change120, rsi, cma5, cma10, \
        cma30, cma60, cma120, ch5, ch10, ch30, ch60, ch120, cl5, cl10, cl30, cl60, cl120 \
            = cf.trend('cf0')
        insert_table2(i, price, atr, change5, change10, change30, change60, change120, rsi, cma5, cma10,
                      cma30, cma60, cma120, ch5, ch10, ch30, ch60, ch120, cl5, cl10, cl30, cl60, cl120)
        # print("cf0 done")

    def f11():
        i = 11  # 鸡蛋
        price, atr, change5, change10, change30, change60, change120, rsi, cma5, cma10, \
        cma30, cma60, cma120, ch5, ch10, ch30, ch60, ch120, cl5, cl10, cl30, cl60, cl120 \
            = cf.trend('jd0')
        insert_table2(i, price, atr, change5, change10, change30, change60, change120, rsi, cma5, cma10,
                      cma30, cma60, cma120, ch5, ch10, ch30, ch60, ch120, cl5, cl10, cl30, cl60, cl120)
        # print("jd0 done")

    def f12():
        i = 12  # 橡胶
        price, atr, change5, change10, change30, change60, change120, rsi, cma5, cma10, \
        cma30, cma60, cma120, ch5, ch10, ch30, ch60, ch120, cl5, cl10, cl30, cl60, cl120 \
            = cf.trend('ru0')
        insert_table2(i, price, atr, change5, change10, change30, change60, change120, rsi, cma5, cma10,
                      cma30, cma60, cma120, ch5, ch10, ch30, ch60, ch120, cl5, cl10, cl30, cl60, cl120)
        # print("ru0 done")

    def f13():
        i = 13  # 螺纹
        price, atr, change5, change10, change30, change60, change120, rsi, cma5, cma10, \
        cma30, cma60, cma120, ch5, ch10, ch30, ch60, ch120, cl5, cl10, cl30, cl60, cl120 \
            = cf.trend('rb0')
        insert_table2(i, price, atr, change5, change10, change30, change60, change120, rsi, cma5, cma10,
                      cma30, cma60, cma120, ch5, ch10, ch30, ch60, ch120, cl5, cl10, cl30, cl60, cl120)
        # print("rb0 done")

    def f14():
        i = 14  # 热卷
        price, atr, change5, change10, change30, change60, change120, rsi, cma5, cma10, \
        cma30, cma60, cma120, ch5, ch10, ch30, ch60, ch120, cl5, cl10, cl30, cl60, cl120 \
            = cf.trend('hc0')
        insert_table2(i, price, atr, change5, change10, change30, change60, change120, rsi, cma5, cma10,
                      cma30, cma60, cma120, ch5, ch10, ch30, ch60, ch120, cl5, cl10, cl30, cl60, cl120)
        # print("hc0 done")

    def f15():
        i = 15  # 铁矿石
        price, atr, change5, change10, change30, change60, change120, rsi, cma5, cma10, \
        cma30, cma60, cma120, ch5, ch10, ch30, ch60, ch120, cl5, cl10, cl30, cl60, cl120 \
            = cf.trend('i0')
        insert_table2(i, price, atr, change5, change10, change30, change60, change120, rsi, cma5, cma10,
                      cma30, cma60, cma120, ch5, ch10, ch30, ch60, ch120, cl5, cl10, cl30, cl60, cl120)
        # print("i0 done")

    def f16():
        i = 16  # 焦炭
        price, atr, change5, change10, change30, change60, change120, rsi, cma5, cma10, \
        cma30, cma60, cma120, ch5, ch10, ch30, ch60, ch120, cl5, cl10, cl30, cl60, cl120 \
            = cf.trend('j0')
        insert_table2(i, price, atr, change5, change10, change30, change60, change120, rsi, cma5, cma10,
                      cma30, cma60, cma120, ch5, ch10, ch30, ch60, ch120, cl5, cl10, cl30, cl60, cl120)
        # print("j0 done")

    def f17():
        i = 17  # 焦煤
        price, atr, change5, change10, change30, change60, change120, rsi, cma5, cma10, \
        cma30, cma60, cma120, ch5, ch10, ch30, ch60, ch120, cl5, cl10, cl30, cl60, cl120 \
            = cf.trend('jm0')
        insert_table2(i, price, atr, change5, change10, change30, change60, change120, rsi, cma5, cma10,
                      cma30, cma60, cma120, ch5, ch10, ch30, ch60, ch120, cl5, cl10, cl30, cl60, cl120)
        # print("jm0 done")

    def f18():
        i = 18  # 动力煤
        price, atr, change5, change10, change30, change60, change120, rsi, cma5, cma10, \
        cma30, cma60, cma120, ch5, ch10, ch30, ch60, ch120, cl5, cl10, cl30, cl60, cl120 \
            = cf.trend('zc0')
        insert_table2(i, price, atr, change5, change10, change30, change60, change120, rsi, cma5, cma10,
                      cma30, cma60, cma120, ch5, ch10, ch30, ch60, ch120, cl5, cl10, cl30, cl60, cl120)
        # print("zc0 done")

    def f19():
        i = 19  # 玻璃
        price, atr, change5, change10, change30, change60, change120, rsi, cma5, cma10, \
        cma30, cma60, cma120, ch5, ch10, ch30, ch60, ch120, cl5, cl10, cl30, cl60, cl120 \
            = cf.trend('fg0')
        insert_table2(i, price, atr, change5, change10, change30, change60, change120, rsi, cma5, cma10,
                      cma30, cma60, cma120, ch5, ch10, ch30, ch60, ch120, cl5, cl10, cl30, cl60, cl120)
        # print("fg0 done")

    def f20():
        i = 20  # 硅铁
        price, atr, change5, change10, change30, change60, change120, rsi, cma5, cma10, \
        cma30, cma60, cma120, ch5, ch10, ch30, ch60, ch120, cl5, cl10, cl30, cl60, cl120 \
            = cf.trend('sf0')
        insert_table2(i, price, atr, change5, change10, change30, change60, change120, rsi, cma5, cma10,
                      cma30, cma60, cma120, ch5, ch10, ch30, ch60, ch120, cl5, cl10, cl30, cl60, cl120)
        # print("sf0 done")

    def f21():
        i = 21  # 锰硅
        price, atr, change5, change10, change30, change60, change120, rsi, cma5, cma10, \
        cma30, cma60, cma120, ch5, ch10, ch30, ch60, ch120, cl5, cl10, cl30, cl60, cl120 \
            = cf.trend('sm0')
        insert_table2(i, price, atr, change5, change10, change30, change60, change120, rsi, cma5, cma10,
                      cma30, cma60, cma120, ch5, ch10, ch30, ch60, ch120, cl5, cl10, cl30, cl60, cl120)
        # print("sm0 done")

    def f22():
        i = 22  # 塑料
        price, atr, change5, change10, change30, change60, change120, rsi, cma5, cma10, \
        cma30, cma60, cma120, ch5, ch10, ch30, ch60, ch120, cl5, cl10, cl30, cl60, cl120 \
            = cf.trend('l0')
        insert_table2(i, price, atr, change5, change10, change30, change60, change120, rsi, cma5, cma10,
                      cma30, cma60, cma120, ch5, ch10, ch30, ch60, ch120, cl5, cl10, cl30, cl60, cl120)
        # print("l0 done")

    def f23():
        i = 23  # PVC
        price, atr, change5, change10, change30, change60, change120, rsi, cma5, cma10, \
        cma30, cma60, cma120, ch5, ch10, ch30, ch60, ch120, cl5, cl10, cl30, cl60, cl120 \
            = cf.trend('v0')
        insert_table2(i, price, atr, change5, change10, change30, change60, change120, rsi, cma5, cma10,
                      cma30, cma60, cma120, ch5, ch10, ch30, ch60, ch120, cl5, cl10, cl30, cl60, cl120)
        # print("v0 done")

    def f24():
        i = 24  # 聚丙烯
        price, atr, change5, change10, change30, change60, change120, rsi, cma5, cma10, \
        cma30, cma60, cma120, ch5, ch10, ch30, ch60, ch120, cl5, cl10, cl30, cl60, cl120 \
            = cf.trend('pp0')
        insert_table2(i, price, atr, change5, change10, change30, change60, change120, rsi, cma5, cma10,
                      cma30, cma60, cma120, ch5, ch10, ch30, ch60, ch120, cl5, cl10, cl30, cl60, cl120)
        # print("pp0 done")

    def f25():
        i = 25  # PTA
        price, atr, change5, change10, change30, change60, change120, rsi, cma5, cma10, \
        cma30, cma60, cma120, ch5, ch10, ch30, ch60, ch120, cl5, cl10, cl30, cl60, cl120 \
            = cf.trend('ta0')
        insert_table2(i, price, atr, change5, change10, change30, change60, change120, rsi, cma5, cma10,
                      cma30, cma60, cma120, ch5, ch10, ch30, ch60, ch120, cl5, cl10, cl30, cl60, cl120)
        # print("ta0 done")

    def f26():
        i = 26  # 甲醇
        price, atr, change5, change10, change30, change60, change120, rsi, cma5, cma10, \
        cma30, cma60, cma120, ch5, ch10, ch30, ch60, ch120, cl5, cl10, cl30, cl60, cl120 \
            = cf.trend('ma0')
        insert_table2(i, price, atr, change5, change10, change30, change60, change120, rsi, cma5, cma10,
                      cma30, cma60, cma120, ch5, ch10, ch30, ch60, ch120, cl5, cl10, cl30, cl60, cl120)
        # print("ma0 done")

    def f27():
        i = 27  # 铝
        price, atr, change5, change10, change30, change60, change120, rsi, cma5, cma10, \
        cma30, cma60, cma120, ch5, ch10, ch30, ch60, ch120, cl5, cl10, cl30, cl60, cl120 \
            = cf.trend('al0')
        insert_table2(i, price, atr, change5, change10, change30, change60, change120, rsi, cma5, cma10,
                      cma30, cma60, cma120, ch5, ch10, ch30, ch60, ch120, cl5, cl10, cl30, cl60, cl120)
        # print("al0 done")

    def f28():
        i = 28  # 锌
        price, atr, change5, change10, change30, change60, change120, rsi, cma5, cma10, \
        cma30, cma60, cma120, ch5, ch10, ch30, ch60, ch120, cl5, cl10, cl30, cl60, cl120 \
            = cf.trend('zn0')
        insert_table2(i, price, atr, change5, change10, change30, change60, change120, rsi, cma5, cma10,
                      cma30, cma60, cma120, ch5, ch10, ch30, ch60, ch120, cl5, cl10, cl30, cl60, cl120)
        # print("zn0 done")

    def f29():
        i = 29  # 金
        price, atr, change5, change10, change30, change60, change120, rsi, cma5, cma10, \
        cma30, cma60, cma120, ch5, ch10, ch30, ch60, ch120, cl5, cl10, cl30, cl60, cl120 \
            = cf.trend('au0')
        insert_table2(i, price, atr, change5, change10, change30, change60, change120, rsi, cma5, cma10,
                      cma30, cma60, cma120, ch5, ch10, ch30, ch60, ch120, cl5, cl10, cl30, cl60, cl120)
        # print("au0 done")

    def f30():
        i = 30  # 银
        price, atr, change5, change10, change30, change60, change120, rsi, cma5, cma10, \
        cma30, cma60, cma120, ch5, ch10, ch30, ch60, ch120, cl5, cl10, cl30, cl60, cl120 \
            = cf.trend('ag0')
        insert_table2(i, price, atr, change5, change10, change30, change60, change120, rsi, cma5, cma10,
                      cma30, cma60, cma120, ch5, ch10, ch30, ch60, ch120, cl5, cl10, cl30, cl60, cl120)
        # print("ag0 done")

    def f31():
        i = 31  # 铜
        price, atr, change5, change10, change30, change60, change120, rsi, cma5, cma10, \
        cma30, cma60, cma120, ch5, ch10, ch30, ch60, ch120, cl5, cl10, cl30, cl60, cl120 \
            = cf.trend('cu0')
        insert_table2(i, price, atr, change5, change10, change30, change60, change120, rsi, cma5, cma10,
                      cma30, cma60, cma120, ch5, ch10, ch30, ch60, ch120, cl5, cl10, cl30, cl60, cl120)
        # print("cu0 done")

    try:
        _thread.start_new_thread(f0, ())
        _thread.start_new_thread(f1, ())
        _thread.start_new_thread(f2, ())
        _thread.start_new_thread(f3, ())
        _thread.start_new_thread(f4, ())
        _thread.start_new_thread(f5, ())
        _thread.start_new_thread(f6, ())
        _thread.start_new_thread(f7, ())
        _thread.start_new_thread(f8, ())
        _thread.start_new_thread(f9, ())
        _thread.start_new_thread(f10, ())
        _thread.start_new_thread(f11, ())
        _thread.start_new_thread(f12, ())
        _thread.start_new_thread(f13, ())
        _thread.start_new_thread(f14, ())
        _thread.start_new_thread(f15, ())
        _thread.start_new_thread(f16, ())
        _thread.start_new_thread(f17, ())
        _thread.start_new_thread(f18, ())
        _thread.start_new_thread(f19, ())
        _thread.start_new_thread(f20, ())
        _thread.start_new_thread(f21, ())
        _thread.start_new_thread(f22, ())
        _thread.start_new_thread(f23, ())
        _thread.start_new_thread(f24, ())
        _thread.start_new_thread(f25, ())
        _thread.start_new_thread(f26, ())
        _thread.start_new_thread(f27, ())
        _thread.start_new_thread(f28, ())
        _thread.start_new_thread(f29, ())
        _thread.start_new_thread(f30, ())
        _thread.start_new_thread(f31, ())

    except:
        print("Error: 无法启动线程")


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_ComodityMonitor()
    ui.setupUi(MainWindow)
    update_tab1(ui)
    update_tab2(ui)
    MainWindow.show()
    sys.exit(app.exec_())
