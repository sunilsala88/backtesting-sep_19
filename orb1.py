
from backtesting import Backtest, Strategy

import pandas as pd

import time




class ORBStrategy(Strategy):
    
    def init(self):
        self.orb_high = None
        self.orb_low = None
        self.trade=0


    def next(self):
        # print(self.data.df)
        # time.sleep(1)

        # if len(self.data) < 2:
        #     return
        # else:

            if self.data.index[-1].time() == pd.Timestamp('10:00').time():
                df=self.data.df
                d=self.data.index[-1]
                d=pd.to_datetime(d.date())
                df=df[df.index>=d]
                self.orb_high = df.High.max()
                self.orb_low = df.Low.min()
                self.trade=0
                print(self.orb_high, self.orb_low)

        
            if not self.position and self.orb_high and self.orb_low:
                print('inside condition')
                if (self.data.Close[-1] > self.orb_high) and self.trade==0:
                    print('buy condition satisfied')
                    self.buy()
                    self.trade=1
                elif (self.data.Close[-1] < self.orb_low) and self.trade==0:
                    print('sell condition satisfied')
                    self.sell()
                    self.trade=1

            elif self.position:
                # Close position by the end of the day
                print('i have some position')
                if self.data.index[-1].time() == pd.Timestamp('15:20').time():
                    self.position.close()
                print(self.position)


import yfinance as yf
def fetch_data(stocks):
    data = yf.download(stocks, period='5d',interval='1m')
    return data
    

    
stocks=['AMZN','GOOG']
results = {}
for stock in stocks:
    data = fetch_data(stock)
    print(data)
    data.reset_index(inplace=True)
    data['Date']=data['Datetime'].dt.tz_localize(None)
    data.set_index('Date',inplace=True)
    bt = Backtest(data, ORBStrategy, cash=100_000, commission=.002)
    stats = bt.run()
    results[stock] = stats
    bt.plot()

for stock, stats in results.items():
    print(f"{stock}:")
    print(stats)