from deta import Deta
import streamlit as st
class DBcon:
    def __init__(self) -> None:
        self.DeTa=Deta(st.secrets['Deta_DB_key'])
        self.Db=self.DeTa.Base('deep_base')
        #self.DrIve=self.DeTa.Drive('Dash_store')

   
        
        
    
   