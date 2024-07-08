import os
from dotenv import load_dotenv
from langchain_community.vectorstores import Chroma
from langchain_openai import OpenAIEmbeddings

load_dotenv()

class Retriever:
    def __init__(self):
        self.chroma_path = os.getenv('CHROMA_PATH')
        self.embedding_model = OpenAIEmbeddings()
        self.vectorstore = Chroma(persist_directory=self.chroma_path, embedding_function=self.embedding_model)

    def retrieve(self, query, k=4):
        return self.vectorstore.similarity_search(query, k=k)