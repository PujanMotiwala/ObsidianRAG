from src.data_processing.processor import DataProcessor

def main():
    processor = DataProcessor()
    documents = processor.load_documents()
    splits = processor.split_documents(documents)
    print(f"Processed {len(documents)} documents into {len(splits)} chunks.")

if __name__ == "__main__":
    main()