# Day 39: Iterate on Your AI Product Based on Evidence

# Install:
# pip install fastapi openai langchain pandas

from fastapi import FastAPI
from pydantic import BaseModel
import pandas as pd

app = FastAPI(
    title="AI Product Iteration System"
)

# -----------------------------------
# Sample User Feedback Data
# -----------------------------------

feedback_data = [

    {
        "issue":
        "Incorrect retrieval",

        "count": 25
    },

    {
        "issue":
        "Slow response",

        "count": 18
    },

    {
        "issue":
        "Hallucinated answer",

        "count": 12
    },

    {
        "issue":
        "Poor citation quality",

        "count": 8
    }
]

# -----------------------------------
# Analyze Feedback
# -----------------------------------

df = pd.DataFrame(
    feedback_data
)

df = df.sort_values(
    by="count",
    ascending=False
)

print(
    "\nTop User Issues:\n"
)

print(df)

# -----------------------------------
# Improvement Plan
# -----------------------------------

improvements = {

    "Incorrect retrieval":
    "Increase retrieval quality using better chunking and reranking.",

    "Slow response":
    "Add Redis caching and async processing.",

    "Hallucinated answer":
    "Strengthen grounding with stricter prompts.",

    "Poor citation quality":
    "Return source chunks with answers."
}

# -----------------------------------
# API Schema
# -----------------------------------

class Question(
    BaseModel
):

    query: str

# -----------------------------------
# Improved Answer Endpoint
# -----------------------------------

@app.post("/ask")

def ask(
    request: Question
):

    return {

        "question":
        request.query,

        "answer":
        "Improved grounded answer.",

        "citations":
        [
            "Document 1",
            "Document 2"
        ],

        "version":
        "v2.0"
    }

# -----------------------------------
# Metrics Endpoint
# -----------------------------------

@app.get("/metrics")

def metrics():

    return {

        "average_rating":
        4.6,

        "retrieval_accuracy":
        "91%",

        "latency":
        "1.2 sec",

        "product_version":
        "v2.0"
    }

# -----------------------------------
# Key Learning
# -----------------------------------

print(
    "\n💡 Product improvements should be driven by user evidence, not assumptions."
)