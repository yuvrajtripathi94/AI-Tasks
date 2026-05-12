# Day 11: How Retrieval Systems Work

# Install required library
# pip install sentence-transformers scikit-learn

from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np

# Sample knowledge base
documents = [
    "Machine learning helps computers learn from data.",
    "Artificial Intelligence is transforming industries.",
    "Python is widely used for AI development.",
    "Retrieval systems find relevant information quickly.",
    "Embeddings help measure semantic similarity.",
    "Neural networks are inspired by the human brain."
]

# Load embedding model
model = SentenceTransformer('all-MiniLM-L6-v2')

# Convert documents into embeddings
doc_embeddings = model.encode(documents)

# Query
query = "How do AI systems search relevant information?"

# Convert query into embedding
query_embedding = model.encode([query])

# Calculate similarity scores
similarities = cosine_similarity(
    query_embedding,
    doc_embeddings
)[0]

# Get top matching document
top_index = np.argmax(similarities)

# Print results
print("🔹 Query:\n")
print(query)

print("\n🔹 Most Relevant Document:\n")
print(documents[top_index])

print("\n🔹 Similarity Score:")
print(similarities[top_index])

# Show all similarity scores
print("\n🔹 All Similarity Scores:\n")

for doc, score in zip(documents, similarities):
    print(f"{doc} --> {score:.4f}")