import streamlit as st
import yaml
from yaml.loader import SafeLoader
import streamlit_authenticator as stauth


def yaml_config():
    # Loading config file
    with open('./users.yaml', 'r', encoding='utf-8') as file:
            st.session_state.config = yaml.load(file, Loader=SafeLoader)

    # Creating the authenticator object
    st.session_state.authenticator = stauth.Authenticate(
        st.session_state.config['credentials'],
        st.session_state.config['cookie']['name'],
        st.session_state.config['cookie']['key'],
        st.session_state.config['cookie']['expiry_days'],
        st.session_state.config['pre-authorized']
    )
    
    # Saving config file
    with open('./users.yaml', 'w', encoding='utf-8') as file:
        yaml.dump(st.session_state.config, file, default_flow_style=False)