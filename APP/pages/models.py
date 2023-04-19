import streamlit as st
import pandas as pd
import requests as res

st.write(pd.DataFrame(res.post("https://trade07-1-j3584132.deta.app/",headers={"x-api-key":"a0TvWwDmm4GF_oqheWPNEzJV2RPuzzjPijK6jhvwAoVph"},json={'asset':'BTCUSDT','interval':'1m','lookback':'1m'}).json()))