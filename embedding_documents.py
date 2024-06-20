from langchain_core.output_parsers import StrOutputParser
from langchain_nomic import NomicEmbeddings
from langchain_core.runnables import RunnableParallel, RunnablePassthrough, RunnableLambda
from pinecone import Pinecone, ServerlessSpec
from langchain_pinecone import PineconeVectorStore
from langchain_core.output_parsers import StrOutputParser
from PDF_loader import pdf_loader
import os
from dotenv import load_dotenv

# Charge les variables d'environnement du fichier .env
load_dotenv()
api_nomic = os.getenv("CLEF_API_NOMIC")
api_pinecone = os.getenv("CLEF_API_PINECONE")

cv_text = pdf_loader("")

def vecto_cv(cv_texts):
    embeddings = NomicEmbeddings(model="nomic-embed-text-v1.5")
    vectorstore = PineconeVectorStore(index_name='cv', embedding=embeddings,pinecone_api_key=api_pinecone)
    cv_texts = [doc.page_content for doc in cv_text]
    vectorstore.add_texts(cv_texts)
    print('added to the index')

if __name__ == "__main__":
    vecto_cv(cv_text)
