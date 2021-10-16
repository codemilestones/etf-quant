import backtrader as bt

import pandas as pd
import numpy as np

class NetTradeStrategy(bt.Strategy):
    params=(('p1',12),('p2',26),('p3',9),)
    def __init__(self):
        self.order = None
        #获取MACD柱
        self.macdhist = bt.ind.MACDHisto(self.data,
                        period_me1=self.p.p1, 
                        period_me2=self.p.p2, 
                        period_signal=self.p.p3)
        # bt.ind.MACD(self.data)
        # bt.ind.MACDHisto(self.data)
        # bt.ind.RSI(self.data,period=14)
        # bt.ind.BBands(self.data)
        self.highest = bt.indicators.Highest(self.data.high, period=650, subplot=False)
        self.lowest = bt.indicators.Lowest(self.data.low, period=650, subplot=False)
        mid = (self.highest + self.lowest)/2
        perc_levels = [x for x in np.arange(
            1 + 0.005 * 5, 1 - 0.005 * 5 - 0.005/2, -0.005)]
        self.price_levels = [mid * x for x in perc_levels]
        self.last_price_index = None
        for i in range(len(self.price_levels)):
            print(i)
            print(self.price_levels[i] + 0)
        

    def next(self):
        if self.last_price_index == None:
            for i in range(len(self.price_levels)):
                if self.data.close > self.price_levels[i]:
                    self.last_price_index = i
                    self.order_target_percent(
                        target=i/(len(self.price_levels) - 1))
                    return
        else:
            signal = False
            while True:
                upper = None
                lower = None
                if self.last_price_index > 0:
                    upper = self.price_levels[self.last_price_index - 1]
                if self.last_price_index < len(self.price_levels) - 1:
                    lower = self.price_levels[self.last_price_index + 1]
                # 还不是最轻仓，继续涨，就再卖一档
                if upper != None and self.data.close > upper:
                    self.last_price_index = self.last_price_index - 1
                    signal = True
                    continue
                # 还不是最重仓，继续跌，再买一档
                if lower != None and self.data.close < lower:
                    self.last_price_index = self.last_price_index + 1
                    signal = True
                    continue
                break
            if signal:
                self.long_short = None
                self.order_target_percent(
                    target=self.last_price_index/(len(self.price_levels) - 1))