import tensorflow as tf
import streamlit as st
import numpy as np
import os

@st.cache_resource
def load_TCN_model():
           
            return tf.keras.models.load_model("/app/deep_strategy_maker/APP/TF_api/TCN_model.h5")
     
@st.cache_resource
def load_LSTM_model():
      return tf.keras.models.load_model("/app/deep_strategy_maker/APP/TF_api/LSTM_model.h5")
class Tensor_mod:
    def __init__(self) -> None:
          pass
    
    def standardize(self,arr):
          mean=np.mean(arr)
          std=np.std(arr,ddof=2)
          return (arr-mean)/std
    def data_preprocess(self,feeddd,ema6,ema12,ema26):

        feeddd.reset_index(inplace=True)
        time=(feeddd['Time'].values).astype(np.int32)
        param=np.array([time[len(feeddd)-1],feeddd['Volume'][len(feeddd)-1],feeddd['Close'][len(feeddd)-1],ema6[len(ema6)-1],ema12[len(ema12)-1],ema26[len(ema26)-1]])
        print(param)
       
        param=self.standardize(param)
        print(param)
        
       
        return param
    
    def predict(self,param,model):
        
        return tf.argmax(model.predict(param.reshape((1, 6, 1))),axis=1).numpy()[0]
    
    def data_preprocess_Lstm(self,feeddd,ema6,ema12,ema26):
        feeddd.reset_index(inplace=True)
        
        time=(feeddd['Time'].values).astype(np.int32)
       
        param=[[]]
        for i in range(1,5):
              param[0].append([time[len(feeddd)-i],feeddd['Volume'][len(feeddd)-i],feeddd['Close'][len(feeddd)-i],ema6[len(ema6)-i],ema12[len(ema12)-i],ema26[len(ema26)-i]])
       
        param=self.standardize(param)
        return param
    
    def LSTM_predict(self,param,model):
          return tf.argmax(model.predict(param)).numpy()[0]
