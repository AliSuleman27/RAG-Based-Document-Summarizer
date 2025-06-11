# summarizer.py
from langchain.chains import LLMChain
from langchain.prompts import ChatPromptTemplate
from langchain_groq import ChatGroq
from langchain.callbacks import get_openai_callback
from config import Config
from typing import Dict, Any

class Summarizer:
    def __init__(self):
        self.llm = ChatGroq(
            temperature=0.3,
            model_name=Config.GROQ_MODEL,
            api_key=Config.GROQ_API_KEY
        )
        self.prompt = ChatPromptTemplate.from_messages([
            ("system", """You are an expert document summarizer. Create a concise, coherent summary that captures the key points from the following context. Follow these rules:
            1. Omit technical details unless crucial
            2. Maintain original meaning
            3. Use clear, professional language"""),
            ("human", "Context:\n{context}\n\nSummary:")
        ])
    
    def summarize(self, context: str) -> Dict[str, Any]:
        """Summarize context using LangChain callback to capture token usage."""
        with get_openai_callback() as cb:
            chain = LLMChain(llm=self.llm, prompt=self.prompt)
            result = chain.run(context=context)
            
            return {
                "summary": result,
                "token_usage": {
                    "prompt_tokens": cb.prompt_tokens,
                    "completion_tokens": cb.completion_tokens,
                    "total_tokens": cb.total_tokens
                }
            }