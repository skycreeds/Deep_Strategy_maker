from tensorflow import keras
import streamlit as st

@st.cache(allow_output_mutation=True)
def load_in_model(model_arch:str):
    if model_arch=='TCN':
        return keras.models.load_model('./TCN_model.h5')
    elif model_arch=='LSTM':
        return keras.models.load_model('./LSTM_model.h5')


    