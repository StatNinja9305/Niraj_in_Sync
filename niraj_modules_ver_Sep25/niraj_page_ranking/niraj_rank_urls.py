
import json
import numpy as np
from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity


def rank_niraj_pages_by_score(
        url_file_path = '../Data/urls.json', 
        # Assume each URL entry has "text" attribute.
        corpus_file_path = '../Data/corpus.txt', 
        temp_file_path = '../Data/urls_scored.json', 
        out_file_path = "../Data/score_URLs.json", 
        ):

    # Load the data and pre-trained Sentence-BERT model
    with open(url_file_path, 'r', encoding='utf-8') as file:
        data = json.load(file)
    with open(corpus_file_path, 'r', encoding='utf-8') as file:
        corpus = file.readlines()
    model = SentenceTransformer('sentence-transformers/LaBSE')  # Load Sentence-BERT model

    scores = []
    chunk_size = 4000

    # Tokenize the corpus
    corpus_embeddings = model.encode(corpus, convert_to_tensor=True)
    for entry in data:
        try:
            text = entry['text']
            print(entry['url'])
            tokenized_chunks = []
            chunk_embeddings = model.encode([text], convert_to_tensor=True)

            # Split the chunk_embeddings into chunks of size chunk_size
            for i in range(0, len(chunk_embeddings[0]), chunk_size):
                chunk = chunk_embeddings[0][i:i + chunk_size]
                tokenized_chunks.append(chunk)

            if tokenized_chunks:  # Check if tokenized_chunks is not empty
                similarity_scores = cosine_similarity(tokenized_chunks[0].reshape(1, -1), corpus_embeddings)
                similarity_score = similarity_scores.mean()
            else:
                similarity_score = 0.0  # Assign a default similarity score of 0.0
            
            del entry['text'] 
            entry['score'] = float(similarity_score)

            with open(temp_file_path, 'w', encoding='utf-8') as json_file:
                json.dump(data, json_file, ensure_ascii=False, indent=4)
                    
            scores.append([entry['url'], entry['country'],entry['domain'], entry['category'], float(similarity_score)])  # Convert similarity_score to float
        except Exception as e:
            print(f"An error occurred: {e}")

    scores.sort(key=lambda x: x[4], reverse=True)  # Sort scores in descending order based on similarity scores

    with open(out_file_path, "w", encoding='utf-8') as file:
        json.dump(scores, file, ensure_ascii=False, indent=4)
    return scores

