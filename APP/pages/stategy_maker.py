import streamlit as st
import talib as Tb
from APi.appiOb import APi
from ..barfi import st_barfi, barfi_schemas, Block
#####################################################
######################################################
feed = Block(name='Data Feed')
feed.add_output()
feed.add_option(name='TFrame',type='select',items=['1m','1d'],value='1m')
feed.add_option(name='MAX_lookback',type='integer')
def feed_func(self):
    self.api=APi()
    print(123)
    Tfr=self.get_option(name='TFrame')
    print(Tfr)
    lokb=str(self.get_option(name='MAX_lookback'))
    print(lokb)
    jk=self.api.getminutedata('BTCUSDT',Tfr,lokb+'m')
    print(456)
    self.set_interface(name='Output 1', value=jk)
feed.add_compute(feed_func)
########################################################################
RsI = Block(name='RSI')
RsI.add_input()
RsI.add_output()
RsI.add_option(name='lookback',type='integer')
def RsI_func(self):
    lokk=self.get_option(name='lookback')
    print(458)

    in_0 = self.get_interface(name='Input 1')
    out_2=Tb.RSI(in_0['Close'],timeperiod=lokk)
    print(345)
    print(out_2)
    self.set_interface(name='Output', value=out_2[lokk])   
RsI.add_compute(RsI_func)
######################################################################
Ema=Block(name='EMA')
Ema.add_input()
Ema.add_output()
Ema.add_option(name='lookback',type='integer')
def Ema_func(self):
    lokk=self.get_option(name='lookback')
    in_0 = self.get_interface(name='Input 1')
    out3=Tb.EMA(in_0['Close'],timeperiod=lokk)
    self.set_interface(name='Output', value=out3[lokk])
RsI.add_compute(Ema_func)
#######################################################################
GRoLS=Block(name='compare')
GRoLS.add_input(name='IN 1')
GRoLS.add_input(name='IN 2')
GRoLS.add_output()
GRoLS.add_option(name='sign',type='select',items=['>','<'],value='>')
def COmp_func(self):
    in_1=self.get_interface(name='IN 1')
    in_2=self.get_interface(name='IN 2')
    opt=self.get_option(name='sign')
    if opt=='>':
        if in_1>in_2:
            self.self.set_interface(name='Output', value=True)
        else:
            self.self.set_interface(name='Output', value=False)
    else:
        if in_1<in_2:
            self.self.set_interface(name='Output', value=True)
        else:
            self.self.set_interface(name='Output', value=False)
GRoLS.add_compute(COmp_func)
######################################################################
And=Block(name="AND")
And.add_input(name='in1')
And.add_input(name='in2')
And.add_output(name='out1')

def And_func(self):
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
    in_1=self.get_interface(name='in1')
    in_2=self.get_interface(name='in2')
    if in_1 | in_2:
        self.set_interface(name='out1',value=True)
    else:
        self.set_interface(name='out1',value=False)
Orr.add_compute(And_func)
########################################################################





######################################################################
result = Block(name='Result')
result.add_input()
def result_func(self):
    in_1 = self.get_interface(name='Input 1')
    print(in_1)
result.add_compute(result_func)
#############################################################################

#<--widgets arrangements-->

usr=st.session_state['usr']
load_schema = st.selectbox('Select a saved schema:', barfi_schemas(usr))


# compute_engine = st.checkbox('Activate barfi compute engine', value=False)

barfi_result = st_barfi(base_blocks=[feed,RsI,result,Ema,GRoLS,And,Orr],
                    compute_engine=False ,load_schema=load_schema,user=usr)
st.write(barfi_result)


