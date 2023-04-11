import time,json,requests
import numpy as np  
import pandas as pd 
import plotly.express as px  
import streamlit as st 
from APi.appiOb import APi
from Pcomponents.charting import chaRTTY
#################################################################

###################################################################################





st.set_page_config(page_title='DEEP DASH',
                   page_icon='📈',
                   layout='wide'
                   )#page configuration
if 'Api' not in st.session_state:
    st.session_state.Api=APi()

chaRT=chaRTTY()

st.title('Deep Trade Dashboard')#Title bar
st.session_state['ASSET']=st.selectbox('select market',                #selecting market using delectbox
                                       ['BTCUSDT','ETHUSDT']
                                       )
##############################button render####################################
Ema={'EMA1':1,'EMA2':1,'EMA3':1}
rsi={'RSI1':1}
Ema['EMA1']=st.number_input('EMA1',min_value=2)
Ema['EMA2']=st.number_input('EMA2',min_value=2)
Ema['EMA3']=st.number_input('EMA3',min_value=2)
rsi['RSI1']=st.number_input('RSI1',min_value=2)
#######################chart rendering##############################################################
placeholder=st.empty()
while True:
    with placeholder.container():
         st.plotly_chart(chaRT.plotty(asset=st.session_state['ASSET'],eMAA=1,ematime=Ema))
         st.plotly_chart(chaRT.plotty2(rse=1,rsitime=rsi))
         time.sleep(30)


