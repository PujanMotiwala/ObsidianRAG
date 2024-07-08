from langchain_openai import OpenAIEmbeddings

class Embedder:
    def __init__(self):
        self.embedding_model = OpenAIEmbeddings()

    def embed_documents(self, documents):
        return self.embedding_model.embed_documents([doc.page_content for doc in documents])

    def embed_query(self, query):
        return self.embedding_model.embed_query(query)