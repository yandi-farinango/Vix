import backtrader as bt 
from backtrader import Cerebro
import os 

cerebro = Cerebro()

class SPYVIXData(bt.feeds.GenericCSVData):      # To attach datafeed, we're extending GenericCSVData class 
    # specifiy lines we are interested in 
    lines = ('vixopen', 'vixhigh', 'vixclose')

    # Mapping GenericCSVData class to columns in OUR CSV
    params = (
        ('dtformat', '%Y-%m-%d'),
        ('date', 0), 
        ('spyopen', 1), 
        ('spyhigh', 2), 
        ('spylow', 3), 
        ('spyclose', 4), 
        ('spyadjclose', 5), 
        ('spyvolume', 6), 
        ('vixopen', 7), 
        ('vixhigh', 8), 
        ('vixlow', 9), 
        ('vixclose', 10)
    )

# VIX Data Feed 
class VIXData(bt.feeds.GenericCSVData):
    params = (
        ('dtformat', '%m/%d/%Y'),
        ('date', 0),
        ('vixopen', 1), 
        ('vixhigh', 2), 
        ('vixlow', 3), 
        ('vixclose', 4), 
        ('volume', -1), 
        ('openinterest', -1)
    )

spy_vix_file = 'Data/spy_vix.csv'
vix_file = 'Data/vix.csv'


# instantiate Data Feed classes 
spyVixDataFeed = SPYVIXData(dataname=spy_vix_file)
vixDataFeed = VIXData(dataname=vix_file)

# # Connect Data Feed to Cerebro 
cerebro.adddata(spyVixDataFeed)
cerebro.adddata(vixDataFeed)

cerebro.run()
cerebro.plot(volume=False)  # we havent provided volume data 