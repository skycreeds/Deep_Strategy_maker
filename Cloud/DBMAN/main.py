from flask import Flask,jsonify,request
from binance import Client
import pandas as pd

api_key="RPMoUjlXHyhmZ1rSAvVx89iWWS5ENczsxNHWGv67i7zY1OLr8gxPdZevmXQg7Guj"
api_secret="Vwk6pemdQIfF8vkjNYMGqegB9sLXw24ITrVv9FHBCWTINzpTcciOQv27peCX9cyO"
client = Client(api_key, api_secret)

app = Flask(__name__)

@app.route('/', methods=["POST"])
def hello_world():
    dat=request.get_json()
    return client.get_historical_klines(dat['asset'],dat['interval'],dat['lookback'])
    
    