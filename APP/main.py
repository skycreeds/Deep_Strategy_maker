import time,json,requests
import numpy as np  
import pandas as pd 
import plotly.express as px  
import streamlit as st 
from components.appiOb import APi
from components.charting import chaRTTY
st.set_page_config(page_title='DEEP DASH',
                   page_icon='📈',
                   layout='wide'
                   )#page configuration
if 'startp1' not in st.session_state:
    st.session_state.Api=APi()
    st.session_state.startp1=0

chaRT=chaRTTY()

st.title('Deep Trade Dashboard')#Title bar
st.session_state['ASSET']=st.selectbox('select market',                #selecting market using delectbox
                                       ['BTCUSDT','ETHUSDT']
                                       )



st.get
placeholder=st.empty()
while True:
    with placeholder.container():

        st.plotly_chart(chaRT.plotty(asset=st.session_state['ASSET'],eMAA=1,ematime=[6,12]))
    time.sleep(1)


