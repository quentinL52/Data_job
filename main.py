import os
import subprocess
import sys

# Ajouter le répertoire contenant vos modules personnalisés au chemin de recherche de Python
sys.path.append('/mount/src/data_job/')

# Installer Chromium
def install_chromium():
    subprocess.run(['apt-get', 'update'], check=True)
    subprocess.run(['apt-get', 'install', '-y', 'chromium-browser'], check=True)
    # Créer un lien symbolique pour Google Chrome
    if not os.path.exists('/usr/bin/google-chrome'):
        os.symlink('/usr/bin/chromium-browser', '/usr/bin/google-chrome')

# Appeler la fonction d'installation de Chromium
install_chromium()


import streamlit as st
from streamlit_function.file_authentificator.manage_log import login_page, reset_password
from streamlit_function.file_authentificator.yaml_config import yaml_config
from apscheduler.schedulers.background import BackgroundScheduler   
from scraping.main_scrap import update



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


# Initialiser le scheduler
scheduler = BackgroundScheduler()

# Planifier la tâche pour s'exécuter tous les jours à la même heure
scheduler.add_job(update, 'cron', hour=20, minute=00)

# Démarrer le scheduler
scheduler.start()