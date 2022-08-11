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

#加载Sharpe比率和最大回测分析器
    cerebro.addanalyzer(bt.analyzers.SharpeRatio, _name = 'SharpeRatio')
    cerebro.addanalyzer(bt.analyzers.DrawDown, _name='DrawDown')

# 策略执行前的资金
    before = cerebro.broker.getvalue()
    print('Starting Portfolio Value: %.2f' % cerebro.broker.getvalue())

    result = cerebro.run()

# 策略执行后的资金
    print('Final Portfolio Value: %.2f' % cerebro.broker.getvalue())
    earned = cerebro.broker.getvalue() - before
    print('============================================> %.2f' % earned)

    print('夏普比率：', result[0].analyzers.SharpeRatio.get_analysis()['sharperatio'])
    print('最大回撤：', result[0].analyzers.DrawDown.get_analysis()['max']['drawdown'])

    if needPaint:
        cerebro.plot()
