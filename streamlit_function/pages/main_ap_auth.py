import streamlit as st
import json
from streamlit_function.pages.profil import profil
from streamlit_function.pages.load_model_ia import reco_annonce_job
from streamlit_function.pages.chat import chat
from streamlit_function.file_authentificator.manage_log import reset_password

def ap_auth():

    acceuil_page, profil_page, reco_page, annonces_page = st.tabs(['Acceuil','Profil','Recommandation IA','Annonces'])

    with acceuil_page:
        st.markdown(f'# Bonjour {st.session_state["name"]} !')

        with open('./streamlit_function/pages/texte_acceuil.txt', 'r') as file:
            markdown_text = file.read()

        # Afficher le texte en Markdown
        st.markdown(markdown_text)

    with profil_page:
        info_perso, reset_password_users = st.tabs(['Informations personelles','Nouveau mot de passe'])
        with info_perso:
            profil()
        with reset_password_users:
            reset_password()


    with reco_page:
        chat()

    with annonces_page:
        json_str = json.dumps(st.session_state["config"]["credentials"]["usernames"][st.session_state["username"]])
        json_reco = reco_annonce_job(json_str)

        for dico in json_reco:

            st.markdown(f"""
            ## {dico["entreprise"]}
            ### {dico["poste"]}

            #### Contrat : {dico['contract']}
            #### Skills : {dico['skill']}
            #### [{"Lien de l'annonce"}]({dico['link']})

            ---
            """)
        





