| Config | Model           | Chunk Size | Overlap | k | ROUGE-1    | ROUGE-2    | ROUGE-L    | Semantic Sim B/W generated and actual | **Average Score** |
| ------ | --------------- | ---------- | ------- | - | ---------- | ---------- | ---------- | ------------ | ----------------- |
| A      | llama3-70b-8192 | 1000       | 200     | 7 | 0.3910     | **0.1423** | **0.2506** | 0.6336       | **0.3544**        |
| B      | llama3-70b-8192 | 500        | 200     | 5 | 0.3911 | 0.1334     | 0.2343     | 0.6638   | **0.3556**        |
| C      | qwen-qwq        | 200        | 50      | 5 | 0.1301     | 0.0400     | 0.0820     | 0.4795       | **0.1829**        |
| D\*    | llama-3.3-70b-versatile | 500       | 150     | 7 | **0.3928**     | 0.1217     | 0.2159     | **0.7887**       | **0.3773**        |

- The results were computed for 50 samples and the averaged.
- The rouge score was much helful here because differnt LLM tend to have different temperature values set and measure of overlap donot capture the semantic similarity between teh samples. Considering the D Config as best with reasonable chunk_size, overlap, diverse k value and high cosine simialrity between generated and actual ones.
