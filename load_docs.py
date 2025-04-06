from langchain_community.document_loaders import TextLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_google_genai import GoogleGenerativeAIEmbeddings
from langchain_community.vectorstores import FAISS
import os

def load_vectorstore(files: list[str], api_key: str):
    
    all_chunks = []
    
    for file in files:
        loader = TextLoader(file)
        docs = loader.load()

        splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=100)
        chunks = splitter.split_documents(docs)
        all_chunks.extend(chunks)

    embedding = GoogleGenerativeAIEmbeddings(
        model="models/embedding-001",
        google_api_key=api_key
    )

    vectorstore = FAISS.from_documents(all_chunks, embedding)
    return vectorstore
