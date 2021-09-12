import datetime as dt
import backtrader as bt
import backtrader.feeds as btfeed


def start_strategy(data, strategy, needPaint):
# 初始化模型
    cerebro = bt.Cerebro()
# 设定初始资金
    cerebro.broker.setcash(100000.0)
# 设定交易费率，取万1
    cerebro.broker.setcommission(0.0001)
# 设定需要最低买的股数
    cerebro.addsizer(bt.sizers.FixedSize, stake=100)

# 加载数据

    cerebro.adddata(data)

    #加载策略
    cerebro.addstrategy(strategy)

# 策略执行前的资金
    before = cerebro.broker.getvalue()
    print('Starting Portfolio Value: %.2f' % cerebro.broker.getvalue())

    cerebro.run()

# 策略执行后的资金
    print('Final Portfolio Value: %.2f' % cerebro.broker.getvalue())
    earned = cerebro.broker.getvalue() - before
    print('============================================> %.2f' % earned)

    if needPaint:
        cerebro.plot()
