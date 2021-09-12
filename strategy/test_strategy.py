import backtrader as bt

class TradeStrategy(bt.Strategy):
    params=(('p1',12),('p2',26),('p3',9),)
    def __init__(self):
        self.order = None
        #获取MACD柱
        self.macdhist = bt.ind.MACDHisto(self.data,
                        period_me1=self.p.p1, 
                        period_me2=self.p.p2, 
                        period_signal=self.p.p3)
        bt.ind.MACD(self.data)
        bt.ind.MACDHisto(self.data)
        bt.ind.RSI(self.data,period=14)
        bt.ind.BBands(self.data)

    def next(self):
        if not self.position:
            # 得到当前的账户价值
            total_value = self.broker.getvalue()
            #1手=100股，满仓买入
            ss=int((total_value/100)/self.datas[0].close[0])*100
            #当MACD柱大于0（红柱）且无持仓时满仓买入
            if self.macdhist > 0:
                self.order=self.buy(size=ss)
        else:
            #当MACD柱小于0（绿柱）且持仓时全部清仓
            if self.macdhist < 0:
                self.close()