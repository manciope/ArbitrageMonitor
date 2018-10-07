import datetime
import urllib.request

import numpy as np
import pandas as pd
import talib


def fetch_data(symbol, interval='Daily'):
    if interval == 'Daily':
        url = r'http://stock2.finance.sina.com.cn/futures/api/json.php/IndexService.getInnerFuturesDailyKLine?symbol=' + symbol
    elif interval == '5m':
        url = r'http://stock2.finance.sina.com.cn/futures/api/json.php/IndexService.getInnerFuturesMiniKLine5m?symbol=' + symbol
    elif interval == '30m':
        url = r'http://stock2.finance.sina.com.cn/futures/api/json.php/IndexService.getInnerFuturesMiniKLine30m?symbol=' + symbol
    elif interval == '60m':
        url = r'http://stock2.finance.sina.com.cn/futures/api/json.php/IndexService.getInnerFuturesMiniKLine30m?symbol=' + symbol
    try:
        res = urllib.request.urlopen(url)
    except:
        pass
    html = res.read()
    temp = pd.read_json(html)
    temp.columns = ['time', 'open', 'high', 'low', 'close', 'volumn']
    temp.sort_values(by='time', inplace=True)
    temp = temp.reset_index(drop=True)
    return temp


def difference(symbol1, symbol2, threshold='2018-01-01', method='minus', quant1=1, quant2=1):
    temp1 = fetch_data(symbol1)
    temp2 = fetch_data(symbol2)
    temp1.time = pd.to_datetime(temp1.time)
    temp2.time = pd.to_datetime(temp2.time)
    threshold = datetime.datetime.strptime(threshold, "%Y-%m-%d")
    del_temp1 = pd.DataFrame(temp1.time < threshold)
    del_temp1 = del_temp1[del_temp1['time'] == True].index
    temp1.drop(del_temp1, inplace=True)
    temp1 = temp1.reset_index(drop=True)
    del_temp2 = pd.DataFrame(temp2.time < threshold)
    del_temp2 = del_temp2[del_temp2['time'] == True].index
    temp2.drop(del_temp2, inplace=True)
    temp2 = temp2.reset_index(drop=True)

    if method == 'minus':
        result = pd.DataFrame(temp1['close'] * quant1 - temp2['close'] * quant2)
    elif method == 'divide':
        result = pd.DataFrame(temp1['close'] * quant1 / (temp2['close'] * quant2))
    result['time'] = temp1['time']

    price1 = round(temp1.close[len(result) - 1], 2)
    price2 = round(temp2.close[len(result) - 1], 2)
    latesest_diff = round(result.close[len(result) - 1], 2)
    pre_diff = round(result.close[len(result) - 2], 2)
    diff_10 = round(result.close[len(result) - 11], 2)
    diff_20 = round(result.close[len(result) - 21], 2)
    diff_30 = round(result.close[len(result) - 31], 2)
    min_time = result.time[0].strftime("%Y-%m-%d")
    max_time = result.time[len(result) - 1].strftime("%Y-%m-%d")

    avg_diff = round(np.mean(result.close), 2)

    min_diff = round(np.min(result.close), 2)
    percentile5 = round(np.percentile(result.close, 5), 2)
    percentile95 = round(np.percentile(result.close, 95), 2)
    max_diff = round(np.max(result.close), 2)

    # print("handling "+ symbol1 +" and "+symbol2)
    return min_time, max_time, price1, price2, latesest_diff, pre_diff, diff_10, diff_20, diff_30, min_diff, percentile5, avg_diff, percentile95, max_diff


def trend(symbol, threshold='2018-01-01'):
    temp = fetch_data(symbol)
    temp.time = pd.to_datetime(temp.time)
    threshold = datetime.datetime.strptime(threshold, "%Y-%m-%d")
    del_temp = pd.DataFrame(temp.time < threshold)
    del_temp = del_temp[del_temp['time'] == True].index
    temp.drop(del_temp, inplace=True)
    temp = temp.reset_index(drop=True)

    try:
        temp['atr'] = round(talib.ATR(temp['high'], temp['low'], temp['close'], timeperiod=20), 2)
        temp['change5'] = round(talib.ROC(temp['close'], timeperiod=5), 2)
        temp['change10'] = round(talib.ROC(temp['close'], timeperiod=10), 2)
        temp['change30'] = round(talib.ROC(temp['close'], timeperiod=30), 2)
        temp['change60'] = round(talib.ROC(temp['close'], timeperiod=60), 2)
        temp['change120'] = round(talib.ROC(temp['close'], timeperiod=120), 2)
        temp['rsi'] = round(talib.RSI(temp['close'], timeperiod=14), 2)
        temp['cma5'] = round((np.divide(temp['close'], talib.MA(temp['close'], timeperiod=5)) - 1) * 100, 2)
        temp['cma10'] = round((np.divide(temp['close'], talib.MA(temp['close'], timeperiod=10)) - 1) * 100, 2)
        temp['cma30'] = round((np.divide(temp['close'], talib.MA(temp['close'], timeperiod=30)) - 1) * 100, 2)
        temp['cma60'] = round((np.divide(temp['close'], talib.MA(temp['close'], timeperiod=60)) - 1) * 100, 2)
        temp['cma120'] = round((np.divide(temp['close'], talib.MA(temp['close'], timeperiod=120)) - 1) * 100, 2)
        temp['ch5'] = round((np.divide(temp['close'], talib.MAX(temp['high'], timeperiod=5)) - 1) * 100, 2)
        temp['ch10'] = round((np.divide(temp['close'], talib.MAX(temp['high'], timeperiod=10)) - 1) * 100, 2)
        temp['ch30'] = round((np.divide(temp['close'], talib.MAX(temp['high'], timeperiod=30)) - 1) * 100, 2)
        temp['ch60'] = round((np.divide(temp['close'], talib.MAX(temp['high'], timeperiod=60)) - 1) * 100, 2)
        temp['ch120'] = round((np.divide(temp['close'], talib.MAX(temp['high'], timeperiod=120)) - 1) * 100, 2)
        temp['cl5'] = round((np.divide(temp['close'], talib.MIN(temp['low'], timeperiod=5)) - 1) * 100, 2)
        temp['cl10'] = round((np.divide(temp['close'], talib.MIN(temp['low'], timeperiod=10)) - 1) * 100, 2)
        temp['cl30'] = round((np.divide(temp['close'], talib.MIN(temp['low'], timeperiod=30)) - 1) * 100, 2)
        temp['cl60'] = round((np.divide(temp['close'], talib.MIN(temp['low'], timeperiod=60)) - 1) * 100, 2)
        temp['cl120'] = round((np.divide(temp['close'], talib.MIN(temp['low'], timeperiod=120)) - 1) * 100, 2)
    except:
        pass

    return temp.iloc[len(temp) - 1, :][
        ['close', 'atr', 'change5', 'change10', 'change30', 'change60', 'change120', 'rsi', 'cma5', 'cma10', 'cma30',
         'cma60', 'cma120' \
            , 'ch5', 'ch10', 'ch30', 'ch60', 'ch120', 'cl5', 'cl10', 'cl30', 'cl60', 'cl120']]
