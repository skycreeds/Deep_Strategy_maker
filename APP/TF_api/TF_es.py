import tensorflow as tf
import streamlit as st
import numpy as np
import os

@st.cache_resource
def load_TCN_model():
            print(os.getcwd())
            return tf.keras.models.load_model('TCN_model.h5')
        #elif _model_arch=='LSTM':
            #return tf.keras.models.load_model('./LSTM_model.h5')
@st.cache_resource
def load_LSTM_model():
      return tf.keras.models.load_model('LSTM_model.h5')
class Tensor_mod:
    def __init__(self) -> None:
          pass
    
    def standardize(self,arr):
          mean=np.mean(arr)
          std=np.std(arr,ddof=2)
          return (arr-mean)/std
    def data_preprocess(self,feeddd,ema6,ema12,ema26):
        print('inside preprocess1')
        # print('emas',ema6,ema12,ema26)
        # print('time',feeddd.index[len(feeddd)-1])
        # print('latestf',feeddd['Close'][len(feeddd)-1])
        feeddd.reset_index(inplace=True)
        time=(feeddd['Time'].values).astype(np.int32)
        param=np.array([time[len(feeddd)-1],feeddd['Volume'][len(feeddd)-1],feeddd['Close'][len(feeddd)-1],ema6,ema12,ema26])
        print(param)
        print('inside preprocess2')
        param=self.standardize(param)
        print(param)
        
        #self.param=self.scaler.transform(self.param)
        # param=self.scaler.fit(param)
        # param=self.scaler.transform(param)
        print('inside preprocess3')
        return param
    
    def predict(self,param,model):
        print('inside predic function')
        return tf.argmax(model.predict(param.reshape((1, 6, 1))),axis=1).numpy()[0]
    
    def data_preprocess_Lstm(self,feeddd,ema6,ema12,ema26):
          pass