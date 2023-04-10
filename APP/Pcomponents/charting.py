import plotly as px
import streamlit as st
import plotly.graph_objects as go
# from .appiOb import APi
from . import Tools
#import talib as Tb
class chaRTTY:
    def __init__(self) -> None:
      self.temp_asset=""
      self.dframe=None
      self.fig=self.fig2=go.Figure()
      self.api=st.session_state.Api
    def plotty(self,asset,eMAA=0,ematime={}):
        if asset != self.temp_asset:
          self.temp_asset=asset
          self.dframe=self.api.getminutedata(self.temp_asset,'1m','30m')
        
        else:
           self.fig=go.Figure()
           self.dframe=Tools.add_Data_Frames(self.dframe,self.api.getminutedata(self.temp_asset,'1m','1m'))
           

           self.fig.add_candlestick(x=self.dframe.index,
                open=self.dframe['Open'],
                high=self.dframe['High'],
                low=self.dframe['Low'],
                close=self.dframe['Close'],name=self.temp_asset)
           self.fig=Tools.ema(eMAA,self.fig,self.dframe,ematime)
           

        return self.fig
    def plotty2(self,rse=0,rsitime={}):
           self.fig2=go.Figure()
           self.fig2=Tools.rsi(rse,self.fig2,self.dframe,rsitime)
           
           return self.fig2   

        



