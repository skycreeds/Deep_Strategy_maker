import plotly as px
import plotly.graph_objects as go
from .appiOb import APi
from . import Tools
class chaRTTY:
    def __init__(self) -> None:
        self.temp_asset=''
        self.Dframe=None
        self.api=APi()
    
    def plot_charti(self,asset):
        if asset != self.temp_asset:
            self.temp_asset=asset
            self.Dframe=self.api.getminutedata(self.temp_asset,'1m','1h')
            fig = go.Figure(data=[go.Candlestick(x=self.Dframe.index,
                open=self.Dframe['Open'],
                high=self.Dframe['High'],
                low=self.Dframe['Low'],
                close=self.Dframe['Close'])])
        else:
            self.Dframe=Tools.add_Data_Frames(self.Dframe,self.api.getminutedata(self.temp_asset,'1m','1m'))
            fig=fig.update(data=[go.Candlestick(x=self.Dframe.index,
                open=self.Dframe['Open'],
                high=self.Dframe['High'],
                low=self.Dframe['Low'],
                close=self.Dframe['Close'])])
        return fig

        



