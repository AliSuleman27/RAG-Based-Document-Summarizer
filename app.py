from flask import Flask, request, render_template, jsonify
from retriever import Retriever
from summarizer import Summarizer
from langchain.text_splitter import RecursiveCharacterTextSplitter
import os
from config import Config
from document_parser import DocumentParser

app = Flask(__name__)
retriever = Retriever()
summarizer = Summarizer()

@app.route("/", methods=["GET"])
def home():
    return render_template("index.html")

@app.route("/summarize", methods=["POST"])
def summarize():
    # 1. Process uploaded file
    file = request.files["document"]
    text = extract_text(file)
    
    # 2. Chunk document
    splitter = RecursiveCharacterTextSplitter(
        chunk_size=Config.CHUNK_SIZE,
        chunk_overlap=Config.CHUNK_OVERLAP
    )
    chunks = splitter.split_text(text)
    
    # 3. Create vector index
    retriever.create_index(chunks)
    
    # 4. Retrieve relevant chunks
    query = "Provide a comprehensive summary of this document"
    docs = retriever.retrieve(query, k=5)
    context = "\n\n".join([doc.page_content for doc in docs])
    
    # 5. Generate summary
    summary = summarizer.summarize(context)
    
    return jsonify({
        "summary": summary,
        "context_chunks": [doc.page_content for doc in docs]
    })

def extract_text(file):
    """Extract text from uploaded file using appropriate parser"""
    try:
        parser = DocumentParser.get_parser(file)
        return parser.extract_text(file)
    except Exception as e:
        raise ValueError(f"Error processing document: {str(e)}")

if __name__ == "__main__":
    app.run(debug=True)