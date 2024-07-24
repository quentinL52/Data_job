import streamlit as st
from streamlit_function.file_authentificator.manage_log import login_page
from streamlit_function.background_image import background_image
from streamlit_function.pages.main_ap_auth import ap_auth
import streamlit_authenticator as stauth
from streamlit_function.file_authentificator.cryptography_users import decrypt_yaml, encrypt_yaml
import yaml


background_image()

with open("users.yaml", 'r') as file:
    data = yaml.safe_load(file)
        
# Creating the authenticator object
st.session_state.authenticator = stauth.Authenticate(
    st.session_state.config['credentials'],
    st.session_state.config['cookie']['name'],
    st.session_state.config['cookie']['key'],
    st.session_state.config['cookie']['expiry_days'],
    st.session_state.config['pre-authorized']
)


if not st.session_state["authentication_status"]:
    login_page()    

elif st.session_state["authentication_status"]: 
    #lieu personnel utilisateur
    ap_auth()
        

elif st.session_state["authentication_status"] is False:
    st.error('Username/password is incorrect')

elif st.session_state["authentication_status"] is None:
    st.warning('Please enter your username and password')

with open("users.yaml", 'w') as file:
    yaml.dump(st.session_state.config, file, default_flow_style=False, allow_unicode=True)


