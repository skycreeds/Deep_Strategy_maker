import time,json,requests
import numpy as np  
import pandas as pd 
import plotly.express as px  
import streamlit as st 
from APi import DBob
from Pcomponents.charting import chaRTTY
import hashlib
#################################################################
import subprocess
import os

package_path = os.path.join(os.path.dirname(__file__), 'barfi')

# Install the package using pip
subprocess.check_call(['python3',package_path,'install'])

###################################################################################

#session state initialisations
if 'side_bar' not in st.session_state:
    st.session_state['side_bar']='collapsed'
    st.session_state['Dbi']=DBob.DBcon()
    


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
            st.plotly_chart(chaRT.plotty(asset=st.session_state['ASSET'],eMAA=1,ematime=Ema))
            st.plotly_chart(chaRT.plotty2(rse=1,rsitime=rsi))
            
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
              psw1=st.text_input('Password',key=2)
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
                    st.warning('🙋‍♂️ Welcome,Login to continue')
                except:
                    st.warning('⚠️ User already exist')
            else:
                 st.warning('⚠️ No password or username')
else:
     main()
            
        
        
      


        

    



