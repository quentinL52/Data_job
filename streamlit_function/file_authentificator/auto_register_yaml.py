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

def update_file_content(new_content):
    """Mettre à jour le contenu du fichier YAML sur GitHub."""
    response = requests.get(GITHUB_API_URL, headers={'Authorization': f'token {GITHUB_TOKEN}'})
    response.raise_for_status()
    sha = response.json()['sha']
    
    # Encodez le nouveau contenu YAML en base64
    encoded_content = base64.b64encode(yaml.dump(new_content).encode('utf-8')).decode('utf-8')

    # Préparez les données pour la requête PUT
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