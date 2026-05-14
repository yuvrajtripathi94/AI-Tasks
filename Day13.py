# Day 13: Embedding Deep Dive

# Install required library
# pip install sentence-transformers scikit-learn

from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np

# Load embedding model
model = SentenceTransformer('all-MiniLM-L6-v2')

# Sample sentences
sentences = [
    "Artificial Intelligence is changing the world.",
    "AI is transforming industries globally.",
    "I enjoy playing cricket on weekends.",
    "Machine learning helps computers learn patterns.",
    "Football is one of the most popular sports."
]

# Generate embeddings
embeddings = model.encode(sentences)

# Print embedding dimensions
print("🔹 Embedding Shape:")
print(embeddings.shape)

# Compute similarity matrix
similarity_matrix = cosine_similarity(embeddings)

print("\n🔹 Semantic Similarity Matrix:\n")

for i in range(len(sentences)):
    for j in range(len(sentences)):
        print(f"Sentence {i+1} ↔ Sentence {j+1}")
        print(f"Score: {similarity_matrix[i][j]:.4f}")
        print("-" * 40)

# Query sentence
query = "Technology powered by AI is growing rapidly."

query_embedding = model.encode([query])

# Similarity with dataset
scores = cosine_similarity(query_embedding, embeddings)[0]

# Most similar sentence
best_index = np.argmax(scores)

print("\n🔹 Query:")
print(query)

print("\n🔹 Most Similar Sentence:")
print(sentences[best_index])

print("\n🔹 Similarity Score:")
print(scores[best_index])