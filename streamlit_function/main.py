import streamlit as st
from streamlit_authenticator.utilities.exceptions import CredentialsError, ForgotError, LoginError, RegisterError, ResetError, UpdateError 
from file_python.manage_log import login_page, reset_password
from file_python.yaml_config import yaml_config



yaml_config()


if not st.session_state["authentication_status"]:
    login_page()

elif st.session_state["authentication_status"]:
    st.write(f'Welcome *{st.session_state["name"]}*')
    if st.session_state.config['credentials']['usernames'][st.session_state["username"]]["Forgot"]:
        reset_password()

elif st.session_state["authentication_status"] is False:
    st.error('Username/password is incorrect')

elif st.session_state["authentication_status"] is None:
    st.warning('Please enter your username and password')
st.write(st.session_state.config)


st.write(st.session_state)