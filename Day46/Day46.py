import os
from dotenv import load_dotenv

from langchain_openai import ChatOpenAI
from langchain_openai import OpenAIEmbeddings

from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import FAISS
from langchain.schema import Document

load_dotenv()

llm = ChatOpenAI(
    model="gpt-4o-mini",
    temperature=0
)

embeddings = OpenAIEmbeddings()

# -----------------------------
# Load Documents
# -----------------------------
with open("data/documents.txt", "r", encoding="utf-8") as f:
    text = f.read()

splitter = RecursiveCharacterTextSplitter(
    chunk_size=500,
    chunk_overlap=50
)

chunks = splitter.split_text(text)

docs = [Document(page_content=c) for c in chunks]

vectorstore = FAISS.from_documents(
    docs,
    embeddings
)

# -----------------------------
# Basic Retrieval
# -----------------------------
def basic_retrieval(query):
    return vectorstore.similarity_search(query, k=5)

# -----------------------------
# Technique 1:
# Query Rewriting
# -----------------------------
def query_rewrite(query):

    prompt = f"""
    Rewrite the user query to improve
    semantic search retrieval.

    Query:
    {query}
    """

    rewritten = llm.invoke(prompt)

    return rewritten.content

def rewritten_retrieval(query):

    new_query = query_rewrite(query)

    return vectorstore.similarity_search(
        new_query,
        k=5
    )

# -----------------------------
# Technique 2:
# HyDE Retrieval
# -----------------------------
def hyde_retrieval(query):

    prompt = f"""
    Write a detailed hypothetical answer
    to this question.

    Question:
    {query}
    """

    hypothetical = llm.invoke(prompt)

    return vectorstore.similarity_search(
        hypothetical.content,
        k=5
    )

# -----------------------------
# Technique 3:
# Re-ranking
# -----------------------------
def rerank(query, docs):

    scored = []

    for doc in docs:

        prompt = f"""
        Query:
        {query}

        Document:
        {doc.page_content}

        Give relevance score from 1-10.
        Return only number.
        """

        score = llm.invoke(prompt)

        try:
            val = float(score.content.strip())
        except:
            val = 0

        scored.append((val, doc))

    scored.sort(
        key=lambda x: x[0],
        reverse=True
    )

    return [d for _, d in scored]

def reranked_retrieval(query):

    retrieved = vectorstore.similarity_search(
        query,
        k=10
    )

    return rerank(
        query,
        retrieved
    )[:5]

# -----------------------------
# Generate Answer
# -----------------------------
def answer_query(query, method="basic"):

    if method == "basic":
        docs = basic_retrieval(query)

    elif method == "rewrite":
        docs = rewritten_retrieval(query)

    elif method == "hyde":
        docs = hyde_retrieval(query)

    elif method == "rerank":
        docs = reranked_retrieval(query)

    else:
        raise ValueError("Unknown method")

    context = "\n\n".join(
        [d.page_content for d in docs]
    )

    prompt = f"""
    Use the context below to answer.

    Context:
    {context}

    Question:
    {query}
    """

    answer = llm.invoke(prompt)

    return answer.content

# -----------------------------
# Compare All Methods
# -----------------------------
if __name__ == "__main__":

    query = input("Ask: ")

    methods = [
        "basic",
        "rewrite",
        "hyde",
        "rerank"
    ]

    for m in methods:

        print("\n" + "=" * 50)
        print("METHOD:", m.upper())
        print("=" * 50)

        result = answer_query(
            query,
            method=m
        )

        print(result)