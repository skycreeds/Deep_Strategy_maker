from deta import Deta
import streamlit as st
#for database connection of deta base
class DBcon:
    def __init__(self) -> None:
        self.DeTa=Deta('key***********')
        self.Db=self.DeTa.Base('Database******8')
        #self.DrIve=self.DeTa.Drive('Dash_store')

   
        
        
    
   