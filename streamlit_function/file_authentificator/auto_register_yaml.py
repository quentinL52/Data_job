import streamlit as st
import yaml
import requests
import json
import base64

# Configuration de base
GITHUB_REPO = 'quentinL52/Data_job'
FILE_PATH = 'users.yaml'
GITHUB_API_URL = f'https://api.github.com/repos/{GITHUB_REPO}/contents/{FILE_PATH}'
GITHUB_TOKEN = st.secrets["GITHUB_TOKEN"]

def get_file_content():
    """Obtenir le contenu du fichier YAML depuis GitHub."""
    response = requests.get(GITHUB_API_URL, headers={'Authorization': f'token {GITHUB_TOKEN}'})
    response.raise_for_status()
    content = response.json()
    # Décoder le contenu base64 en texte
    file_content = base64.b64decode(content['content']).decode('utf-8')
    return yaml.safe_load(file_content)

def update_file_content(new_content):
    """Mettre à jour le contenu du fichier YAML sur GitHub."""
    response = requests.get(GITHUB_API_URL, headers={'Authorization': f'token {GITHUB_TOKEN}'})
    response.raise_for_status()
    sha = response.json()['sha']

    # Convertir le contenu YAML en texte puis en base64
    new_content_text = yaml.dump(new_content)
    encoded_content = base64.b64encode(new_content_text.encode('utf-8')).decode('utf-8')

    # Préparer les données pour la requête PUT
    update_data = {
        "message": "Update YAML file via Streamlit app",
        "content": encoded_content,
        "sha": sha
    }

    response = requests.put(GITHUB_API_URL, 
                            headers={'Authorization': f'token {GITHUB_TOKEN}'},
                            data=json.dumps(update_data))
    response.raise_for_status()
    print(response.json())