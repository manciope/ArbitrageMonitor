from ArbitrageDemoUI import *
import cal_func as cf
from PyQt5 import QtCore, QtGui, QtWidgets
import _thread
import time
import sys
import numpy as np

def updateUi(ui):

    def f0():
        i = 0  # 豆油/豆粕
        min_time, max_time,price1,price2, latest_diff, pre_diff, min_diff, percentile10, avg_diff, percentile90, max_diff = cf.difference(
            'y0', 'm0', method='divide')
        ui.tableWidget.setItem(i, 0, QtWidgets.QTableWidgetItem(str(min_time)))
        ui.tableWidget.setItem(i, 1, QtWidgets.QTableWidgetItem(str(max_time)))
        ui.tableWidget.setItem(i, 2, QtWidgets.QTableWidgetItem(str(price1)))
        ui.tableWidget.setItem(i, 3, QtWidgets.QTableWidgetItem(str(price2)))
        if latest_diff<=percentile10 or latest_diff>=percentile90:
            newItem=QtWidgets.QTableWidgetItem(str(latest_diff))
            newItem.setForeground(QtGui.QColor(200,111,30))
            ui.tableWidget.setItem(i, 4, newItem)
        else:
            ui.tableWidget.setItem(i, 4, QtWidgets.QTableWidgetItem(str(latest_diff)))
        ui.tableWidget.setItem(i, 5, QtWidgets.QTableWidgetItem(str(pre_diff)))
        ui.tableWidget.setItem(i, 6, QtWidgets.QTableWidgetItem(str(min_diff)))
        ui.tableWidget.setItem(i, 7, QtWidgets.QTableWidgetItem(str(percentile10)))
        ui.tableWidget.setItem(i, 8, QtWidgets.QTableWidgetItem(str(avg_diff)))
        ui.tableWidget.setItem(i, 9, QtWidgets.QTableWidgetItem(str(percentile90)))
        ui.tableWidget.setItem(i, 10, QtWidgets.QTableWidgetItem(str(max_diff)))
        print("y0 and  m0 done")

    def f1():
        i = 1  # 豆粕-菜粕
        min_time, max_time,price1,price2, latest_diff, pre_diff, min_diff, percentile10, avg_diff, percentile90, max_diff = cf.difference(
            'm0', 'rm0', method='minus')
        ui.tableWidget.setItem(i, 0, QtWidgets.QTableWidgetItem(str(min_time)))
        ui.tableWidget.setItem(i, 1, QtWidgets.QTableWidgetItem(str(max_time)))
        ui.tableWidget.setItem(i, 2, QtWidgets.QTableWidgetItem(str(price1)))
        ui.tableWidget.setItem(i, 3, QtWidgets.QTableWidgetItem(str(price2)))
        if latest_diff<=percentile10 or latest_diff>=percentile90:
            newItem=QtWidgets.QTableWidgetItem(str(latest_diff))
            newItem.setForeground(QtGui.QColor(200,111,30))
            ui.tableWidget.setItem(i, 4, newItem)
        else:
            ui.tableWidget.setItem(i, 4, QtWidgets.QTableWidgetItem(str(latest_diff)))
        ui.tableWidget.setItem(i, 5, QtWidgets.QTableWidgetItem(str(pre_diff)))
        ui.tableWidget.setItem(i, 6, QtWidgets.QTableWidgetItem(str(min_diff)))
        ui.tableWidget.setItem(i, 7, QtWidgets.QTableWidgetItem(str(percentile10)))
        ui.tableWidget.setItem(i, 8, QtWidgets.QTableWidgetItem(str(avg_diff)))
        ui.tableWidget.setItem(i, 9, QtWidgets.QTableWidgetItem(str(percentile90)))
        ui.tableWidget.setItem(i, 10, QtWidgets.QTableWidgetItem(str(max_diff)))
        print("m0 and  rm0 done")

    def f2():
        i = 2  # 豆油-棕榈油
        min_time, max_time,price1,price2, latest_diff, pre_diff, min_diff, percentile10, avg_diff, percentile90, max_diff = cf.difference(
            'y0', 'p0', method='minus')
        ui.tableWidget.setItem(i, 0, QtWidgets.QTableWidgetItem(str(min_time)))
        ui.tableWidget.setItem(i, 1, QtWidgets.QTableWidgetItem(str(max_time)))
        ui.tableWidget.setItem(i, 2, QtWidgets.QTableWidgetItem(str(price1)))
        ui.tableWidget.setItem(i, 3, QtWidgets.QTableWidgetItem(str(price2)))
        if latest_diff<=percentile10 or latest_diff>=percentile90:
            newItem=QtWidgets.QTableWidgetItem(str(latest_diff))
            newItem.setForeground(QtGui.QColor(200,111,30))
            ui.tableWidget.setItem(i, 4, newItem)
        else:
            ui.tableWidget.setItem(i, 4, QtWidgets.QTableWidgetItem(str(latest_diff)))
        ui.tableWidget.setItem(i, 5, QtWidgets.QTableWidgetItem(str(pre_diff)))
        ui.tableWidget.setItem(i, 6, QtWidgets.QTableWidgetItem(str(min_diff)))
        ui.tableWidget.setItem(i, 7, QtWidgets.QTableWidgetItem(str(percentile10)))
        ui.tableWidget.setItem(i, 8, QtWidgets.QTableWidgetItem(str(avg_diff)))
        ui.tableWidget.setItem(i, 9, QtWidgets.QTableWidgetItem(str(percentile90)))
        ui.tableWidget.setItem(i, 10, QtWidgets.QTableWidgetItem(str(max_diff)))
        print("y0 and  p0 done")

    def f3():
        i = 3  # 菜油-豆油
        min_time, max_time,price1,price2, latest_diff, pre_diff, min_diff, percentile10, avg_diff, percentile90, max_diff = cf.difference(
            'oi0', 'y0', method='minus')
        ui.tableWidget.setItem(i, 0, QtWidgets.QTableWidgetItem(str(min_time)))
        ui.tableWidget.setItem(i, 1, QtWidgets.QTableWidgetItem(str(max_time)))
        ui.tableWidget.setItem(i, 2, QtWidgets.QTableWidgetItem(str(price1)))
        ui.tableWidget.setItem(i, 3, QtWidgets.QTableWidgetItem(str(price2)))
        if latest_diff<=percentile10 or latest_diff>=percentile90:
            newItem=QtWidgets.QTableWidgetItem(str(latest_diff))
            newItem.setForeground(QtGui.QColor(200,111,30))
            ui.tableWidget.setItem(i, 4, newItem)
        else:
            ui.tableWidget.setItem(i, 4, QtWidgets.QTableWidgetItem(str(latest_diff)))
        ui.tableWidget.setItem(i, 5, QtWidgets.QTableWidgetItem(str(pre_diff)))
        ui.tableWidget.setItem(i, 6, QtWidgets.QTableWidgetItem(str(min_diff)))
        ui.tableWidget.setItem(i, 7, QtWidgets.QTableWidgetItem(str(percentile10)))
        ui.tableWidget.setItem(i, 8, QtWidgets.QTableWidgetItem(str(avg_diff)))
        ui.tableWidget.setItem(i, 9, QtWidgets.QTableWidgetItem(str(percentile90)))
        ui.tableWidget.setItem(i, 10, QtWidgets.QTableWidgetItem(str(max_diff)))
        print("oi0 and  y0 done")

    def f4():
        i = 4  # 菜油-棕榈油
        min_time, max_time,price1,price2, latest_diff, pre_diff, min_diff, percentile10, avg_diff, percentile90, max_diff = cf.difference(
            'oi0', 'p0', method='minus')
        ui.tableWidget.setItem(i, 0, QtWidgets.QTableWidgetItem(str(min_time)))
        ui.tableWidget.setItem(i, 1, QtWidgets.QTableWidgetItem(str(max_time)))
        ui.tableWidget.setItem(i, 2, QtWidgets.QTableWidgetItem(str(price1)))
        ui.tableWidget.setItem(i, 3, QtWidgets.QTableWidgetItem(str(price2)))
        if latest_diff<=percentile10 or latest_diff>=percentile90:
            newItem=QtWidgets.QTableWidgetItem(str(latest_diff))
            newItem.setForeground(QtGui.QColor(200,111,30))
            ui.tableWidget.setItem(i, 4, newItem)
        else:
            ui.tableWidget.setItem(i, 4, QtWidgets.QTableWidgetItem(str(latest_diff)))
        ui.tableWidget.setItem(i, 5, QtWidgets.QTableWidgetItem(str(pre_diff)))
        ui.tableWidget.setItem(i, 6, QtWidgets.QTableWidgetItem(str(min_diff)))
        ui.tableWidget.setItem(i, 7, QtWidgets.QTableWidgetItem(str(percentile10)))
        ui.tableWidget.setItem(i, 8, QtWidgets.QTableWidgetItem(str(avg_diff)))
        ui.tableWidget.setItem(i, 9, QtWidgets.QTableWidgetItem(str(percentile90)))
        ui.tableWidget.setItem(i, 10, QtWidgets.QTableWidgetItem(str(max_diff)))
        print("oi0 and  p0 done")

    def f5():
        i = 5  # 菜油/菜粕
        min_time, max_time,price1,price2, latest_diff, pre_diff, min_diff, percentile10, avg_diff, percentile90, max_diff = cf.difference(
            'oi0', 'rm0', method='divide')
        ui.tableWidget.setItem(i, 0, QtWidgets.QTableWidgetItem(str(min_time)))
        ui.tableWidget.setItem(i, 1, QtWidgets.QTableWidgetItem(str(max_time)))
        ui.tableWidget.setItem(i, 2, QtWidgets.QTableWidgetItem(str(price1)))
        ui.tableWidget.setItem(i, 3, QtWidgets.QTableWidgetItem(str(price2)))
        if latest_diff<=percentile10 or latest_diff>=percentile90:
            newItem=QtWidgets.QTableWidgetItem(str(latest_diff))
            newItem.setForeground(QtGui.QColor(200,111,30))
            ui.tableWidget.setItem(i, 4, newItem)
        else:
            ui.tableWidget.setItem(i, 4, QtWidgets.QTableWidgetItem(str(latest_diff)))
        ui.tableWidget.setItem(i, 5, QtWidgets.QTableWidgetItem(str(pre_diff)))
        ui.tableWidget.setItem(i, 6, QtWidgets.QTableWidgetItem(str(min_diff)))
        ui.tableWidget.setItem(i, 7, QtWidgets.QTableWidgetItem(str(percentile10)))
        ui.tableWidget.setItem(i, 8, QtWidgets.QTableWidgetItem(str(avg_diff)))
        ui.tableWidget.setItem(i, 9, QtWidgets.QTableWidgetItem(str(percentile90)))
        ui.tableWidget.setItem(i, 10, QtWidgets.QTableWidgetItem(str(max_diff)))
        print("oi0 and  rm0 done")

    def f6():
        i = 6  # 玉米淀粉-玉米
        min_time, max_time,price1,price2, latest_diff, pre_diff, min_diff, percentile10, avg_diff, percentile90, max_diff = cf.difference(
            'cs0', 'c0', method='minus')
        ui.tableWidget.setItem(i, 0, QtWidgets.QTableWidgetItem(str(min_time)))
        ui.tableWidget.setItem(i, 1, QtWidgets.QTableWidgetItem(str(max_time)))
        ui.tableWidget.setItem(i, 2, QtWidgets.QTableWidgetItem(str(price1)))
        ui.tableWidget.setItem(i, 3, QtWidgets.QTableWidgetItem(str(price2)))
        if latest_diff<=percentile10 or latest_diff>=percentile90:
            newItem=QtWidgets.QTableWidgetItem(str(latest_diff))
            newItem.setForeground(QtGui.QColor(200,111,30))
            ui.tableWidget.setItem(i, 4, newItem)
        else:
            ui.tableWidget.setItem(i, 4, QtWidgets.QTableWidgetItem(str(latest_diff)))
        ui.tableWidget.setItem(i, 5, QtWidgets.QTableWidgetItem(str(pre_diff)))
        ui.tableWidget.setItem(i, 6, QtWidgets.QTableWidgetItem(str(min_diff)))
        ui.tableWidget.setItem(i, 7, QtWidgets.QTableWidgetItem(str(percentile10)))
        ui.tableWidget.setItem(i, 8, QtWidgets.QTableWidgetItem(str(avg_diff)))
        ui.tableWidget.setItem(i, 9, QtWidgets.QTableWidgetItem(str(percentile90)))
        ui.tableWidget.setItem(i, 10, QtWidgets.QTableWidgetItem(str(max_diff)))
        print("cs0 and  c0 done")

    def f7():
        i = 7  # 螺纹钢-热卷
        min_time, max_time,price1,price2, latest_diff, pre_diff, min_diff, percentile10, avg_diff, percentile90, max_diff = cf.difference(
            'rb0', 'hc0', method='minus')
        ui.tableWidget.setItem(i, 0, QtWidgets.QTableWidgetItem(str(min_time)))
        ui.tableWidget.setItem(i, 1, QtWidgets.QTableWidgetItem(str(max_time)))
        ui.tableWidget.setItem(i, 2, QtWidgets.QTableWidgetItem(str(price1)))
        ui.tableWidget.setItem(i, 3, QtWidgets.QTableWidgetItem(str(price2)))
        if latest_diff<=percentile10 or latest_diff>=percentile90:
            newItem=QtWidgets.QTableWidgetItem(str(latest_diff))
            newItem.setForeground(QtGui.QColor(200,111,30))
            ui.tableWidget.setItem(i, 4, newItem)
        else:
            ui.tableWidget.setItem(i, 4, QtWidgets.QTableWidgetItem(str(latest_diff)))
        ui.tableWidget.setItem(i, 5, QtWidgets.QTableWidgetItem(str(pre_diff)))
        ui.tableWidget.setItem(i, 6, QtWidgets.QTableWidgetItem(str(min_diff)))
        ui.tableWidget.setItem(i, 7, QtWidgets.QTableWidgetItem(str(percentile10)))
        ui.tableWidget.setItem(i, 8, QtWidgets.QTableWidgetItem(str(avg_diff)))
        ui.tableWidget.setItem(i, 9, QtWidgets.QTableWidgetItem(str(percentile90)))
        ui.tableWidget.setItem(i, 10, QtWidgets.QTableWidgetItem(str(max_diff)))
        print("rb0 and  hc0 done")

    def f8():
        i = 8  # 螺纹钢/铁矿石
        min_time, max_time,price1,price2, latest_diff, pre_diff, min_diff, percentile10, avg_diff, percentile90, max_diff = cf.difference(
            'rb0', 'i0', method='divide')
        ui.tableWidget.setItem(i, 0, QtWidgets.QTableWidgetItem(str(min_time)))
        ui.tableWidget.setItem(i, 1, QtWidgets.QTableWidgetItem(str(max_time)))
        ui.tableWidget.setItem(i, 2, QtWidgets.QTableWidgetItem(str(price1)))
        ui.tableWidget.setItem(i, 3, QtWidgets.QTableWidgetItem(str(price2)))
        if latest_diff<=percentile10 or latest_diff>=percentile90:
            newItem=QtWidgets.QTableWidgetItem(str(latest_diff))
            newItem.setForeground(QtGui.QColor(200,111,30))
            ui.tableWidget.setItem(i, 4, newItem)
        else:
            ui.tableWidget.setItem(i, 4, QtWidgets.QTableWidgetItem(str(latest_diff)))
        ui.tableWidget.setItem(i, 5, QtWidgets.QTableWidgetItem(str(pre_diff)))
        ui.tableWidget.setItem(i, 6, QtWidgets.QTableWidgetItem(str(min_diff)))
        ui.tableWidget.setItem(i, 7, QtWidgets.QTableWidgetItem(str(percentile10)))
        ui.tableWidget.setItem(i, 8, QtWidgets.QTableWidgetItem(str(avg_diff)))
        ui.tableWidget.setItem(i, 9, QtWidgets.QTableWidgetItem(str(percentile90)))
        ui.tableWidget.setItem(i, 10, QtWidgets.QTableWidgetItem(str(max_diff)))
        print("rb0 and  i0 done")

    def f9():
        i = 9  # 焦炭/焦煤
        min_time, max_time,price1,price2, latest_diff, pre_diff, min_diff, percentile10, avg_diff, percentile90, max_diff = cf.difference(
            'j0', 'jm0', method='divide')
        ui.tableWidget.setItem(i, 0, QtWidgets.QTableWidgetItem(str(min_time)))
        ui.tableWidget.setItem(i, 1, QtWidgets.QTableWidgetItem(str(max_time)))
        ui.tableWidget.setItem(i, 2, QtWidgets.QTableWidgetItem(str(price1)))
        ui.tableWidget.setItem(i, 3, QtWidgets.QTableWidgetItem(str(price2)))
        if latest_diff<=percentile10 or latest_diff>=percentile90:
            newItem=QtWidgets.QTableWidgetItem(str(latest_diff))
            newItem.setForeground(QtGui.QColor(200,111,30))
            ui.tableWidget.setItem(i, 4, newItem)
        else:
            ui.tableWidget.setItem(i, 4, QtWidgets.QTableWidgetItem(str(latest_diff)))
        ui.tableWidget.setItem(i, 5, QtWidgets.QTableWidgetItem(str(pre_diff)))
        ui.tableWidget.setItem(i, 6, QtWidgets.QTableWidgetItem(str(min_diff)))
        ui.tableWidget.setItem(i, 7, QtWidgets.QTableWidgetItem(str(percentile10)))
        ui.tableWidget.setItem(i, 8, QtWidgets.QTableWidgetItem(str(avg_diff)))
        ui.tableWidget.setItem(i, 9, QtWidgets.QTableWidgetItem(str(percentile90)))
        ui.tableWidget.setItem(i, 10, QtWidgets.QTableWidgetItem(str(max_diff)))
        print("j0 and  jm0 done")

    def f10():
        i = 10  # L-PP
        min_time, max_time,price1,price2, latest_diff, pre_diff, min_diff, percentile10, avg_diff, percentile90, max_diff = cf.difference(
            'l0', 'pp0', method='minus')
        ui.tableWidget.setItem(i, 0, QtWidgets.QTableWidgetItem(str(min_time)))
        ui.tableWidget.setItem(i, 1, QtWidgets.QTableWidgetItem(str(max_time)))
        ui.tableWidget.setItem(i, 2, QtWidgets.QTableWidgetItem(str(price1)))
        ui.tableWidget.setItem(i, 3, QtWidgets.QTableWidgetItem(str(price2)))
        if latest_diff<=percentile10 or latest_diff>=percentile90:
            newItem=QtWidgets.QTableWidgetItem(str(latest_diff))
            newItem.setForeground(QtGui.QColor(200,111,30))
            ui.tableWidget.setItem(i, 4, newItem)
        else:
            ui.tableWidget.setItem(i, 4, QtWidgets.QTableWidgetItem(str(latest_diff)))
        ui.tableWidget.setItem(i, 5, QtWidgets.QTableWidgetItem(str(pre_diff)))
        ui.tableWidget.setItem(i, 6, QtWidgets.QTableWidgetItem(str(min_diff)))
        ui.tableWidget.setItem(i, 7, QtWidgets.QTableWidgetItem(str(percentile10)))
        ui.tableWidget.setItem(i, 8, QtWidgets.QTableWidgetItem(str(avg_diff)))
        ui.tableWidget.setItem(i, 9, QtWidgets.QTableWidgetItem(str(percentile90)))
        ui.tableWidget.setItem(i, 10, QtWidgets.QTableWidgetItem(str(max_diff)))
        print("l0 and  pp0 done")

    def f11():
        i = 11  # PP-3MA
        min_time, max_time, price1, price2, latest_diff, pre_diff, min_diff, percentile10, avg_diff, percentile90, max_diff = cf.difference(
            'pp0', 'ma0', method='minus', quant2=3)
        ui.tableWidget.setItem(i, 0, QtWidgets.QTableWidgetItem(str(min_time)))
        ui.tableWidget.setItem(i, 1, QtWidgets.QTableWidgetItem(str(max_time)))
        ui.tableWidget.setItem(i, 2, QtWidgets.QTableWidgetItem(str(price1)))
        ui.tableWidget.setItem(i, 3, QtWidgets.QTableWidgetItem(str(price2)))
        if latest_diff<=percentile10 or latest_diff>=percentile90:
            newItem=QtWidgets.QTableWidgetItem(str(latest_diff))
            newItem.setForeground(QtGui.QColor(200,111,30))
            ui.tableWidget.setItem(i, 4, newItem)
        else:
            ui.tableWidget.setItem(i, 4, QtWidgets.QTableWidgetItem(str(latest_diff)))
        ui.tableWidget.setItem(i, 5, QtWidgets.QTableWidgetItem(str(pre_diff)))
        ui.tableWidget.setItem(i, 6, QtWidgets.QTableWidgetItem(str(min_diff)))
        ui.tableWidget.setItem(i, 7, QtWidgets.QTableWidgetItem(str(percentile10)))
        ui.tableWidget.setItem(i, 8, QtWidgets.QTableWidgetItem(str(avg_diff)))
        ui.tableWidget.setItem(i, 9, QtWidgets.QTableWidgetItem(str(percentile90)))
        ui.tableWidget.setItem(i, 10, QtWidgets.QTableWidgetItem(str(max_diff)))
        print("pp0 and  ma0 done")

    def f12():
        i = 12  # 铝/锌
        min_time, max_time,price1,price2, latest_diff, pre_diff, min_diff, percentile10, avg_diff, percentile90, max_diff = cf.difference(
            'al0', 'zn0', method='divide')
        ui.tableWidget.setItem(i, 0, QtWidgets.QTableWidgetItem(str(min_time)))
        ui.tableWidget.setItem(i, 1, QtWidgets.QTableWidgetItem(str(max_time)))
        ui.tableWidget.setItem(i, 2, QtWidgets.QTableWidgetItem(str(price1)))
        ui.tableWidget.setItem(i, 3, QtWidgets.QTableWidgetItem(str(price2)))
        if latest_diff<=percentile10 or latest_diff>=percentile90:
            newItem=QtWidgets.QTableWidgetItem(str(latest_diff))
            newItem.setForeground(QtGui.QColor(200,111,30))
            ui.tableWidget.setItem(i, 4, newItem)
        else:
            ui.tableWidget.setItem(i, 4, QtWidgets.QTableWidgetItem(str(latest_diff)))
        ui.tableWidget.setItem(i, 5, QtWidgets.QTableWidgetItem(str(pre_diff)))
        ui.tableWidget.setItem(i, 6, QtWidgets.QTableWidgetItem(str(min_diff)))
        ui.tableWidget.setItem(i, 7, QtWidgets.QTableWidgetItem(str(percentile10)))
        ui.tableWidget.setItem(i, 8, QtWidgets.QTableWidgetItem(str(avg_diff)))
        ui.tableWidget.setItem(i, 9, QtWidgets.QTableWidgetItem(str(percentile90)))
        ui.tableWidget.setItem(i, 10, QtWidgets.QTableWidgetItem(str(max_diff)))
        print("al0 and  zn0 done")

    def f13():
        i = 13  # 铜/锌
        min_time, max_time,price1,price2, latest_diff, pre_diff, min_diff, percentile10, avg_diff, percentile90, max_diff = cf.difference(
            'cu0', 'zn0', method='divide')
        ui.tableWidget.setItem(i, 0, QtWidgets.QTableWidgetItem(str(min_time)))
        ui.tableWidget.setItem(i, 1, QtWidgets.QTableWidgetItem(str(max_time)))
        ui.tableWidget.setItem(i, 2, QtWidgets.QTableWidgetItem(str(price1)))
        ui.tableWidget.setItem(i, 3, QtWidgets.QTableWidgetItem(str(price2)))
        if latest_diff<=percentile10 or latest_diff>=percentile90:
            newItem=QtWidgets.QTableWidgetItem(str(latest_diff))
            newItem.setForeground(QtGui.QColor(200,111,30))
            ui.tableWidget.setItem(i, 4, newItem)
        else:
            ui.tableWidget.setItem(i, 4, QtWidgets.QTableWidgetItem(str(latest_diff)))
        ui.tableWidget.setItem(i, 5, QtWidgets.QTableWidgetItem(str(pre_diff)))
        ui.tableWidget.setItem(i, 6, QtWidgets.QTableWidgetItem(str(min_diff)))
        ui.tableWidget.setItem(i, 7, QtWidgets.QTableWidgetItem(str(percentile10)))
        ui.tableWidget.setItem(i, 8, QtWidgets.QTableWidgetItem(str(avg_diff)))
        ui.tableWidget.setItem(i, 9, QtWidgets.QTableWidgetItem(str(percentile90)))
        ui.tableWidget.setItem(i, 10, QtWidgets.QTableWidgetItem(str(max_diff)))
        print("cu0 and  zn0 done")

    def f14():
        i = 14  # 金/银
        min_time, max_time,price1,price2, latest_diff, pre_diff, min_diff, percentile10, avg_diff, percentile90, max_diff = cf.difference(
            'au0', 'ag0', method='divide',quant1=15)
        ui.tableWidget.setItem(i, 0, QtWidgets.QTableWidgetItem(str(min_time)))
        ui.tableWidget.setItem(i, 1, QtWidgets.QTableWidgetItem(str(max_time)))
        ui.tableWidget.setItem(i, 2, QtWidgets.QTableWidgetItem(str(price1)))
        ui.tableWidget.setItem(i, 3, QtWidgets.QTableWidgetItem(str(price2)))
        if latest_diff<=percentile10 or latest_diff>=percentile90:
            newItem=QtWidgets.QTableWidgetItem(str(latest_diff))
            newItem.setForeground(QtGui.QColor(200,111,30))
            ui.tableWidget.setItem(i, 4, newItem)
        else:
            ui.tableWidget.setItem(i, 4, QtWidgets.QTableWidgetItem(str(latest_diff)))
        ui.tableWidget.setItem(i, 5, QtWidgets.QTableWidgetItem(str(pre_diff)))
        ui.tableWidget.setItem(i, 6, QtWidgets.QTableWidgetItem(str(min_diff)))
        ui.tableWidget.setItem(i, 7, QtWidgets.QTableWidgetItem(str(percentile10)))
        ui.tableWidget.setItem(i, 8, QtWidgets.QTableWidgetItem(str(avg_diff)))
        ui.tableWidget.setItem(i, 9, QtWidgets.QTableWidgetItem(str(percentile90)))
        ui.tableWidget.setItem(i, 10, QtWidgets.QTableWidgetItem(str(max_diff)))
        print("au0 and  ag0 done")

    try:
        _thread.start_new_thread(f0,())
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
        print("Error: 无法启动线程")

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_ArbitrageMonitor()

    ui.setupUi(MainWindow)
    updateUi(ui)
    time.sleep(12)
    MainWindow.show()

    sys.exit(app.exec_())
