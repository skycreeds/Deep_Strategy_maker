import pandas as pd
from binance.client import Client
from . import Tools
class APi:
    def __init__(self) -> None:
        self.config=Tools.config_RoE()
        self.cLient=Client(self.config['api_key'],self.config['api_secret'])

    def getminutedata(self,symbol,interval,lookback):
        frame=pd.DataFrame(self.cLient.get_historical_klines(symbol,interval,lookback))
        frame=frame.iloc[:,:6]
        frame.columns=['Time','Open','High','Low','Close','Volume']
        frame=frame.set_index('Time')
        frame.index=pd.to_datetime(frame.index,unit='ms')
        frame=frame.astype(float)
        return frame
    