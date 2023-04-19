import plotly as px
import streamlit as st
from APi.appiOb import APi
import plotly.graph_objects as go
# from .appiOb import APi
from . import Tools
#import talib as Tb
import time
class chaRTTY:
    def __init__(self,Tframe) -> None:
      self.temp_asset=""
      self.alert=0
      
      if Tframe =='1m':
          self.Tframe=Tframe
          self.lookback='30m'
      else:
          self.Tframe=Tframe
          self.lookback='30d'


      self.dframe=None
      self.fig=self.fig2=go.Figure()
      self.api=APi()
    def plotty(self,asset,eMAA=0,ematime={}):
        if asset != self.temp_asset:
          self.temp_asset=asset
          self.dframe=self.api.getminutedata(self.temp_asset,self.Tframe,self.lookback)
        
        else:
           self.fig=go.Figure()
           self.dframe=Tools.add_Data_Frames(self.dframe,self.api.getminutedata(self.temp_asset,'1m','1m'))
           self.alert=1
           self.fig.add_candlestick(x=self.dframe.index,
                open=self.dframe['Open'],
                high=self.dframe['High'],
                low=self.dframe['Low'],
                close=self.dframe['Close'],name=self.temp_asset)
           self.fig=Tools.ema(eMAA,self.fig,self.dframe,ematime)
           

        return self.fig
    def plotty2(self,rse=0,rsitime={}):
           self.fig2=go.Figure()
           print(222222222222222)
           self.fig2=Tools.rsi(rse,self.fig2,self.dframe,rsitime)
           
           return self.fig2   

        



