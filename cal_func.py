import urllib.request
import pandas as pd
import numpy as np
import datetime


def fetch_data(symbol,interval='Daily'):
    if interval=='Daily':
        url = r'http://stock2.finance.sina.com.cn/futures/api/json.php/IndexService.getInnerFuturesDailyKLine?symbol='+symbol
    elif interval=='5m':
        url = r'http://stock2.finance.sina.com.cn/futures/api/json.php/IndexService.getInnerFuturesMiniKLine5m?symbol=' + symbol
    elif interval=='30m':
        url = r'http://stock2.finance.sina.com.cn/futures/api/json.php/IndexService.getInnerFuturesMiniKLine30m?symbol=' + symbol
    elif interval=='60m':
        url = r'http://stock2.finance.sina.com.cn/futures/api/json.php/IndexService.getInnerFuturesMiniKLine30m?symbol=' + symbol
    res = urllib.request.urlopen(url)
    html = res.read().decode('utf-8')

    temp=pd.read_json(html)
    temp.columns=['time','open','high','low','close','volumn']
    temp.sort_values(by='time',inplace= True)
    temp=temp.reset_index(drop=True)
    return temp

def difference(symbol1,symbol2,threshold='2018-01-01', method='minus',quant1=1,quant2=1):
    temp1=fetch_data(symbol1)
    temp2=fetch_data(symbol2)
    temp1.time=pd.to_datetime(temp1.time)
    temp2.time = pd.to_datetime(temp2.time)
    threshold=datetime.datetime.strptime(threshold,"%Y-%m-%d")
    del_temp1=pd.DataFrame(temp1.time<threshold)
    del_temp1 = del_temp1[del_temp1['time'] == True].index
    temp1.drop(del_temp1,inplace=True)
    temp1 = temp1.reset_index(drop=True)
    del_temp2=pd.DataFrame(temp2.time<threshold)
    del_temp2 = del_temp2[del_temp2['time'] == True].index
    temp2.drop(del_temp2,inplace=True)
    temp2 = temp2.reset_index(drop=True)

    if method=='minus':
        result=pd.DataFrame(temp1['close']*quant1-temp2['close']*quant2)
    elif method=='divide':
        result = pd.DataFrame(temp1['close']*quant1 / (temp2['close']*quant2))
    result['time']=temp1['time']

    price1=round(temp1.close[len(result)-1],2)
    price2 = round(temp2.close[len(result) - 1], 2)
    latesest_diff=round(result.close[len(result)-1],2)
    pre_diff=round(result.close[len(result)-2],2)
    diff_10=round(result.close[len(result)-11],2)
    diff_20 = round(result.close[len(result) - 21], 2)
    diff_30 = round(result.close[len(result) - 31], 2)
 #   sample_number=len(result)
    min_time= result.time[0].strftime("%Y-%m-%d")
    max_time= result.time[len(result)-1].strftime("%Y-%m-%d")

    avg_diff= round(np.mean(result.close),2)

    min_diff=round(np.min(result.close),2)
    percentile5=round(np.percentile(result.close,5),2)
    percentile95=round(np.percentile(result.close,95),2)
    max_diff=round(np.max(result.close),2)

    print("handling "+ symbol1 +" and "+symbol2)
    return min_time, max_time,price1,price2,latesest_diff, pre_diff, diff_10, diff_20, diff_30, min_diff,percentile5,avg_diff,percentile95,max_diff


#difference('rb0','ru0',method='divide')
