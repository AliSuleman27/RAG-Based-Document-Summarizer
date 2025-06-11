# pipeline.py
from langchain.text_splitter import RecursiveCharacterTextSplitter
from config import Config
from retriever import Retriever
from summarizer import Summarizer
from document_parser import DocumentParser
from typing import Dict, Any

class SummarizationPipeline:
    def __init__(self):
        self.retriever = Retriever()
        self.summarizer = Summarizer()
        self.splitter = RecursiveCharacterTextSplitter(
            chunk_size=Config.CHUNK_SIZE,
            chunk_overlap=Config.CHUNK_OVERLAP
        )

    def extract_text(self, file):
        try:
            parser = DocumentParser.get_parser(file)
            return parser.extract_text(file)
        except Exception as e:
            raise ValueError(f"Error processing document: {str(e)}")

    def run(self, file, text=None) -> Dict[str, Any]:
        # 1. Extract text
        if not text:
            text = self.extract_text(file)

        # 2. Split into chunks
        chunks = self.splitter.split_text(text)

        # 3. Create vector index
        self.retriever.create_index(chunks)

        # 4. Retrieve relevant chunks
        query = "Provide a comprehensive summary of this document"
        docs = self.retriever.retrieve(query, k=5)
        context = "\n\n".join([doc.page_content for doc in docs])

        # 5. Generate summary and get token usage
        summary_result = self.summarizer.summarize(context)

        return {
            "summary": summary_result["summary"],
            "context_chunks": [doc.page_content for doc in docs],
            "token_usage": summary_result["token_usage"],
            "chunk_count": len(chunks),
            "processed_text_length": len(text)
        }