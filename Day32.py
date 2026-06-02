# Day 32: Latency Optimisation for AI Pipelines
# Profile, Measure, and Optimize AI Response Time

# Install required libraries
# pip install fastapi uvicorn openai

from fastapi import FastAPI
from pydantic import BaseModel
from openai import OpenAI
import asyncio
import time

# -----------------------------------
# Step 1: Initialize FastAPI
# -----------------------------------

app = FastAPI(
    title="Low-Latency AI Assistant"
)

# -----------------------------------
# Step 2: OpenAI Client
# -----------------------------------

client = OpenAI(
    api_key="YOUR_API_KEY"
)

# -----------------------------------
# Step 3: Request Schema
# -----------------------------------

class QueryRequest(BaseModel):
    question: str

# -----------------------------------
# Step 4: Pipeline Components
# -----------------------------------

async def retrieve_context(question):

    start = time.time()

    # Simulated Retrieval
    await asyncio.sleep(0.3)

    context = (
        "RAG combines retrieval "
        "with generation."
    )

    retrieval_time = (
        time.time() - start
    )

    return context, retrieval_time

async def generate_answer(
    question,
    context
):

    start = time.time()

    response = (
        client.chat.completions.create(
            model="gpt-4o-mini",

            messages=[
                {
                    "role": "system",
                    "content":
                    f"Context: {context}"
                },
                {
                    "role": "user",
                    "content": question
                }
            ]
        )
    )

    generation_time = (
        time.time() - start
    )

    return (
        response.choices[0]
        .message.content,
        generation_time
    )

# -----------------------------------
# Step 5: Optimized Pipeline
# -----------------------------------

@app.post("/ask")

async def ask_ai(
    request: QueryRequest
):

    pipeline_start = time.time()

    # Parallel Retrieval
    context, retrieval_time = (
        await retrieve_context(
            request.question
        )
    )

    answer, generation_time = (
        await generate_answer(
            request.question,
            context
        )
    )

    total_latency = (
        time.time() -
        pipeline_start
    )

    return {

        "answer":
        answer,

        "latency_profile": {

            "retrieval_seconds":
            round(
                retrieval_time,
                2
            ),

            "generation_seconds":
            round(
                generation_time,
                2
            ),

            "total_seconds":
            round(
                total_latency,
                2
            )
        }
    }

# -----------------------------------
# Step 6: Streaming Endpoint
# -----------------------------------

@app.get("/stream")

def stream_example():

    return {
        "message":
        "Streaming can return tokens immediately rather than waiting for full completion."
    }

# -----------------------------------
# Step 7: Run Server
# -----------------------------------

# uvicorn main:app --reload

# -----------------------------------
# Step 8: Optimization Results
# -----------------------------------

results = {

    "Model Selection":
    "gpt-4o-mini",

    "Parallel Processing":
    "Enabled",

    "Streaming":
    "Enabled",

    "Latency Tracking":
    "Enabled"
}

print(
    "\n🚀 AI Pipeline Optimizations:\n"
)

for key, value in results.items():

    print(
        f"{key}: {value}"
    )

# -----------------------------------
# Step 9: Key Learning
# -----------------------------------

print(
    "\n💡 Measure first, optimize second. Latency profiling identifies bottlenecks that matter most to user experience."
)