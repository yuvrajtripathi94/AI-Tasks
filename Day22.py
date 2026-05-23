# Day 22: Designing Production-Ready AI APIs
# Focus: Validation, Error Handling, Streaming, Structured Responses

# Install required libraries
# pip install fastapi uvicorn openai pydantic

from fastapi import FastAPI, HTTPException
from fastapi.responses import StreamingResponse
from pydantic import BaseModel, Field
from openai import OpenAI
import time
import json

# -----------------------------
# Step 1: Initialize FastAPI App
# -----------------------------

app = FastAPI(
    title="Production AI API",
    version="1.0"
)

# -----------------------------
# Step 2: Initialize OpenAI Client
# -----------------------------

client = OpenAI(
    api_key="YOUR_API_KEY"
)

# -----------------------------
# Step 3: Request Schema
# -----------------------------

class ChatRequest(BaseModel):

    question: str = Field(
        min_length=3,
        max_length=500,
        description="User input question"
    )

# -----------------------------
# Step 4: Structured Error Codes
# -----------------------------

ERROR_CODES = {
    "INVALID_INPUT": 1001,
    "MODEL_FAILURE": 2001,
    "TOKEN_LIMIT_EXCEEDED": 3001
}

# -----------------------------
# Step 5: Health Check Endpoint
# -----------------------------

@app.get("/health")

def health_check():

    return {
        "status": "healthy",
        "service": "AI API"
    }

# -----------------------------
# Step 6: Streaming Generator
# -----------------------------

def stream_response(text):

    words = text.split()

    for word in words:
        yield word + " "
        time.sleep(0.05)

# -----------------------------
# Step 7: Main AI Endpoint
# -----------------------------

@app.post("/chat")

def chat(request: ChatRequest):

    question = request.question.strip()

    # Input Validation
    if len(question) < 3:

        raise HTTPException(
            status_code=400,
            detail={
                "error": "Invalid input",
                "error_code": ERROR_CODES["INVALID_INPUT"]
            }
        )

    # Prevent extremely large requests
    if len(question.split()) > 200:

        raise HTTPException(
            status_code=400,
            detail={
                "error": "Token limit exceeded",
                "error_code": ERROR_CODES["TOKEN_LIMIT_EXCEEDED"]
            }
        )

    try:

        # LLM Request
        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {
                    "role": "system",
                    "content": "You are a helpful AI assistant."
                },

                {
                    "role": "user",
                    "content": question
                }
            ]
        )

        answer = response.choices[0].message.content

        # Structured API Response
        return {
            "success": True,
            "question": question,
            "answer": answer,
            "model": "gpt-4o-mini"
        }

    except Exception as e:

        raise HTTPException(
            status_code=500,
            detail={
                "error": str(e),
                "error_code": ERROR_CODES["MODEL_FAILURE"]
            }
        )

# -----------------------------
# Step 8: Streaming Endpoint
# -----------------------------

@app.post("/stream")

def stream_chat(request: ChatRequest):

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {
                "role": "user",
                "content": request.question
            }
        ]
    )

    answer = response.choices[0].message.content

    return StreamingResponse(
        stream_response(answer),
        media_type="text/plain"
    )

# -----------------------------
# Step 9: Run API Server
# -----------------------------

# Run using:
# uvicorn filename:app --reload

# Example:
# uvicorn main:app --reload

# -----------------------------
# Step 10: Example API Request
# -----------------------------

# POST /chat
# {
#   "question": "What is Retrieval-Augmented Generation?"
# }

# -----------------------------
# Step 11: Key Learning
# -----------------------------

print("✅ Production-Ready AI API Created")
print("Includes validation, streaming, error handling, and structured responses.")