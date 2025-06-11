### app.py
- contains the code for the api-end points.

### config.py
- contains all the editable configurations such as chunk-size, chunk-overlap, mrr lambda, llm model, embedding models

### document_pareser.py
- it accepts the documents and define three different parsing options, analyze the extension of the file, parse it and return the string text which is use for chunking.

### embeddings.py
- It uses the mentioned embedding in the config.py from hugging face, contains two functions, one to encode the query and one to encode the chunks as array. the size of embedding currently uses is 768

### retreiver.py
- It uses the MMR startgy which intiviely penalizes the chunks similarity score, if similar chunk has already been selected, which ensures we select the diverse chunks from documents. lambda control the measure of dissimilarity between the chunks.

### summarizer.py
- It uses the LLM-chain with a custom prompt template with a system message, context retrieved chunk and user prompt for the model and return the structured summary.

### pipeline.py
- It combines the components in multiple file to perform end-end summarization process.
- doc parsing --> chunking ---> MRR Chunk Retrieval with query similarity and diversity ---> getting chunks text corresponding to emebddings index ---> storing the retrieved chunks ---> passing to summarizer ---> returning the summary in json, also returns the token usage summary.

### test.py
- runs the grid search for testing the performance given multiple tunable parameters from Config file.
