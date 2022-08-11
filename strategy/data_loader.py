import backtrader as bt
import pandas as pd

# 输入原始数据path 'data/sh510500.csv'
# 输入开始时间，结束时间，datetime.datetime(2013, 1, 1)
# 返回backtrader的数据格式
def getDataFromCSV(source_file, start, end):
    temp_file = 'temp.csv'
    df = pd.read_csv(source_file)
    df=df.drop(columns ='Unnamed: 0')
    df.to_csv(temp_file, index=False)

    data = bt.feeds.GenericCSVData(
        dataname=temp_file,
        datetime=0,
        open=1,
        high=2,
        low=3,
        close=4,
        volume=5,
        dtformat=('%Y-%m-%d'),
        openinterest=1,
        fromdate=start,
        todate=end
    )
    return data
