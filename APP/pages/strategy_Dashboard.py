from barfi import barfi_schemas, Block,load_schema_name,manage_schema
import streamlit as st
from streamlit.runtime.scriptrunner import add_script_run_ctx
from streamlit.runtime.scriptrunner.script_run_context import get_script_run_ctx
from APi.appiOb import APi
import time
from threading import Thread
import hashlib
st.header('STRATEGY DASHBOARD')

usr=st.session_state['usr']
comp_ob=st.session_state['compute_obj']
load_schema=st.selectbox('load strategy ',barfi_schemas(usr))
schema_state=load_schema_name(load_schema+'@'+hashlib.sha256(usr.encode()).hexdigest(),usr)
st.write(schema_state)

if st.button('press me'):
    for i in range(0,5):
        comp_ob.add_editor_state(editor_state=schema_state)
        comp_ob._map_block_link()
        comp_ob._execute_compute()
        time.sleep(1)







# def pr():
#     for i in range(10):
#         print(i)
#         time.sleep(1)

# thread = Thread(target=pr)
# add_script_run_ctx(thread)

# if st.button('start thread'):
#     thread.start()


# ce=Compute_obj

# barfi_result=load_schema_name(schema_name=)



# for i in range(0,5):

#     ce.add_editor_state(editor_state=barfi_result)
#     ce._map_block_link()
#     ce._execute_compute()
#     time.sleep(1)



