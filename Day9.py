# Day 9: Semantic Similarity with Embeddings

# Install required library
# pip install sentence-transformers

from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity

# Load embedding model
model = SentenceTransformer('all-MiniLM-L6-v2')

# Sample sentences
sentences = [
    "Machine learning is transforming technology.",
    "AI is changing the future of technology.",
    "I love playing football.",
    "Natural language processing works with text data.",
    "Soccer is my favorite sport."
]

# Generate embeddings
embeddings = model.encode(sentences)

# Compute similarity matrix
similarity_matrix = cosine_similarity(embeddings)

# Print similarity scores
print("🔹 Semantic Similarity Matrix:\n")

for i in range(len(sentences)):
    for j in range(len(sentences)):
        print(f"Similarity between:\n'{sentences[i]}'\nand\n'{sentences[j]}'")
        print(f"Score: {similarity_matrix[i][j]:.4f}")
        print("-" * 60)

# Manual query test
query = "Artificial Intelligence is improving technology."

query_embedding = model.encode([query])

query_similarity = cosine_similarity(
    query_embedding,
    embeddings
)[0]

# Get most similar sentence
best_match_index = query_similarity.argmax()

print("\n🔹 Query:\n", query)
print("\n🔹 Most Similar Sentence:\n", sentences[best_match_index])
print("Similarity Score:", query_similarity[best_match_index])