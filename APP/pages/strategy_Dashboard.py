from barfi import barfi_schemas, Block,load_schema_name,manage_schema
import streamlit as st
#from streamlit.runtime.scriptrunner import add_script_run_ctx
#from streamlit.runtime.scriptrunner.script_run_context import get_script_run_ctx
from APi.appiOb import APi
import time
#from threading import Thread
import hashlib
st.header('STRATEGY DASHBOARD')
st.session_state['backtest']=0
usr=st.session_state['usr']
comp_ob=st.session_state['compute_obj']
load_schema=st.selectbox('💡load strategy ',barfi_schemas(usr))
schema_state=load_schema_name(load_schema+'@'+hashlib.sha256(usr.encode()).hexdigest(),usr)
#st.write(schema_state)
col1,col2=st.columns(2)
with col1:
    quat=st.number_input('enter quantity to trade in each signal',min_value=1)
with col2:
    amt=st.number_input('💰Amount to trade',min_value=1000)



x=False
if st.button('start'):
    x=True
if st.button('stop'):
    x=False
placeholder=st.empty()
act={1:'buy',0:'Hold',-1:'Sell'}
temp=0
delt=0
temp_sig=0
own_quant=0
buy_p=0
temp_amt=amt
profit=0
first_time=1
while x:

    comp_ob.add_editor_state(editor_state=schema_state)
    comp_ob._map_block_link()
    comp_ob._execute_compute()

    
    with placeholder.container():
        col1,col2=st.columns(2)
        col3,col4=st.columns(2)
        #getting price and signal from the strategy
        df=st.session_state['price']
        sig=st.session_state['buy']
        #find change in price
        df=df[len(df)-1]
        if temp==0:
            temp=df
        else:
            delt=temp-df
            temp=df
        #executing function based on signals
        if temp_sig != sig:
            if sig==1:
                #buy
                own_quant=own_quant+quat
                buy_p=df*quat
                amt=amt-(buy_p)
                temp_sig=sig
                first_time=0
               
            elif sig==-1 and not first_time:
                #sell
                profit=(df*quat)-buy_p
                own_quant=own_quant-quat
                amt=amt+(df*quat)
                temp_sig=sig
                
            else:
                #hold
                temp_sig=sig

        amt_change=temp_amt-amt  
        temp_amt=amt   
      

        with col1:
            st.metric(label='💵curent price',value=df,delta=delt)
        with col2:
            st.metric(label='⚡ signal',value=act[sig])
            st.metric(label='quantity',value=own_quant)

        with col3:
            st.metric(label="Current Amount",value=amt,delta=amt_change )
        with col4:
            st.metric(label='📈Profit',value='',delta=profit)

    time.sleep(2)

#always remember the datastructyre is reverse in time that is the cureent price is n-1
