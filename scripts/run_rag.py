import os
import sys

# Add the project root directory to the Python path
project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.insert(0, project_root)

from src.rag.pipeline import RAGPipeline

def main():
    pipeline = RAGPipeline()
    while True:
        query = input("Enter your question (or 'quit' to exit): ")
        if query.lower() == 'quit':
            break
        response = pipeline.run(query)
        print(response)
        print("\n" + "="*50 + "\n")

if __name__ == "__main__":
    main()