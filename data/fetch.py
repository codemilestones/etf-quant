#import akshare as ak
#stock_zh_a_hist_df = ak.stock_zh_a_hist(symbol="000001", period="daily", start_date="20170301", end_date='20210907', adjust="")
#print(stock_zh_a_hist_df)
import akshare as ak
from pandas import Series,DataFrame
import pandas as pd
#前复权拉去股票数
def fetch_index(index):
    stock_df = ak.stock_zh_index_daily_tx(symbol=index)
    stock_df["pcnt"] = (stock_df["close"] - stock_df["close"].shift(1)) / stock_df['close'] * 100
    stock_df["pcnt"].fillna(0)

    # 长线指标 1d, 10d, 20d, 60d, 120d, 240d
    peried = [1,5,10,20,60,120,240]
    for p in peried:
        stock_high_max=compute_m_day_max(stock_df, p)
        stock_low_min=compute_m_day_min(stock_df, p)
        stock_df['pcnt_'+str(p)+'d'] = (stock_high_max - stock_low_min) / stock_df['close'] * 100

    stock_high_max=compute_m_day_max(stock_df, 250)
    stock_low_min=compute_m_day_min(stock_df, 250)
    stock_df['max_price'] = stock_high_max
    stock_df['min_price'] = stock_low_min
    stock_high_max_500=compute_m_day_max(stock_df, 500)
    stock_low_min_500=compute_m_day_min(stock_df, 500) 
    stock_df['max_price_500d'] = stock_high_max_500
    stock_df['min_price_500d'] = stock_low_min_500

    stock_df.to_csv(index + ".csv", date_format='%Y-%m-%d')

def compute_m_day_max(df, day):
    max_df = df['high']
    for i in range(1,day+1):
        max_df = DataFrame([df['high'].shift(i), max_df]).T.max(axis=1)
    return max_df

def compute_m_day_min(df, day):
    min_df = df['low']
    for i in range(1,day+1):
        min_df = DataFrame([df['low'].shift(i), min_df]).T.min(axis=1)
    return min_df

if __name__ == '__main__':
    stock = pd.read_csv('stock.csv')
    for index in stock['code']:
        print('start fetch: ' + index)
        fetch_index(index)