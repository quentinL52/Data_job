import os
from dotenv import load_dotenv
from langchain_community.embeddings import SentenceTransformerEmbeddings
# from langchain.embeddings import SentenceTransformerEmbeddings
pinecone_api_key = os.getenv("PINECONE_API_KEY")
groq_api = os.getenv('GROQ_API_KEY')
load_dotenv()
import langchain
from langchain_groq import ChatGroq
from pinecone import Pinecone, ServerlessSpec
from langchain_pinecone import PineconeVectorStore  
from typing import List
from langchain_core.runnables import RunnablePassthrough
from langchain_core.messages import HumanMessage, SystemMessage, AIMessage
from langchain_core.prompts import PromptTemplate,ChatPromptTemplate, MessagesPlaceholder
from langchain_core.output_parsers import StrOutputParser, JsonOutputParser
import warnings
warnings.filterwarnings('ignore')

from langchain_community.embeddings import SentenceTransformerEmbeddings
embeddings = SentenceTransformerEmbeddings(model_name='sentence-transformers/LaBSE')
vectorstore = PineconeVectorStore(index_name='jobsdata', embedding=embeddings)

def read_system_prompt(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        return file.read()
file_path = 'prompt_experimental.txt'
system_prompt = read_system_prompt(file_path)

from langchain_community.document_loaders import PyPDFLoader
def charger_pdf(pdf):
    loader = PyPDFLoader(pdf)
    pages = loader.load_and_split()

    return pages
pdf_path = 'quentin loumeau cv.pdf'
docu_pdf = charger_pdf(pdf_path)

def chat_groq(t = 0, choix ="llama3-8b-8192", api = os.getenv('GROQ_API_KEY') ) :
  return ChatGroq(temperature = t, model_name=choix,groq_api_key = api)
model_chat = chat_groq()

retrier = vectorstore.as_retriever()
prompt = ChatPromptTemplate.from_messages([("human", system_prompt)])

rag_chain = {"context": retrier, "question": RunnablePassthrough()} | prompt | model_chat
r = rag_chain.invoke("donne moi les 3 skills les plus presente dans les annonces")
 
print(r.content)