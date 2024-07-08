from langchain_community.vectorstores import Chroma
from langchain_openai import OpenAIEmbeddings, ChatOpenAI
from langchain.prompts import ChatPromptTemplate
import os


CHROMA_PATH = os.environ['CHROMA_PATH']

PROMPT_TEMPLATE = """
Answer the question based only on the following context:

{context}

---

Answer the question based on the above context: {question}
"""

class RAGPipeline:
    def __init__(self):
        embedding_function = OpenAIEmbeddings()
        self.db = Chroma(persist_directory=CHROMA_PATH, embedding_function=embedding_function)
        self.model = ChatOpenAI()
        self.prompt_template = ChatPromptTemplate.from_template(PROMPT_TEMPLATE)

    def run(self, query):
        results = self.db.similarity_search_with_relevance_scores(query, k=3)
        if len(results) == 0 or results[0][1] < 0.7:
            return "Unable to find matching results."

        context_text = "\n\n---\n\n".join([doc.page_content for doc, _score in results])
        prompt = self.prompt_template.format(context=context_text, question=query)
        response_text = self.model.invoke(prompt)

        sources = [doc.metadata.get("source", None) for doc, _score in results]
        return f"Response: {response_text}\nSources: {sources}"