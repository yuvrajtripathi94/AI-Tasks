# Day 20: Build a Working AI Knowledge Assistant
# End-to-End RAG Product using FastAPI + FAISS + OpenAI

# Install required libraries
# pip install fastapi uvicorn langchain langchain-openai faiss-cpu openai

from fastapi import FastAPI
from pydantic import BaseModel

from langchain_openai import OpenAIEmbeddings, ChatOpenAI
from langchain.vectorstores import FAISS
from langchain.docstore.document import Document

# -----------------------------
# Step 1: Initialize FastAPI
# -----------------------------

app = FastAPI()

# -----------------------------
# Step 2: Create Knowledge Base
# -----------------------------

documents = [
    Document(
        page_content="FAISS is used for vector similarity search.",
        metadata={"source": "doc_1"}
    ),

    Document(
        page_content="RAG combines retrieval with generation.",
        metadata={"source": "doc_2"}
    ),

    Document(
        page_content="Embeddings convert text into vectors.",
        metadata={"source": "doc_3"}
    ),

    Document(
        page_content="FastAPI helps deploy AI applications as APIs.",
        metadata={"source": "doc_4"}
    )
]

# -----------------------------
# Step 3: Create Embeddings
# -----------------------------

embeddings = OpenAIEmbeddings(
    api_key="YOUR_API_KEY"
)

# Build FAISS vector store
vectorstore = FAISS.from_documents(
    documents,
    embeddings
)

retriever = vectorstore.as_retriever(
    search_kwargs={"k": 2}
)

# -----------------------------
# Step 4: Initialize LLM
# -----------------------------

llm = ChatOpenAI(
    api_key="YOUR_API_KEY",
    model="gpt-3.5-turbo"
)

# -----------------------------
# Step 5: Request Schema
# -----------------------------

class QueryRequest(BaseModel):
    question: str

# -----------------------------
# Step 6: API Endpoint
# -----------------------------

@app.post("/ask")

def ask_question(request: QueryRequest):

    question = request.question

    # Retrieve relevant documents
    retrieved_docs = retriever.invoke(question)

    # Build context
    context = "\n".join(
        [doc.page_content for doc in retrieved_docs]
    )

    # Create source list
    sources = [
        doc.metadata["source"]
        for doc in retrieved_docs
    ]

    # Prompt
    prompt = f"""
Answer the question using ONLY the context below.

Context:
{context}

Question:
{question}

Also mention if the answer is not found in context.
"""

    # Generate response
    response = llm.invoke(prompt)

    # Return API response
    return {
        "question": question,
        "answer": response.content,
        "sources": sources
    }

# -----------------------------
# Step 7: Run Server
# -----------------------------

# Run using:
# uvicorn filename:app --reload

# Example:
# uvicorn main:app --reload

# -----------------------------
# Step 8: Test API
# -----------------------------

# POST Request:
# http://127.0.0.1:8000/ask

# Sample JSON:
# {
#   "question": "What is RAG?"
# }

# -----------------------------
# Step 9: Key Learning
# -----------------------------

print("✅ AI Knowledge Assistant API Ready")
print("This system accepts user questions and returns grounded answers with source citations.")