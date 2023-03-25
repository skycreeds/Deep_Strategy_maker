import json
import os
import pandas as pd
import talib as Tb


def file_join_dir(file):#return the file name relative to current file
    return os.path.join(os.path.dirname(os.path.abspath(__file__)),file)

def config_RoE(read_edit=1,content={}):#function is used to read or edit json configuration (1 for read 0 for edit ) default=1,for reas it returns a dictionary,for write you should give dictionary                                     
    with open(file_join_dir('config.json'),'r+') as file:#always enter the full config as a dict
        if read_edit:
            return json.load(file)
        else:
            
            json.dump(content)

def add_Data_Frames(def1,def2):
    def1=pd.concat([def1,def2])
    return def1

def ema(t,fig,dframe,etime):
    if t:
        for i in etime:
            dframe['EMA']=Tb.EMA(dframe['Close'],i)
            fig=fig.add_scatter(x=dframe.index,y=dframe['EMA'],name='EMA')
    return fig






