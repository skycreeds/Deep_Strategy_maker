import streamlit as st
import talib as Tb
from APi.appiOb import APi
from barfi import st_barfi, barfi_schemas, Block,compute_engine
from TF_api.TF_es import Tensor_mod
from TF_api import TF_es
#####################################################
st.session_state['backtest']=0
Tensor_mod=Tensor_mod()
tcn_model=TF_es.load_TCN_model()
lstm_model=TF_es.load_LSTM_model()
######################################################
feed = Block(name='Data Feed')
feed.add_output(name='outdatafeed')
feed.add_option(name='TFrame',type='select',items=['1m','1d'],value='1m')
feed.add_option(name='MAX_lookback',type='integer')
def feed_func(self):
    self.api=APi()
    print('in feeder')
    Tfr=self.get_option(name='TFrame')
    lokb=str(self.get_option(name='MAX_lookback'))
    print('in feeder2 ')
    if st.session_state['backtest']:
        print('backtest mode')
        jk=st.session_state['data']
    else:
        print('api mode')
        jk=self.api.getminutedata('BTCUSDT',Tfr,lokb+'m')
        print('api mode2')
    print('in feeder ouside modes')
    st.session_state['price']=jk['Close']
    self.set_interface(name='outdatafeed', value=jk)
feed.add_compute(feed_func)
########################################################################
RsI = Block(name='RSI')
RsI.add_input(name='inrsi')
RsI.add_output(name='outrsi')
RsI.add_option(name='lookback',type='integer')
def RsI_func(self):
    print(458)
    lokk=self.get_option(name='lookback')
    in_0 = self.get_interface(name='inrsi')
    out_2=Tb.RSI(in_0['Close'],timeperiod=lokk)
    print(345)
    print('RSI',out_2)
    self.set_interface(name='outrsi', value=out_2)   
RsI.add_compute(RsI_func)
######################################################################
Ema=Block(name='EMA')
Ema.add_input(name='inema')
Ema.add_output(name='outema')
Ema.add_option(name='lookback',type='integer')
def Ema_func(self):
    print('ema1')
    lokk=self.get_option(name='lookback')
    print('ema2')
    in_1 = self.get_interface(name='inema')
    print('ema3')
    out3=Tb.EMA(in_1['Close'],timeperiod=lokk)
    print('ema4')
    print('EMA'+str(lokk),out3[len(out3)-1])
    self.set_interface(name='outema', value=out3)
Ema.add_compute(Ema_func)
#######################################################################
GRoLS=Block(name='compare')
GRoLS.add_input(name='IN 1')
GRoLS.add_input(name='IN 2')
GRoLS.add_output(name='Output')
GRoLS.add_option(name='sign',type='select',items=['>','<'],value='>')
def COmp_func(self):
    print('comp func')
    in_1=self.get_interface(name='IN 1')
    in_2=self.get_interface(name='IN 2')
    opt=self.get_option(name='sign')
    if opt=='>':
        if in_1[len(in_1)-1]>in_2[len(in_2)-1]:
            self.set_interface(name='Output', value=True)
        else:
            self.set_interface(name='Output', value=False)
    else:
        if in_1[len(in_1)-1]<in_1[len(in_1)-1]:
            self.set_interface(name='Output', value=True)
        else:
            self.self.set_interface(name='Output', value=False)
GRoLS.add_compute(COmp_func)
######################################################################
And=Block(name="AND")
And.add_input(name='in1')
And.add_input(name='in2')
And.add_output(name='out1')

def And_func(self):
    print('and block')
    in_1=self.get_interface(name='in1')
    in_2=self.get_interface(name='in2')
    if in_1 & in_2:
        self.set_interface(name='out1',value=True)
    else:
        self.set_interface(name='out1',value=False)
And.add_compute(And_func)
#####################################################################
Orr=Block(name="OR")
Orr.add_input(name='in1')
Orr.add_input(name='in2')
Orr.add_output(name='out1')

def Orr_func(self):
    print('or block')
    in_1=self.get_interface(name='in1')
    in_2=self.get_interface(name='in2')
    if in_1 | in_2:
        self.set_interface(name='out1',value=True)
    else:
        self.set_interface(name='out1',value=False)
Orr.add_compute(Orr_func)
########################################################################
testBlock=Block(name='testBlock')
testBlock.add_input(name="inn")
def testBlock_func(self):
    print('qwqwqwqwqwqwqwqwqqwqw',self.get_interface(name="inn"))
testBlock.add_compute(testBlock_func)
######################################################################
exe = Block(name='EXE')
exe.add_input(name='buy')
exe.add_input(name='sell')
#exe.add_option(name='Quantinty',type='integer')
def exe_func(self):
   print('oppopopopopopopopoppopopopopopopoppopopopopopopopopop')
   if self.get_interface(name='buy'):
       st.session_state['buy']=1
   elif self.get_interface(name='sell'):
       st.session_state['buy']=-1
   else:
       st.session_state['buy']=0   
   
exe.add_compute(exe_func)
#############################################################################
true=Block(name='True/False')
true.add_output(name='out')
true.add_option(name='ops',type='checkbox')
def true_func(self):
    print('t/f')
    if self.get_option(name='ops'):
        self.set_interface(name='out',value=True)
    else:
        self.set_interface(name='out',value=False)
true.add_compute(true_func)
##############################################################################
number=Block('number')
number.add_output(name='out')
number.add_option(name='number',type='integer')
def number_func(self):
    self.set_interface(name='out',value=self.get_option(name='number'))
    print('number block')
number.add_compute(number_func)

###############################################################################
noti=Block('NOT')
noti.add_input(name='in')
noti.add_output(name='out')
def noti_func(self):
    self.set_interface(name='out',value=not self.get_interface(name='in'))
    print('not block')
noti.add_compute(noti_func)
##############################################################################
#<----model blocks------->
###############################################################################
#<--------------------------------TCN model------------------------------->
Tcn=Block('TCN model')
Tcn.add_input(name='datafeed')
Tcn.add_input(name='ema6')
Tcn.add_input(name='ema12')
Tcn.add_input(name='ema26')
Tcn.add_output(name='signal')
def Tcn_func(self):
    #print('inside tcn model function1')
    feeddd = self.get_interface(name='datafeed')
    #print('inside tcn model function2')
    ema6=self.get_interface(name='ema6')
    #print('inside tcn model function3')
    ema12=self.get_interface(name='ema12')
    #print('inside tcn model function4')
    ema26=self.get_interface(name='ema26')
    #print('inside tcn model function5')
    dat=Tensor_mod.data_preprocess(feeddd=feeddd,ema6=ema6,ema12=ema12,ema26=ema26)
    #print('inside tcn model function6')
    self.set_interface(name='signal',value=Tensor_mod.predict(param=dat,model=tcn_model))
    #print('inside tcn model function7')
Tcn.add_compute(Tcn_func)
#######################################################################################################
#<---------------------------LSTM---------------------------------------------->
Lstm=Block('LSTM model')
Lstm.add_input(name='datafeed')
Lstm.add_input(name='ema6')
Lstm.add_input(name='ema12')
Lstm.add_input(name='ema26')
Lstm.add_output(name='signal')
def Lstm_fuc(self):
    print('inside lstm model function1')
    feeddd = self.get_interface(name='datafeed')
    print('inside lstm model function2')
    ema6=self.get_interface(name='ema6')
    print('inside lstm model function3')
    ema12=self.get_interface(name='ema12')
    print('inside lstm model function4')
    ema26=self.get_interface(name='ema26')
    print('inside lstm model function5')
    dat=Tensor_mod.data_preprocess_Lstm(feeddd=feeddd,ema6=ema6,ema12=ema12,ema26=ema26)
    print('inside lstm model function6')
    self.set_interface(name='signal',value=Tensor_mod.LSTM_predict(param=dat,model=lstm_model))
Lstm.add_compute(Lstm_fuc)
###############################################################################
###############################################################################
#<--widgets arrangements-->

usr=st.session_state['usr']
load_schema = st.selectbox('Select a saved schema:', barfi_schemas(usr))


# compute_engine = st.checkbox('Activate barfi compute engine', value=False)
st.session_state['compute_obj']=compute_engine.ComputeEngine([feed,RsI,exe,Ema,GRoLS,And,Orr,testBlock,true,number,noti,Tcn,Lstm])

barfi_result = st_barfi(base_blocks=[feed,RsI,exe,Ema,GRoLS,And,Orr,testBlock,true,number,noti,Tcn,Lstm],
                    compute_engine=True ,load_schema=load_schema,user=usr)
st.write(barfi_result)


