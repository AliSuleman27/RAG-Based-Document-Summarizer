

# Create directory structure
mkdir -p document-summarization/{src,static/{css,js},templates,data/{raw,processed},tests}

# Create empty files
touch document-summarization/src/{__init__.py,config.py,embeddings.py,retriever.py,summarizer.py,app.py}
touch document-summarization/static/css/styles.css
touch document-summarization/static/js/app.js
touch document-summarization/templates/{index.html,results.html}
touch document-summarization/requirements.txt
touch document-summarization/README.md

echo "Directory structure created successfully!"