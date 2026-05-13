# Day 12: Chunking for AI Systems

# Sample document
text = """
Artificial Intelligence is transforming industries worldwide.
Machine learning helps systems learn from data.
Natural Language Processing enables machines to understand text.
Embeddings help AI systems understand semantic meaning.
Chunking is important for Retrieval-Augmented Generation systems.
Large documents are divided into smaller chunks for efficient retrieval.
"""

# Function for chunking text
def chunk_text(text, chunk_size=80):
    chunks = []
    
    for i in range(0, len(text), chunk_size):
        chunk = text[i:i + chunk_size]
        chunks.append(chunk)
    
    return chunks

# Create chunks
chunks = chunk_text(text)

# Print chunks
print("🔹 Original Text:\n")
print(text)

print("\n🔹 Text Chunks:\n")

for index, chunk in enumerate(chunks, start=1):
    print(f"Chunk {index}:")
    print(chunk)
    print("-" * 50)