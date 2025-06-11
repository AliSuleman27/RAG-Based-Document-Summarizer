import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    EMBEDDING_MODEL = "all-mpnet-base-v2"
    GROQ_MODEL = "llama3-70b-8192"
    GROQ_API_KEY = os.getenv("GROQ_API_KEY")
    CHUNK_SIZE = 200
    CHUNK_OVERLAP = 50
    MMR_LAMBDA = 0.5  # Diversity vs relevance balance (0-1)