from langchain_community.document_loaders import PyPDFLoader

def pdf_loader(pdf):
    loader = PyPDFLoader(pdf)
    pages = loader.load_and_split()

    return pages


