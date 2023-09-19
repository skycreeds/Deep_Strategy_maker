import time,json,requests
import numpy as np  
import pandas as pd 
import plotly.express as px  
import streamlit as st 
from APi import DBob
from Pcomponents.charting import chaRTTY
import hashlib
import subprocess,sys
from barfi import save_schema
#A premade schema for first time users
simple_strat={
  "nodes": [
    {
      "type": "Data Feed",
      "id": "node_16837244427902",
      "name": "Data Feed-1",
      "options": [
        [
          "TFrame",
          "1m"
        ],
        [
          "MAX_lookback",
          10
        ]
      ],
      "state": {},
      "interfaces": [
        [
          "outdatafeed",
          {
            "id": "ni_16837244427913",
            "value": None
          }
        ]
      ],
      "position": {
        "x": 31,
        "y": 206
      },
      "width": 200,
      "twoColumn": False,
      "customClasses": ""
    },
    {
      "type": "EMA",
      "id": "node_16837244500904",
      "name": "EMA-1",
      "options": [
        [
          "lookback",
          4
        ]
      ],
      "state": {},
      "interfaces": [
        [
          "inema",
          {
            "id": "ni_16837244500905",
            "value": None
          }
        ],
        [
          "outema",
          {
            "id": "ni_16837244500906",
            "value": None
          }
        ]
      ],
      "position": {
        "x": 291,
        "y": 70
      },
      "width": 200,
      "twoColumn": False,
      "customClasses": ""
    },
    {
      "type": "EMA",
      "id": "node_168372445591410",
      "name": "EMA-2",
      "options": [
        [
          "lookback",
          8
        ]
      ],
      "state": {},
      "interfaces": [
        [
          "inema",
          {
            "id": "ni_168372445591411",
            "value": None
          }
        ],
        [
          "outema",
          {
            "id": "ni_168372445591412",
            "value": None
          }
        ]
      ],
      "position": {
        "x": 293,
        "y": 269
      },
      "width": 200,
      "twoColumn": False,
      "customClasses": ""
    },
    {
      "type": "compare",
      "id": "node_168372448889816",
      "name": "compare-1",
      "options": [
        [
          "sign",
          ">"
        ]
      ],
      "state": {},
      "interfaces": [
        [
          "IN 1",
          {
            "id": "ni_168372448889817",
            "value": None
          }
        ],
        [
          "IN 2",
          {
            "id": "ni_168372448889818",
            "value": None
          }
        ],
        [
          "Output",
          {
            "id": "ni_168372448889819",
            "value": None
          }
        ]
      ],
      "position": {
        "x": 532,
        "y": 89
      },
      "width": 200,
      "twoColumn": False,
      "customClasses": ""
    },
    {
      "type": "EXE",
      "id": "node_168372449891426",
      "name": "EXE-1",
      "options": [],
      "state": {},
      "interfaces": [
        [
          "buy",
          {
            "id": "ni_168372449891527",
            "value": None
          }
        ],
        [
          "sell",
          {
            "id": "ni_168372449891528",
            "value": None
          }
        ]
      ],
      "position": {
        "x": 1012,
        "y": 128
      },
      "width": 200,
      "twoColumn": False,
      "customClasses": ""
    },
    {
      "type": "NOT",
      "id": "node_168372452182632",
      "name": "NOT-1",
      "options": [],
      "state": {},
      "interfaces": [
        [
          "in",
          {
            "id": "ni_168372452182733",
            "value": None
          }
        ],
        [
          "out",
          {
            "id": "ni_168372452182734",
            "value": None
          }
        ]
      ],
      "position": {
        "x": 758,
        "y": 239
      },
      "width": 200,
      "twoColumn": False,
      "customClasses": ""
    }
  ],
  "connections": [
    {
      "id": "16837244537949",
      "from": "ni_16837244427913",
      "to": "ni_16837244500905"
    },
    {
      "id": "168372448171715",
      "from": "ni_16837244427913",
      "to": "ni_168372445591411"
    },
    {
      "id": "168372449245022",
      "from": "ni_16837244500906",
      "to": "ni_168372448889817"
    },
    {
      "id": "168372449453325",
      "from": "ni_168372445591412",
      "to": "ni_168372448889818"
    },
    {
      "id": "168372450223531",
      "from": "ni_168372448889819",
      "to": "ni_168372449891527"
    },
    {
      "id": "168372452575738",
      "from": "ni_168372448889819",
      "to": "ni_168372452182733"
    },
    {
      "id": "168372453355641",
      "from": "ni_168372452182734",
      "to": "ni_168372449891528"
    }
  ],
  "panning": {
    "x": 0,
    "y": 0
  },
  "scaling": 1
}
############################################################
#session state initialisations
if 'side_bar' not in st.session_state:
    st.session_state['side_bar']='collapsed'
    st.session_state['Dbi']=DBob.DBcon()
    st.session_state['thr_alive']=True
    st.session_state['buy']=True
    st.session_state['price']=None
    st.session_state['data']=None
    st.session_state['data_lookback']=None
    st.session_state['backtest']=0

    


#page config
st.set_page_config(page_title='DEEP DASH',
                    page_icon='📈',
                    layout='wide',
                    initial_sidebar_state=st.session_state['side_bar']
                    )#page configuration





def main():

    st.title('Deep Trade Dashboard')#Title bar
    st.session_state['ASSET']=st.selectbox('select market',                #selecting market using delectbox
                                        ['BTCUSDT','ETHUSDT']
                                        )
    ##############################button render####################################

    st.session_state['Tframe']='1m'

    chaRT=chaRTTY(st.session_state["Tframe"])

    Ema={'EMA1':1,'EMA2':1,'EMA3':1}
    rsi={'RSI1':1}
    Ema['EMA1']=st.number_input('EMA1',min_value=2)
    Ema['EMA2']=st.number_input('EMA2',min_value=2)
    Ema['EMA3']=st.number_input('EMA3',min_value=2)
    rsi['RSI1']=st.number_input('RSI1',min_value=2)
    #######################chart rendering##############################################################
    placeholder=st.empty()
    x=1

    while x:
        with placeholder.container():
            if chaRT.alert:
                x=False
            st.plotly_chart(chaRT.plotty(asset=st.session_state['ASSET'],eMAA=1,ematime=Ema))#render candlestick
            st.plotly_chart(chaRT.plotty2(rse=1,rsitime=rsi))#render rsi
            
            time.sleep(1)

#authentication is doen first then the makn code is exexuted

if st.session_state.side_bar=='collapsed':
        st.markdown(
                """
                <style>
                        [data-testid="collapsedControl"] 
                        {
                        display: none
                        }
                </style>
                """,
                unsafe_allow_html=True,
                )
        
        log0sign=st.selectbox('select',['Login','signup']
                                        )
        if log0sign =='Login':
              st.header('Login')
              usr1=st.text_input('Username',key=1)
              psw1=st.text_input('Password',key=2,type='password')
              if (usr1 !='') & (psw1 !=''):
                    hash_val=hashlib.sha256(psw1.encode()).hexdigest()
                    rec=st.session_state.Dbi.Db.get(usr1)
                    if rec is not None:
                        if rec['pass']==hash_val:
                            st.session_state['side_bar']='auto'
                            st.session_state['usr']=rec['key']
                            st.experimental_rerun()
                        else:
                             st.warning("username or password wrong")
                    else:
                        st.warning("⚠️ user not found/Signup")
              else:
                   st.warning('⚠️ No password or username')
                   
        else:
            st.header('Signup')
            usr2=st.text_input('Username',key=3)
            psw2=st.text_input('Password',key=4)
            if (usr2 !='') & (psw2 !=''):
                try:
                    hash_val=hashlib.sha256(psw2.encode()).hexdigest()
                    st.session_state['Dbi'].Db.insert({'key':usr2,'pass':hash_val})
                    save_schema('simple_strategy',schema_data=simple_strat,user=usr2)
                    st.warning('🙋‍♂️ Welcome,Login to continue')
                except:
                    st.warning('⚠️ User already exist')
            else:
                 st.warning('⚠️ No password or username')
else:
     main()
            
        
        
      


        

    



