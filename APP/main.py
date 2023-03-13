import time,json,requests
import numpy as np  
import pandas as pd 
import plotly.express as px  
import streamlit as st 
from components.charting import chaRTTY
st.set_page_config(page_title='DEEP DASH',
                   page_icon='📈',
                   layout='wide'
                   )#page configuration

st.title('Deep Trade Dashboard')#Title bar
st.session_state['ASSET']=st.selectbox('select market',                #selecting market using delectbox
                                       ['BTCUSDT','ETHUSDT']
                                       )
placeholder=st.empty()
for i in range(50):

    with placeholder.container():

        st.plotly_chart(chaRTTY().plot_charti(asset=st.session_state['ASSET']))
    time.sleep(1)


