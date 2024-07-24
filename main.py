import streamlit as st
from streamlit_function.file_authentificator.manage_log import login_page
from streamlit_function.background_image import background_image
from streamlit_function.pages.main_ap_auth import ap_auth
import streamlit_authenticator as stauth
from streamlit_function.file_authentificator.cryptography_users import decrypt_yaml, encrypt_yaml


background_image()

# Charger la clé de chiffrement
key = st.secrets['ENCRYPTED_YAML']

# Charger et déchiffrer le fichier YAML
st.session_state.config = decrypt_yaml(key)
        
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

# Chiffrer et enregistrer les nouvelles données dans le fichier YAML
encrypt_yaml(st.session_state.config, key)


