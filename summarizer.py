from langchain.chains import LLMChain
from langchain.prompts import ChatPromptTemplate
from langchain_groq import ChatGroq
from config import Config

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
    
    def summarize(self, context: str) -> str:
        chain = LLMChain(llm=self.llm, prompt=self.prompt)
        return chain.run(context=context)