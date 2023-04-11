import pandas as pd
import requests as res
from Pcomponents import Tools
class APi:
    def getminutedata(self,symbol,interval,lookback):
        frame=pd.DataFrame(res.post("https://trade07-1-j3584132.deta.app/",headers={"x-api-key":"a0TvWwDmm4GF_oqheWPNEzJV2RPuzzjPijK6jhvwAoVph"},json={'asset':symbol,'interval':interval,'lookback':lookback}))
        frame=frame.iloc[:,:6]
        frame.columns=['Time','Open','High','Low','Close','Volume']
        frame=frame.set_index('Time')
        frame.index=pd.to_datetime(frame.index,unit='ms')
        frame=frame.astype(float)
        return frame
    