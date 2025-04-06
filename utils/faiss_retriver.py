import numpy as np

# Example chunk embeddings (4 chunks, 3D vectors)
doc_vectors = np.array([
    [0.2, -0.5, 0.7],
    [0.1, 0.4, 0.3],
    [0.6, -0.1, 0.2],
    [0.0, 0.0, 1.0],
])

# New query (question) vector
query_vector = np.array([0.3, -0.4, 0.6])

# Cosine similarity function
def cosine_sim(a, b):
    return np.dot(a, b) / (np.linalg.norm(a) * np.linalg.norm(b))

similarities = [cosine_sim(query_vector, doc) for doc in doc_vectors]

top_k = np.argsort(similarities)[-2:][::-1]

print("Most similar chunks:", top_k)