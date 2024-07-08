from src.rag.pipeline import RAGPipeline

def main():
    pipeline = RAGPipeline()
    while True:
        query = input("Enter your question (or 'quit' to exit): ")
        if query.lower() == 'quit':
            break
        response = pipeline.run(query)
        print(f"Response: {response}")

if __name__ == "__main__":
    main()