# Day 15: Build Your First RAG Pipeline

# Install required libraries
# pip install langchain langchain-openai faiss-cpu sentence-transformers openai

from langchain_openai import OpenAIEmbeddings, ChatOpenAI
from langchain.text_splitter import CharacterTextSplitter
from langchain.vectorstores import FAISS
from langchain.chains import RetrievalQA
from langchain.docstore.document import Document

# -----------------------------
# Step 1: Sample Documents
# -----------------------------

documents = [
    Document(page_content="Artificial Intelligence enables machines to simulate human intelligence."),
    
    Document(page_content="Machine learning is a subset of AI that learns patterns from data."),
    
    Document(page_content="Retrieval-Augmented Generation combines retrieval systems with LLMs."),
    
    Document(page_content="FAISS is used for efficient similarity search in vector databases."),
    
    Document(page_content="Embeddings convert text into numerical vector representations.")
]

# -----------------------------
# Step 2: Split Documents
# -----------------------------

splitter = CharacterTextSplitter(
    chunk_size=100,
    chunk_overlap=20
)

docs = splitter.split_documents(documents)

# -----------------------------
# Step 3: Create Embeddings
# -----------------------------

embeddings = OpenAIEmbeddings(
    api_key="YOUR_API_KEY"
)

# -----------------------------
# Step 4: Store in FAISS
# -----------------------------

vectorstore = FAISS.from_documents(
    docs,
    embeddings
)

# -----------------------------
# Step 5: Create Retriever
# -----------------------------

retriever = vectorstore.as_retriever()

# -----------------------------
# Step 6: Initialize LLM
# -----------------------------

llm = ChatOpenAI(
    api_key="YOUR_API_KEY",
    model="gpt-3.5-turbo"
)

# -----------------------------
# Step 7: Build RAG Chain
# -----------------------------

qa_chain = RetrievalQA.from_chain_type(
    llm=llm,
    retriever=retriever
)

# -----------------------------
# Step 8: Ask Question
# -----------------------------

query = "What is Retrieval-Augmented Generation?"

response = qa_chain.invoke(query)

# -----------------------------
# Step 9: Output
# -----------------------------

print("🔹 Question:\n")
print(query)

print("\n🔹 RAG Response:\n")
print(response["result"])