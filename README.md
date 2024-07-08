# ObsidianRAG

ObsidianRAG is a Retrieval-Augmented Generation (RAG) system designed to work with Obsidian vaults. It uses LangChain and OpenAI to provide intelligent responses based on your Obsidian notes.

## Features

- Processes Markdown files from your Obsidian vault
- Builds a vector store for efficient retrieval
- Implements a RAG pipeline for answering queries based on your notes
- Easily extensible for custom use cases

## Prerequisites

- Python 3.8+
- An OpenAI API key
- An Obsidian vault with Markdown files

## Installation

1. Clone this repository:
   ```
   git clone https://github.com/yourusername/ObsidianRAG.git
   cd ObsidianRAG
   ```

2. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```

3. Set up your environment variables:
   - Copy the `.env.example` file to `.env`
   - Open `.env` and fill in your OpenAI API key and the path to your Obsidian vault:
     ```
     OPENAI_API_KEY=your_openai_api_key_here
     DATA_PATH=/path/to/your/obsidian/vault
     CHROMA_PATH=./models/vectorstore/chroma
     ```

## Usage

1. Process your Obsidian notes:
   ```
   python scripts/process_data.py
   ```
   This script will load and split your Markdown files into chunks suitable for embedding.

2. Build the vector store:
   ```
   python scripts/build_vectorstore.py
   ```
   This creates a Chroma vector store from your processed notes.

3. Run the RAG pipeline:
   ```
   python scripts/run_rag.py
   ```
   This starts an interactive session where you can ask questions based on your Obsidian notes.

## Project Structure

- `data/`: Processed data (if any intermediate processing is needed)
- `examples/`: Example scripts demonstrating usage
- `notebooks/`: Jupyter notebooks for exploration and analysis
- `models/vectorstore/chroma/`: Stores the Chroma vector database
- `src/`: Source code for the ObsidianRAG system
  - `data_processing/`: Code for loading and processing Obsidian notes
  - `embeddings/`: Handles document and query embedding
  - `retrieval/`: Manages retrieval from the vector store
  - `rag/`: Implements the RAG pipeline
- `scripts/`: Executable scripts for running different parts of the system

## Customization

You can customize the behavior of ObsidianRAG by modifying the following files:

- `src/data_processing/processor.py`: Adjust how Markdown files are loaded and split
- `src/embeddings/embedder.py`: Change the embedding model or process
- `src/retrieval/retriever.py`: Modify retrieval parameters or methods
- `src/rag/pipeline.py`: Customize the RAG pipeline, e.g., by changing the LLM or chain type

## Contributing

Contributions to ObsidianRAG are welcome! Please feel free to submit a Pull Request.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- [LangChain](https://github.com/hwchase17/langchain) for the powerful LLM tools
- [OpenAI](https://openai.com/) for the language model and embeddings
- [Obsidian](https://obsidian.md/) for the excellent note-taking system