api_key="RPMoUjlXHyhmZ1rSAvVx89iWWS5ENczsxNHWGv67i7zY1OLr8gxPdZevmXQg7Guj"
api_secret="Vwk6pemdQIfF8vkjNYMGqegB9sLXw24ITrVv9FHBCWTINzpTcciOQv27peCX9cyO"
# import requests
import json
import time
import pandas as pd
from binance.client import Client
import streamlit as st
import plotly as px
import plotly.graph_objects as go
import plotly.subplots as subplot


# client = Client(api_key, api_secret)

# asset = 'BTCUSDT'
# def getminutedata(symbol,interval,lookback):
#     frame=pd.DataFrame(client.get_historical_klines(symbol,interval,lookback))
#     frame=frame.iloc[:,:6]
#     frame.columns=['Time','Open','High','Low','Close','Volume']
#     frame=frame.set_index('Time')
#     frame.index=pd.to_datetime(frame.index,unit='ms')
#     frame=frame.astype(float)
#     return frame

# df=getminutedata(asset,'5m','5d')
# fig = go.Figure(data=[go.Candlestick(x=df.index,
#                 open=df['Open'],
#                 high=df['High'],
#                 low=df['Low'],
#                 close=df['Close'])])

# def addi(def1,def2):
#     def1=pd.concat([def1,def2])
#     return def1

# df=getminutedata(asset,'1m','12h')
# fig = go.Figure(data=[go.Candlestick(x=df.index,
#                 open=df['Open'],
#                 high=df['High'],
#                 low=df['Low'],
#                 close=df['Close'])])
# placeholder=st.empty()

# for i in range(1,100):
#     df=addi(df,getminutedata(asset,'1m','1m'))
#     with placeholder.container():
#         st.plotly_chart(fig.update(data=[go.Candlestick(x=df.index,
#                 open=df['Open'],
#                 high=df['High'],
#                 low=df['Low'],
#                 close=df['Close'])]))
#     time.sleep(1)
import os
# def file_join_dir(file):#return the file name relative to current file
#     return os.path.join(os.path.dirname(os.path.abspath(__file__)),file)



# def config_RoE(read_edit=1,content={}):#function is used to read or edit json configuration (1 for read 0 for edit ) default=1,for reas it returns a dictionary,for write you should give dictionary                                     
#     with open(file_join_dir('config.json'),'w+') as file:
#         if read_edit:
#             return json.load(file)
#         else:
            
#             json.dump(content,file)

# st.set_page_config(page_title='DEEP DASH',
#                    page_icon='📈',
#                    layout='wide'
#                    )#page configuration

# st.title('Deep Trade Dashboard')#Title bar

# st.session_state['ASSET']="BTCUSDT" #default market

# st.session_state['ASSET']=st.selectbox('select market',                #selecting market using delectbox
#                                        ['BTCUSDT','ETHUSDT']
                                      # )

# df=getminutedata(asset,'5m','5d')
# fig = go.Figure(data=[go.Candlestick(x=df.index,
#                 open=df['Open'],
#                 high=df['High'],
#                 low=df['Low'],
#                 close=df['Close'])])

# def addi(def1,def2):
#     def1=pd.concat([def1,def2])
#     return def1

# df=getminutedata(st.session_state['ASSET'],'1m','1h')
# fig = go.Figure(data=[go.Candlestick(x=df.index,
#                 open=df['Open'],
#                 high=df['High'],
#                 low=df['Low'],
#                 close=df['Close'])])
# placeholder=st.empty()

# for i in range(1,100):
#     df=addi(df,getminutedata(st.session_state['ASSET'],'1m','1m'))
#     with placeholder.container():
#         st.write(st.session_state['ASSET'])
#         st.plotly_chart(fig.update(data=[go.Candlestick(x=df.index,
#                 open=df['Open'],
#                 high=df['High'],
#                 low=df['Low'],
#                 close=df['Close'])]))
#     time.sleep(1)


#   def EMa(self,T,df):
#         return Tb.EMA(df['Close'],timeperiod=T)
        
#     def plot_charti(self,asset,eMAA=0):
#         if asset != self.temp_asset:
#             print(123)
#             self.temp_asset=asset
#             self.Dframe=self.api.getminutedata(self.temp_asset,'1m','24h')
#             self.fig=go.Figure()
#             candy = go.Candlestick(x=self.Dframe.index,
#                 open=self.Dframe['Open'],
#                 high=self.Dframe['High'],
#                 low=self.Dframe['Low'],
#                 close=self.Dframe['Close'])
#             if eMAA!=0:
#                  self.fig.add_scatter(x=self.Dframe.index,y=self.Dframe['EMA'])

#         else:
#             self.Dframe=Tools.add_Data_Frames(self.Dframe,self.api.getminutedata(self.temp_asset,'1m','1m'))
#             self.Dframe['EMA']=self.EMa(12,self.Dframe)
#             self.fig.update(data=[go.Candlestick(x=self.Dframe.index,
#                 open=self.Dframe['Open'],
#                 high=self.Dframe['High'],
#                 low=self.Dframe['Low'],
# 
# 
##################################################################

from barfi import st_barfi, barfi_schemas, Block,ComputeEngine,load_schema_name
import streamlit as st
from barfi import Block
feed = Block(name='DATA Feeder')
feed.add_option(name='TFrame',type='integer')
feed.add_output()
def feed_func(self):
    self.set_interface(name='Output', value=self.get_option(name='TFrame'))
feed.add_compute(feed_func)

splitter = Block(name='Splitter')
splitter.add_input()
splitter.add_output()
splitter.add_output()
def splitter_func(self):
    in_1 = self.get_interface(name='Input 1')
    value = (in_1/2)
    self.set_interface(name='Output 1', value=value)
    self.set_interface(name='Output 2', value=value)
splitter.add_compute(splitter_func)

mixer = Block(name='Mixer')
mixer.add_input()
mixer.add_input()
mixer.add_output()
def mixer_func(self):
    in_1 = self.get_interface(name='Input 1')
    in_2 = self.get_interface(name='Input 2')
    value = (in_1 + in_2)
    print(value)
    self.set_interface(name='Output 1', value=value)
mixer.add_compute(mixer_func)

result = Block(name='Result')
result.add_input()
def result_func(self):
    in_1 = self.get_interface(name='Input 1')
    print(in_1)
result.add_compute(result_func)

load_schema = st.selectbox('Select a saved schema:', barfi_schemas())
compute_engine=st.checkbox('activate barfi',value=False)


barfi_result = st_barfi(base_blocks=[feed, result, mixer, splitter],
                     compute_engine=False,load_schema=load_schema)





#to execute schema
if compute_engine:
        ce=ComputeEngine(blocks=[feed, result, mixer, splitter])
        ce.add_editor_state(editor_state=barfi_result['editor_state'])
        ce._map_block_link()
        ce._execute_compute()
