import datetime as dt
import backtrader as bt
import backtrader.feeds as btfeed


# 初始化模型
cerebro = bt.Cerebro()
# 设定初始资金
cerebro.broker.setcash(100000.0)
# 设定交易费率，取万1
cerebro.broker.setcommission(0.0001)
# 设定需要最低买的股数
cerebro.addsizer(bt.sizers.FixedSize, stake=100)

# 加载数据
data = btfeed.GenericCSVData(
    dataname='../data/sh510500.csv',
    datetime=0,
    open=1,
    high=2,
    low=3,
    close=4,
    volume=5,
    dtformat=('%Y-%m-%d'),
    openinterest=1
 #   fromdate=dt.datetime(2013, 3, 15),
 #   todate=dt.datetime(2020, 4, 12)
)
cerebro.adddata(data)

# 策略执行前的资金
print('Starting Portfolio Value: %.2f' % cerebro.broker.getvalue())

cerebro.run()

# 策略执行后的资金
print('Final Portfolio Value: %.2f' % cerebro.broker.getvalue())