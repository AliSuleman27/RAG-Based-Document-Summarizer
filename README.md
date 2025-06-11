
# RAG-based Document Summarizer

A Retrieval-Augmented Generation (RAG) system for summarizing documents, supporting PDF, TXT, and DOC/DOCX formats. The system extracts key information using semantic search and generates concise summaries with LLMs.

## Features

- Supports multiple document formats (PDF, TXT, DOC/DOCX)
- Chunking with configurable size and overlap
- Semantic retrieval using FAISS vector store
- Summary generation with Groq's Llama3-70b
- Configurable parameters for retrieval and generation
- Flask-based web interface

## Setup

### Prerequisites

- Python 3.8+
- pip
- Groq API key (free tier available)

### Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/AliSuleman27/RAG-Based-Document-Summarizer.git
   cd document-summarizer
   ```

2. Create and activate a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # Linux/Mac
   venv\Scripts\activate    # Windows
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Create a `.env` file and add your Groq API key:
   ```
   GROQ_API_KEY=your_api_key_here
   ```

## Configuration

Modify `config.py` to adjust system parameters:

| Parameter | Description | Default Value |
|-----------|------------|---------------|
| `EMBEDDING_MODEL` | Sentence embedding model | "all-mpnet-base-v2" |
| `GROQ_MODEL` | LLM for summarization | "llama3-70b-8192" |
| `CHUNK_SIZE` | Text chunk size (characters) | 500 |
| `CHUNK_OVERLAP` | Overlap between chunks | 150 |
| `MMR_LAMBDA` | Diversity vs relevance balance (0-1) | 0.5 |

## Architecture

### Components

1. **Document Parser**
   - Factory pattern to handle different file types
   - Supports PDF (PyPDF2), TXT, and DOC/DOCX (python-docx)

2. **Text Processing**
   - Recursive character text splitting
   - Configurable chunk size and overlap

3. **Retrieval System**
   - FAISS vector store for efficient similarity search
   - HuggingFace sentence embeddings
   - Maximal Marginal Relevance (MMR) for balanced retrieval

4. **Summarization**
   - Groq's Llama3-70b model
   - Custom prompt template for consistent summaries
   - Temperature control for deterministic output

5. **Web Interface**
   - Flask-based frontend
   - Simple HTML/JS interface

### Workflow

1. Document upload
2. Text extraction based on file type
3. Chunking with overlap
4. Vector embedding creation
5. Relevant chunk retrieval using MMR
6. LLM-based summarization of retrieved context
7. Summary presentation

## Usage

### Running the Application

Start the Flask development server:
```bash
python app.py
```

Access the web interface at `http://localhost:5000`

### API Endpoints

- `GET /`: Returns the web interface
- `POST /summarize`: Processes document and returns summary

Example API response:
```json
{
  "summary": "The document discusses... [generated summary]",
  "context_chunks": ["...relevant text chunk 1...", "...chunk 2..."]
}
```

## Customization

### Modifying the Summarization Prompt

Edit the prompt template in `summarizer.py`:
```python
self.prompt = ChatPromptTemplate.from_messages([
    ("system", """Your custom instructions here..."""),
    ("human", "Context:\n{context}\n\nSummary:")
])
```

### Adjusting Retrieval Parameters

Modify in `config.py`:
- Increase `CHUNK_SIZE` for longer context windows
- Adjust `MMR_LAMBDA` (higher = more diverse results)
- Change `EMBEDDING_MODEL` for different embedding quality/speed tradeoffs

## Troubleshooting

**Common Issues:**

1. **Document parsing errors**:
   - Ensure files are not password protected
   - Verify file extensions match content

2. **API key issues**:
   - Check `.env` file exists with correct GROQ_API_KEY
   - Verify network connectivity

3. **Memory limitations**:
   - Reduce `CHUNK_SIZE` for large documents
   - Decrease number of retrieved chunks (`k` parameter)

## Performance Considerations

- Larger chunk sizes require more memory
- Smaller overlaps may miss context connections
- Higher MMR lambda values increase diversity but may reduce relevance
- Groq API has rate limits (check your plan)

## Future Enhancements

1. Add support for more document types (PPT, HTML)
2. Implement batch processing for multiple documents
3. Add summary length control
4. Include confidence scoring for retrieved chunks
5. Add user feedback mechanism to improve retrieval
6. Using K-mediod centering approaches for efficient retrieval.
