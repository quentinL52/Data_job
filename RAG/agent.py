import warnings
warnings.filterwarnings('ignore')

####################  pdf loader, va extraire le texte et retourner un str ###########################
from langchain_community.document_loaders import PyPDFLoader

def pdf_loader(pdf):
    loader = PyPDFLoader(pdf)
    pages = loader.load_and_split()
    pdf_text = ""
    for page in pages:
        pdf_text += page.page_content + "\n"
    return pdf_text

pdf_path = ' '
docu_pdf = pdf_loader(pdf_path)

################## charger le vector store #########################################################

import os
from dotenv import load_dotenv

load_dotenv()
pinecone_api_key = os.getenv("PINECONE_API_KEY")

from langchain_huggingface import HuggingFaceEmbeddings
from langchain_pinecone import PineconeVectorStore

embeddings = HuggingFaceEmbeddings(model_name='sentence-transformers/LaBSE')
vectorstore = PineconeVectorStore(index_name='jobsdata', embedding=embeddings)

################# definir le parser ############################################

from langchain_core.output_parsers import JsonOutputParser
from langchain_core.pydantic_v1 import BaseModel, Field

class Job(BaseModel):
    poste: str = Field(description="the name of the job position")
    contract: str = Field(description="the contract type")
    salary: str = Field(description="the salary for the job")
    link: str = Field(description="url link to the job offer")
    skill: str = Field(description="list of skills for the job offer")

parser = JsonOutputParser(pydantic_object=Job)

############## definir le modele et appeler les differents elements ############################
from langchain_groq import ChatGroq
from langchain_core.prompts import PromptTemplate
retriever = vectorstore.as_retriever()

def chat_groq(t=0, choix="llama3-70b-8192", api=os.getenv('GROQ_API_KEY')):
    return ChatGroq(temperature=t, model_name=choix, groq_api_key=api)

model_chat = chat_groq()

def read_system_prompt(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        return file.read()
file_path = 'prompt_tool_reco_job.txt'
system_prompt = read_system_prompt(file_path)

prompt = PromptTemplate(
    template=system_prompt,
    input_variables=["query"],
    partial_variables={"format_instructions": parser.get_format_instructions()},
)

from langchain_core.runnables import RunnableSequence
rag_chain = RunnableSequence(
    retriever |
    prompt |
    model_chat |
    parser
)

response = rag_chain.invoke(docu_pdf)
import json
response_json = json.dumps(response, ensure_ascii=False, indent=4)
print(type(response_json))
