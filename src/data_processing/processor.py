from langchain_community.document_loaders import DirectoryLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter

class DataProcessor:
    def __init__(self, data_path):
        self.data_path = data_path

    def load_documents(self):
        loader = DirectoryLoader(self.data_path, glob="**/*.md", recursive=True)
        documents = loader.load()
        return documents

    def split_documents(self, documents):
        text_splitter = RecursiveCharacterTextSplitter(
            chunk_size=300,
            chunk_overlap=100,
            length_function=len,
            add_start_index=True,
        )
        chunks = text_splitter.split_documents(documents)
        return chunks