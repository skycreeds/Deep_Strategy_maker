import pandas as pd
import requests as res
#api for getting data from binance through deta proxy

class APi:
    def getminutedata(self,symbol,interval,lookback):
        try:
            #post request is sent with parameters needed
            frame=pd.DataFrame(res.post("https://trade07-1-j3584132.deta.app/",headers={"x-api-key":"a0TvWwDmm4GF_oqheWPNEzJV2RPuzzjPijK6jhvwAoVph"},json={'asset':symbol,'interval':interval,'lookback':lookback}).json())
            #data processing 
            frame=frame.iloc[:,:6]
            frame.columns=['Time','Open','High','Low','Close','Volume']
            frame=frame.set_index('Time')#setting time as index
            frame.index=pd.to_datetime(frame.index,unit='ms')#setting as index
            frame=frame.astype(float)#converting datypes to float
            return frame
        except:
            print('api error')

    