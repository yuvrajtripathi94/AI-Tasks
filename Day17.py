import numpy as np
import faiss
from sentence_transformers import SentenceTransformer

# =========================
# 📦 1. Load Model
# =========================
model = SentenceTransformer("all-MiniLM-L6-v2")

# =========================
# 📄 2. Documents + Metadata
# =========================
documents = [
    {
        "text": "FAISS is a vector search library used for similarity search",
        "year": 2024,
        "type": "tech"
    },
    {
        "text": "Old blog explains basic FAISS concepts",
        "year": 2020,
        "type": "blog"
    },
    {
        "text": "Cyber security involves malware and trojans",
        "year": 2023,
        "type": "security"
    },
    {
        "text": "Latest AI models improve retrieval augmented generation systems",
        "year": 2025,
        "type": "ai"
    },
    {
        "text": "Marketing guide for AI tools and business growth",
        "year": 2022,
        "type": "marketing"
    }
]

# =========================
# 🔢 3. Create Embeddings
# =========================
texts = [doc["text"] for doc in documents]
embeddings = model.encode(texts).astype("float32")

# =========================
# 🏗️ 4. Build FAISS Index
# =========================
dim = embeddings.shape[1]
index = faiss.IndexFlatL2(dim)
index.add(embeddings)

print("✅ FAISS index created with metadata support")

# =========================
# 🔍 5. Metadata Filter Search
# =========================
def search(query, year_filter=None, doc_type=None, top_k=3):
    query_vec = model.encode([query]).astype("float32")

    # Step 1: Retrieve more candidates
    distances, indices = index.search(query_vec, 10)

    results = []

    for i, idx in enumerate(indices[0]):
        doc = documents[idx]

        # Step 2: Apply metadata filtering
        if year_filter and doc["year"] < year_filter:
            continue
        if doc_type and doc["type"] != doc_type:
            continue

        results.append((doc, distances[0][i]))

        if len(results) == top_k:
            break

    # Step 3: Print results
    print("\n🔎 Query:", query)
    print("🎯 Filter:", {"year": year_filter, "type": doc_type})
    print("\n📌 Results:\n")

    for i, (doc, dist) in enumerate(results):
        print(f"{i+1}. {doc['text']}")
        print(f"   📅 Year: {doc['year']} | 🏷️ Type: {doc['type']} | Distance: {dist:.4f}\n")

# =========================
# 🚀 6. Test Cases
# =========================

# Without filter (baseline behavior)
search("FAISS similarity search")

# With metadata filtering
search("FAISS similarity search", year_filter=2023)

search("AI systems", doc_type="ai")

search("security malware", doc_type="security")