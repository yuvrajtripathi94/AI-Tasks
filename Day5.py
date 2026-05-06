# Day 5: Mini Semantic Search Engine

# Install (run once in Colab)
# !pip install sentence-transformers

from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.feature_extraction.text import CountVectorizer
import numpy as np

# Load model
model = SentenceTransformer('all-MiniLM-L6-v2')

# Step 1: Create dataset (20 sentences)
documents = [
    "Machine learning is a subset of artificial intelligence",
    "Deep learning uses neural networks",
    "Natural language processing deals with text data",
    "AI is transforming industries",
    "Python is widely used in data science",
    "Cricket is a popular sport in India",
    "Football is played worldwide",
    "The weather is very hot today",
    "It is raining heavily outside",
    "Data science involves statistics and programming",
    "Neural networks are inspired by the human brain",
    "AI models require large datasets",
    "Books are a great source of knowledge",
    "Reading improves vocabulary",
    "Music helps in relaxation",
    "Traveling opens new experiences",
    "Healthy food improves lifestyle",
    "Exercise keeps the body fit",
    "Technology is evolving rapidly",
    "Smartphones are used daily"
]

# Step 2: Generate embeddings
doc_embeddings = model.encode(documents)

# Step 3: Semantic Search Function
def semantic_search(query, top_k=3):
    query_embedding = model.encode([query])
    similarities = cosine_similarity(query_embedding, doc_embeddings)[0]
    
    top_indices = np.argsort(similarities)[::-1][:top_k]
    
    results = [(documents[i], similarities[i]) for i in top_indices]
    return results

# Step 4: Keyword Search (baseline)
def keyword_search(query, top_k=3):
    vectorizer = CountVectorizer()
    X = vectorizer.fit_transform(documents + [query])
    
    doc_vectors = X[:-1]
    query_vector = X[-1]
    
    similarities = cosine_similarity(query_vector, doc_vectors)[0]
    top_indices = np.argsort(similarities)[::-1][:top_k]
    
    results = [(documents[i], similarities[i]) for i in top_indices]
    return results

# Step 5: Test query
query = "AI and machine learning"

print("🔍 Query:", query)

print("\n🚀 Semantic Search Results:")
for doc, score in semantic_search(query):
    print(f"{doc}  (score: {score:.4f})")

print("\n🔑 Keyword Search Results:")
for doc, score in keyword_search(query):
    print(f"{doc}  (score: {score:.4f})")