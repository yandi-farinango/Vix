import backtrader as bt 
import datetime


class VIXStrategy(bt.Strategy):   # extends bt.Strategy
    def __init__(self):
        self.vix = self.datas[0].vixclose
        self.spyopen = self.datas[0].open
        self.spyclose = self.datas[0].close

    # logging function for printing date 
    def log(self, txt, dt=None):
        dt = dt or self.datas[0].datetime.date(0)
        print('%s, %s' % (dt.isoformat(), txt))

    # what we want the strategy to do next
    # whatever indicator we are triggering our strategy based on  
    def next(self):
        # self.log(self.current_data)
        if self.vix[0] > 35:
            self.log('Previous VIX, %.2f' % self.vix[0])
            self.log('SPY Open, %.2f' % self.spyopen[0])

            # print(self.position.size)

            # if we havent taken a position yet and VIX is above 35
            if not self.position or self.broker.getcash() > 5000:
                size = int(self.broker.getcash() / self.spyopen[0])
                print('Buying {} SPY at {}'.format(size, self.spyopen[0]))
                self.buy(size=size)

        if len(self.spyopen) % 20 == 0:
            self.log('Adding 5000 cash to VIX buy and hold strategy. Cash on hand is now {}'.format(self.broker.getcash()))
            self.broker.add_cash(5000)

        # if VIX falls below 12, and we have an existing position, trigger sell ie close()
        # if self.vix[0] < 12 and self.position:
        #     self.close()    # can also do self.sell() to specify number of shares to sell 


