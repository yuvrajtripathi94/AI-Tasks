# Day 31: How Production AI Systems Handle Scale
# Add Caching + Async Processing using FastAPI & Redis

# Install required libraries
# pip install fastapi uvicorn redis openai

from fastapi import FastAPI
from pydantic import BaseModel
from openai import OpenAI
import redis
import json

# -----------------------------------
# Step 1: Initialize FastAPI
# -----------------------------------

app = FastAPI(
    title="Scalable AI Assistant"
)

# -----------------------------------
# Step 2: OpenAI Client
# -----------------------------------

client = OpenAI(
    api_key="YOUR_API_KEY"
)

# -----------------------------------
# Step 3: Redis Cache
# -----------------------------------

redis_client = redis.Redis(
    host="localhost",
    port=6379,
    decode_responses=True
)

# -----------------------------------
# Step 4: Request Schema
# -----------------------------------

class QueryRequest(BaseModel):
    question: str

# -----------------------------------
# Step 5: Async AI Processing
# -----------------------------------

async def generate_answer(question):

    response = client.chat.completions.create(
        model="gpt-4o-mini",

        messages=[
            {
                "role": "user",
                "content": question
            }
        ]
    )

    return response.choices[0].message.content

# -----------------------------------
# Step 6: Cached Endpoint
# -----------------------------------

@app.post("/ask")

async def ask_ai(request: QueryRequest):

    question = request.question

    # Check Cache First
    cached_answer = redis_client.get(
        question
    )

    if cached_answer:

        return {
            "source": "cache",
            "answer": cached_answer
        }

    # Generate New Response
    answer = await generate_answer(
        question
    )

    # Store in Redis Cache
    redis_client.setex(
        question,
        3600,
        answer
    )

    return {
        "source": "openai",
        "answer": answer
    }

# -----------------------------------
# Step 7: Health Check
# -----------------------------------

@app.get("/health")

def health():

    return {
        "status": "healthy"
    }

# -----------------------------------
# Step 8: Run Server
# -----------------------------------

# uvicorn main:app --reload

# -----------------------------------
# Step 9: Benefits
# -----------------------------------

benefits = [

    "Reduced OpenAI API calls",

    "Lower inference cost",

    "Faster response times",

    "Improved scalability",

    "Handles concurrent users",

    "Reduced latency"
]

print("\n🚀 Production Scaling Benefits:\n")

for item in benefits:

    print(f"✔ {item}")

# -----------------------------------
# Step 10: Key Learning
# -----------------------------------

print(
    "\n💡 Production AI systems use caching and asynchronous processing to serve more users without increasing costs linearly."
)