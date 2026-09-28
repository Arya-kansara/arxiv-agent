import faiss
import numpy as np

def build_faiss_index(embeddings):

    vectors = np.array(embeddings).astype("float32")

    faiss.normalize_L2(vectors)

    dimension = vectors.shape[1]

    index = faiss.IndexFlatIP(dimension)

    index.add(vectors)

    return index