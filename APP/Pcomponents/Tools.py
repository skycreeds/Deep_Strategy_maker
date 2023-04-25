import json
import os
import pandas as pd
import requests
import os
import sys
import subprocess
os.system('python3 '+'/app/deep_strategy_maker/barfi1/setup.py install')
import streamlit as st
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
    import talib as Tb



def file_join_dir(file):#return the file name relative to current file
    return os.path.join(os.path.dirname(os.path.abspath(__file__)),file)

# def config_RoE(read_edit=1,content={}):#function is used to read or edit json configuration (1 for read 0 for edit ) default=1,for reas it returns a dictionary,for write you should give dictionary                                     
#     with open(file_join_dir('config.json'),'r+') as file:#always enter the full config as a dict
#         if read_edit:
#             return json.load(file)
#         else:
            
#             json.dump(content)

def add_Data_Frames(def1,def2):
    def1=pd.concat([def1,def2])
    return def1

def ema(t,fig,dframe,etime):
    if t:
        for i in etime:
            dframe['EMA']=Tb.EMA(dframe['Close'],etime[i])
            fig=fig.add_scatter(x=dframe.index,y=dframe['EMA'],name=i)
    return fig

def rsi(t,fig,dframe,rtime):
    if t:
        for i in rtime:
            dframe['RSI']=Tb.RSI(dframe['Close'],rtime[i])
            fig=fig.add_scatter(x=dframe.index,y=dframe['RSI'],name=i)
            return fig



    






