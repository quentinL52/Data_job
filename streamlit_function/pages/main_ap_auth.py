import streamlit as st
from streamlit_function.pages.profil import profil


def ap_auth():

    acceuil_page, profil_page, reco_page, annonces_page = st.tabs(['Acceuil','Profil','Recommandation IA','Annonces'])

    with acceuil_page:
        st.markdown(f'# Bonjour {st.session_state["name"]} !')

        with open('./streamlit_function/pages/texte_acceuil.txt', 'r') as file:
            markdown_text = file.read()

        # Afficher le texte en Markdown
        st.markdown(markdown_text)

    with profil_page:
        profil()
        


