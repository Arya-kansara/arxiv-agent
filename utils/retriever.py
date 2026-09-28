import numpy as np
import faiss
from utils.embeddings import model

def retrieve_chunks(question, chunks, index, k=8):

    query_vector = model.encode([question]).astype("float32")
    faiss.normalize_L2(query_vector)

    scores, indices = index.search(query_vector, k)

    results = []

    for i in indices[0]:
        if i == -1:
            continue

        chunk = chunks[i]

        # Remove noisy OCR chunks
        if "<pad>" in chunk or "<EOS>" in chunk:
            continue

        if "American governments" in chunk:
            continue

        if "The Law will never be perfect" in chunk:
            continue

        results.append(chunk)

    return results[:5]