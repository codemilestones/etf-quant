from net_strategy import NetTradeStrategy
from pandas._libs.tslibs import timestamps
from test_strategy import TradeStrategy
from strategy_manager import start_strategy
import backtrader as bt
import pandas as pd
import datetime

origin_file = 'data/sh510500.csv'
temp_file = 'temp.csv'

start_date = [
    datetime.datetime(2013, 1, 1),
    datetime.datetime(2013, 7, 1),
    datetime.datetime(2014, 1, 1),
    datetime.datetime(2014, 7, 1),
    datetime.datetime(2015, 1, 1),
    datetime.datetime(2015, 7, 1),
    datetime.datetime(2016, 1, 1),
    datetime.datetime(2016, 7, 1),
    datetime.datetime(2017, 1, 1),
    datetime.datetime(2017, 7, 1),
    datetime.datetime(2018, 1, 1),
    datetime.datetime(2018, 7, 1),
    datetime.datetime(2019, 1, 1),
    datetime.datetime(2019, 7, 1),
    datetime.datetime(2020, 1, 1),
    datetime.datetime(2020, 7, 1),
    datetime.datetime(2021, 1, 1),
    datetime.datetime(2021, 7, 1)
]

end_date = [
    datetime.datetime(2013, 1, 1),
    datetime.datetime(2013, 7, 1),
    datetime.datetime(2014, 1, 1),
    datetime.datetime(2014, 7, 1),
    datetime.datetime(2015, 1, 1),
    datetime.datetime(2015, 7, 1),
    datetime.datetime(2016, 1, 1),
    datetime.datetime(2016, 7, 1),
    datetime.datetime(2017, 1, 1),
    datetime.datetime(2017, 7, 1),
    datetime.datetime(2018, 1, 1),
    datetime.datetime(2018, 7, 1),
    datetime.datetime(2019, 1, 1),
    datetime.datetime(2019, 7, 1),
    datetime.datetime(2020, 1, 1),
    datetime.datetime(2020, 7, 1),
    datetime.datetime(2021, 1, 1),
    datetime.datetime(2021, 7, 1)
]

def run_test(file, start, end):
    print("")
    print(start)
    data = bt.feeds.GenericCSVData(
        dataname=file,
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

    start_strategy(data, TradeStrategy, False)

for i in range(10, 12):
    df = pd.read_csv(origin_file)
    df=df.drop(columns ='Unnamed: 0')
    df.to_csv(temp_file, index=False)

    run_test(temp_file, start_date[i], start_date[i+6])