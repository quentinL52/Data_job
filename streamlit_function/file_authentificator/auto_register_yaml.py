import streamlit as st
import yaml
import requests
import json


def update_file_content(new_content,file_path):
    # Configuration de base
    GITHUB_REPO = 'quentinL52/Data_job'
    FILE_PATH = file_path
    GITHUB_API_URL = f'https://api.github.com/repos/{GITHUB_REPO}/contents/{FILE_PATH}'
    GITHUB_TOKEN = st.secrets["GITHUB_TOKEN"]
    """Mettre à jour le contenu du fichier YAML sur GitHub."""
    response = requests.get(GITHUB_API_URL, headers={'Authorization': f'token {GITHUB_TOKEN}'})
    response.raise_for_status()
    sha = response.json()['sha']
    
    # Convertir le contenu YAML en texte
    new_content_text = yaml.dump(new_content)

    # Préparez les données pour la requête PUT
    update_data = {
        "message": "Update YAML file via Streamlit app",
        "content": new_content_text,
        "sha": sha
    }

    response = requests.put(GITHUB_API_URL, 
                            headers={'Authorization': f'token {GITHUB_TOKEN}'},
                            data=json.dumps(update_data))
    response.raise_for_status()
    print(response.json())