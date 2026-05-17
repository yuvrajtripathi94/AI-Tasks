# Day 16: Diagnosing RAG Failure Modes

# Install required libraries
# pip install langchain langchain-openai faiss-cpu openai

from langchain_openai import OpenAIEmbeddings, ChatOpenAI
from langchain.vectorstores import FAISS
from langchain.docstore.document import Document
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np

# -----------------------------
# Step 1: Sample Documents
# -----------------------------

documents = [
    Document(page_content="Machine learning learns patterns from data."),
    
    Document(page_content="FAISS is used for vector similarity search."),
    
    Document(page_content="RAG combines retrieval with generation."),
    
    Document(page_content="Embeddings convert text into vectors.")
]

# -----------------------------
# Step 2: Generate Embeddings
# -----------------------------

embeddings = OpenAIEmbeddings(
    api_key="YOUR_API_KEY"
)

# Create FAISS vector store
vectorstore = FAISS.from_documents(
    documents,
    embeddings
)

# -----------------------------
# Step 3: Test Query
# -----------------------------

query = "How do retrieval systems reduce hallucination?"

# Retrieve relevant docs
retriever = vectorstore.as_retriever(search_kwargs={"k": 2})

retrieved_docs = retriever.invoke(query)

# -----------------------------
# Step 4: Print Retrieved Docs
# -----------------------------

print("🔹 Query:\n")
print(query)

print("\n🔹 Retrieved Documents:\n")

for i, doc in enumerate(retrieved_docs, start=1):
    print(f"Document {i}:")
    print(doc.page_content)
    print("-" * 50)

# -----------------------------
# Step 5: Generate Answer
# -----------------------------

llm = ChatOpenAI(
    api_key="YOUR_API_KEY",
    model="gpt-3.5-turbo"
)

context = "\n".join([doc.page_content for doc in retrieved_docs])

prompt = f"""
Answer the question using ONLY the context below.

Context:
{context}

Question:
{query}
"""

response = llm.invoke(prompt)

# -----------------------------
# Step 6: Output
# -----------------------------

print("\n🔹 AI Response:\n")
print(response.content)

# -----------------------------
# Step 7: Failure Analysis
# -----------------------------

print("\n🔹 Possible RAG Failure Modes:\n")

failure_modes = [
    "Wrong documents retrieved",
    "Insufficient context in chunks",
    "Embedding similarity mismatch",
    "Hallucinated generation by LLM",
    "Small or incomplete knowledge base"
]

for item in failure_modes:
    print(f"- {item}")