from langchain_nomic.embeddings import NomicEmbeddings
from pinecone import Pinecone as PineconeClient
from pinecone import Pinecone, ServerlessSpec
from langchain_pinecone import PineconeVectorStore
from PDF_loader import pdf_loader
from api import clef_api_nomic, clef_api_pinecone
api_nomic = clef_api_nomic()
api_pinecone = clef_api_pinecone()

pc = Pinecone(api_key=api_pinecone)
index = pc.Index("cv")
documents = pdf_loader("CV_Quentin_Loumeau.pdf")

embeddings = NomicEmbeddings(model="nomic-embed-text-v1.5",nomic_api_key=api_nomic)
embeddings.embed_documents(
    [documents]
)

#docsearch = PineconeVectorStore.add_documents(documents, embeddings, index_name=index,)

