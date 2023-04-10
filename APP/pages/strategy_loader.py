from barfi import st_barfi, barfi_schemas, Block,ComputeEngine,load_schema_name
import streamlit as st
from APi.appiOb import APi
import time
from pages.stategy_maker import Compute_obj
ce=Compute_obj
st.write(barfi_schemas())
barfi_result=load_schema_name(schema_name='sample')



for i in range(0,5):

    ce.add_editor_state(editor_state=barfi_result)
    ce._map_block_link()
    ce._execute_compute()
    time.sleep(1)