from langchain.vectorstores import FAISS
from langchain.schema import Document
from typing import List
from config import Config
from embeddings import EmbeddingManager

class Retriever:
    def __init__(self):
        self.embedding_manager = EmbeddingManager()
        self.vector_store = None
    
    def create_index(self, chunks: List[str], metadata: List[dict] = None):
        docs = [
            Document(page_content=chunk, metadata=meta or {})
            for chunk, meta in zip(chunks, metadata or [{}]*len(chunks))
        ]
        self.vector_store = FAISS.from_documents(
            docs, 
            self.embedding_manager.model
        )
        return self
    
    def retrieve(self, query: str, k: int = 7) -> List[Document]:
        if not self.vector_store:
            raise ValueError("Vector store not initialized")
        
        return self.vector_store.max_marginal_relevance_search(
            query, 
            k=k, 
            lambda_mult=Config.MMR_LAMBDA
        )