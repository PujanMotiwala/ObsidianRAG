import os
from dotenv import load_dotenv
from langchain_community.vectorstores import Chroma
from langchain_openai import OpenAIEmbeddings
from src.data_processing.processor import DataProcessor

load_dotenv()

def main():
    processor = DataProcessor()
    documents = processor.load_documents()
    splits = processor.split_documents(documents)

    embedding_model = OpenAIEmbeddings()
    chroma_path = os.getenv('CHROMA_PATH')
    
    vectorstore = Chroma.from_documents(
        documents=splits,
        embedding=embedding_model,
        persist_directory=chroma_path
    )
    vectorstore.persist()
    print(f"Vector store built and saved to {chroma_path}")

if __name__ == "__main__":
    main()