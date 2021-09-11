#import akshare as ak
#stock_zh_a_hist_df = ak.stock_zh_a_hist(symbol="000001", period="daily", start_date="20170301", end_date='20210907', adjust="")
#print(stock_zh_a_hist_df)
import akshare as ak
#前复权拉去股票数
def fetch_index(index):
    stock_zh_a_hist_df = ak.stock_zh_index_daily(symbol=index)
    stock_zh_a_hist_df.to_csv(index + ".csv")
    print(stock_zh_a_hist_df)

index_list = ["sh510500", "sh515700", "sh512010", "sz159928"]

for index in index_list:
    fetch_index(index)