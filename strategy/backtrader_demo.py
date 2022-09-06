import backtrader as bt
import pandas as pd
import matplotlib.pyplot as plt
import datetime as dt
import numpy as np

from data_loader import getDataFromCSV

class SMAStrategy(bt.Strategy):
    def __init__(self):
        self.dataclose = self.data0.close
        self.order = None
        self.buyprice = None
        self.buycomm = None
        self.sma = bt.indicators.MovingAverageSimple(self.data0, period=100)

    def next(self):
        if not self.position:
            if self.dataclose[0] > self.sma[0]:
                self.buy()
        else:
            if self.dataclose[0] < self.sma[0]:
                self.close()

class MyStrategy(bt.Strategy):

    def __init__(self):
        self.sma = bt.indicators.MovingAverageSimple(self.data0, period=100)        
        self.buy_signal = bt.indicators.CrossOver(self.data.close, self.sma)
        self.sell_signal = bt.indicators.CrossDown(self.data.close, self.sma)
        self.last_sell_data = None


    def next(self):
        if not self.position and self.buy_signal[0] == 1:
            if not self.last_sell_data or (self.datetime.date(0) - self.last_sell_data).days > 100:
                self.order = self.buy()
                self.order = self.sell(exectype=bt.Order.StopTrail, trailpercent=0.1)



    def notify_order(self, order):
        if order.ordtype == 1 and order.status == 2:
            self.last_sell_data = self.datetime.date(0)

if __name__ == "__main__":
    cerebro = bt.Cerebro()
    data_stock = getDataFromCSV('data/sh510500.csv', dt.datetime(2015,5,29), dt.datetime(2022,1,1))
    cerebro.adddata(data_stock)

    cerebro.addstrategy(MyStrategy)
    cerebro.addanalyzer(bt.analyzers.SharpeRatio, _name = 'SharpeRatio')
    cerebro.addanalyzer(bt.analyzers.DrawDown, _name='DrawDown')

    cerebro.broker.setcash(100000.0)
    cerebro.broker.setcommission(commission=0.0006)

    cerebro.addsizer(bt.sizers.PercentSizer, percents=90)

    before = cerebro.broker.getvalue()
    print('Starting Portfolio Value: %.2f' % cerebro.broker.getvalue())

    result = cerebro.run()
    
    print('Final Portfolio Value: %.2f' % cerebro.broker.getvalue())
    earned = cerebro.broker.getvalue() - before
    print('============================================> %.2f' % earned)

    print('夏普比率：', result[0].analyzers.SharpeRatio.get_analysis()['sharperatio'])
    print('最大回撤：', result[0].analyzers.DrawDown.get_analysis()['max']['drawdown'])

    cerebro.plot()