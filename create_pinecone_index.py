from pinecone import Pinecone as PineconeClient
from pinecone import Pinecone, ServerlessSpec
import time
import os
from dotenv import load_dotenv

# Charge les variables d'environnement du fichier .env
load_dotenv()
api_pinecone = os.getenv("CLEF_API_PINECONE")


pc = Pinecone(api_key=api_pinecone)


def creer_index(nom):
    index_name = nom  

    existing_indexes = [index_info["name"] for index_info in pc.list_indexes()]

    if index_name not in existing_indexes:
        # fonction qui sert a creer un index 
        pc.create_index(
            name=index_name, # le nom de l'index
            dimension=256, # le nombre de vecteur de l'index
            metric="cosine", # la metrique de calcul des vecteurs
            spec=ServerlessSpec(cloud="aws", region="us-east-1"), # les infos du serveur du vector store
        )
        while not pc.describe_index(index_name).status["ready"]:
            time.sleep(1)

    index = pc.Index(index_name)
    return index

if __name__ == "__main__":
    creer_index("coucou")
