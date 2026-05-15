# Day 14: Build a Semantic Search Engine

# Install required libraries
# pip install sentence-transformers scikit-learn

from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np

# Sample dataset
documents = [
    "Artificial Intelligence is transforming industries.",
    "Machine learning helps systems learn from data.",
    "Python is widely used in AI development.",
    "Semantic search understands meaning, not just keywords.",
    "Embeddings convert text into numerical vectors.",
    "Retrieval systems help find relevant information quickly.",
    "Natural Language Processing works with text data.",
    "Chatbots use AI to communicate with users."
]

# Load embedding model
model = SentenceTransformer('all-MiniLM-L6-v2')

# Generate document embeddings
doc_embeddings = model.encode(documents)

# User query
query = "How do AI systems understand meaning in text?"

# Generate query embedding
query_embedding = model.encode([query])

# Calculate similarity scores
similarities = cosine_similarity(
    query_embedding,
    doc_embeddings
)[0]

# Get top 3 most similar documents
top_indices = np.argsort(similarities)[::-1][:3]

# Print results
print("🔹 Query:\n")
print(query)

print("\n🔹 Top 3 Semantic Search Results:\n")

for index in top_indices:
    print(f"Document: {documents[index]}")
    print(f"Similarity Score: {similarities[index]:.4f}")
    print("-" * 50)