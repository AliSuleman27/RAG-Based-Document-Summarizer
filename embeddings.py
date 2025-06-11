from langchain.embeddings import HuggingFaceEmbeddings
from config import Config

class EmbeddingManager:
    def __init__(self):
        self.model = HuggingFaceEmbeddings(
            model_name=Config.EMBEDDING_MODEL,
            model_kwargs={"device": "cpu"}
        )
    
    def embed_texts(self, texts):
        return self.model.embed_documents(texts)
    
    def embed_query(self, query):
        return self.model.embed_query(query)