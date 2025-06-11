import pandas as pd
from pipeline import SummarizationPipeline
from rouge_score import rouge_scorer
import json
from sklearn.metrics.pairwise import cosine_similarity
from embeddings import EmbeddingManager
import traceback
from config import Config


# Initialize components
pipeline = SummarizationPipeline()
embedder = EmbeddingManager()
scorer = rouge_scorer.RougeScorer(['rouge1', 'rouge2', 'rougeL'], use_stemmer=True)
dataset = pd.read_csv('data/validation.csv').head(5)


def cosine_sim(text_a: str, text_b: str) -> float:
    """Compute cosine similarity between two texts using the embedding model."""
    emb_a = embedder.embed_query(text_a)
    emb_b = embedder.embed_query(text_b)

    return float(cosine_similarity([emb_a], [emb_b])[0][0])


results = []
evals = []
mmr_lambda = [0.5]
llm_models = ["llama3-70b-8192"]

for mmr in mmr_lambda:
    Config.MMR_LAMBDA = mmr
    for llm in llm_models:
        Config.GROQ_MODEL = llm
        for i, row in dataset.iterrows():
            article = row["article"]
            reference = row["highlights"]

            try:
                output = pipeline.run("",article)
                generated = output["summary"]
                scores = scorer.score(reference, generated)
                sem_sim = cosine_sim(reference,generated)

                results.append({
                    "id": i,
                    "rouge1": scores["rouge1"].fmeasure,
                    "rouge2": scores["rouge2"].fmeasure,
                    "rougeL": scores["rougeL"].fmeasure,
                    "semantic_similarity": sem_sim,
                })

                # Progress log
                print(
                    f"[{i}] R1: {scores['rouge1'].fmeasure:.4f} | "
                    f"R2: {scores['rouge2'].fmeasure:.4f} | "
                    f"RL: {scores['rougeL'].fmeasure:.4f} | "
                    f"SemSim: {sem_sim:.4f}"
                )

            except Exception as e:
                print(f"[{i}] Error: {e}")
                traceback.print_exc()

        avg_metrics = {
            'mmr_lambda':mmr,
            'llm' : llm,
            "rouge1_avg": sum(r["rouge1"] for r in results) / len(results),
            "rouge2_avg": sum(r["rouge2"] for r in results) / len(results),
            "rougeL_avg": sum(r["rougeL"] for r in results) / len(results),
            "semantic_similarity_avg": sum(r["semantic_similarity"] for r in results) / len(results),
        }
        evals.append(avg_metrics)

df = pd.DataFrame(evals)
df.to_csv('results.csv')


