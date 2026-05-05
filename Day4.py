# Day 4: Vectors — Sentence Embeddings & Similarity

# Install (run once in Colab)
# !pip install sentence-transformers

from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity

# Load pre-trained embedding model
model = SentenceTransformer('all-MiniLM-L6-v2')

# Sample sentences
sentences = [
    "I love machine learning",
    "I enjoy studying AI and ML",
    "The weather is very hot today",
    "Deep learning models are powerful",
    "It is raining outside"
]

# Step 1: Generate embeddings
embeddings = model.encode(sentences)

print("Embeddings shape:", embeddings.shape)

# Step 2: Cosine similarity between all sentences
similarity_matrix = cosine_similarity(embeddings)

print("\nSimilarity Matrix:\n")
print(similarity_matrix)

# Step 3: Compare specific pairs
pairs = [
    (0, 1),  # similar meaning
    (0, 2),  # different meaning
    (2, 4)   # weather-related similarity
]

print("\nPairwise Similarity Scores:\n")
for i, j in pairs:
    print(f"Sentence 1: {sentences[i]}")
    print(f"Sentence 2: {sentences[j]}")
    print("Similarity Score:", similarity_matrix[i][j])
    print("-" * 50)