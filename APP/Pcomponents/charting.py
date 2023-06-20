#Charting components
import plotly as px
import streamlit as st
from APi.appiOb import APi
import plotly.graph_objects as go
from . import Tools

import time
#class to plot charts of ema and rsi
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
      #To plot Ema
    def plotty(self,asset,eMAA=0,ematime={}):
        if asset != self.temp_asset:
          self.temp_asset=asset
          #get data using api module
          self.dframe=self.api.getminutedata(self.temp_asset,self.Tframe,self.lookback)
        
        else:
           self.fig=go.Figure()
           self.dframe=Tools.add_Data_Frames(self.dframe,self.api.getminutedata(self.temp_asset,'1m','1m'))
           self.alert=1
           #render Candle stick data
           self.fig.add_candlestick(x=self.dframe.index,
                open=self.dframe['Open'],
                high=self.dframe['High'],
                low=self.dframe['Low'],
                close=self.dframe['Close'],name=self.temp_asset)
           self.fig=Tools.ema(eMAA,self.fig,self.dframe,ematime)
        return self.fig
    #To plot RSI 
    def plotty2(self,rse=0,rsitime={}):
           self.fig2=go.Figure()
           self.fig2=Tools.rsi(rse,self.fig2,self.dframe,rsitime)
           
           return self.fig2   

        



