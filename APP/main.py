import time,json,requests
import numpy as np  
import pandas as pd 
import plotly.express as px  
import streamlit as st 
from APi.appiOb import APi
from Pcomponents.charting import chaRTTY
#################################################################
import requests
import os
import sys
import subprocess

# check if the library folder already exists, to avoid building everytime you load the pahe
if not os.path.isdir("/tmp/ta-lib"):

    # Download ta-lib to disk
    with open("/tmp/ta-lib-0.4.0-src.tar.gz", "wb") as file:
        response = requests.get(
            "http://prdownloads.sourceforge.net/ta-lib/ta-lib-0.4.0-src.tar.gz"
        )
        file.write(response.content)
    # get our current dir, to configure it back again. Just house keeping
    default_cwd = os.getcwd()
    os.chdir("/tmp")
    # untar
    os.system("tar -zxvf ta-lib-0.4.0-src.tar.gz")
    os.chdir("/tmp/ta-lib")
    # build
    os.system("./configure --prefix=/home/appuser/venv/")
    os.system("make")
    # install
    os.system("mkdir -p /home/appuser/venv/")
    os.system("make install")
    os.system("ls -la /home/appuser/venv/")
    # back to the cwd
    os.chdir(default_cwd)
    sys.stdout.flush()

# add the library to our current environment
from ctypes import *

lib = CDLL("/home/appuser/venv/lib/libta_lib.so.0.0.0")
# import library
try:
    import talib
except ImportError:
    subprocess.check_call([sys.executable, "-m", "pip", "install", "--global-option=build_ext", "--global-option=-L/home/appuser/venv/lib/", "--global-option=-I/home/appuser/venv/include/", "ta-lib==0.4.24"])
finally:
    import talib

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
         time.sleep(1)


