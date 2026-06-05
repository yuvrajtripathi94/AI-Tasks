# Day 35: Production Hardening and Reliability Engineering

# Install Required Libraries
# pip install fastapi uvicorn pytest httpx

from fastapi import FastAPI
from pydantic import BaseModel
import time
import random

# -----------------------------------
# Step 1: FastAPI Application
# -----------------------------------

app = FastAPI(
    title="Production Ready AI Assistant"
)

# -----------------------------------
# Step 2: Request Schema
# -----------------------------------

class QueryRequest(BaseModel):
    question: str

# -----------------------------------
# Step 3: Circuit Breaker
# -----------------------------------

failure_count = 0
failure_threshold = 3
circuit_open = False

def call_llm(question):

    global failure_count
    global circuit_open

    if circuit_open:

        return {
            "status": "fallback",
            "message":
            "Service temporarily unavailable."
        }

    try:

        # Simulate API failure
        if random.random() < 0.3:
            raise Exception("LLM Timeout")

        failure_count = 0

        return {
            "status": "success",
            "answer":
            f"Response for: {question}"
        }

    except Exception:

        failure_count += 1

        if failure_count >= failure_threshold:
            circuit_open = True

        return {
            "status": "error",
            "message":
            "Model service unavailable."
        }

# -----------------------------------
# Step 4: Graceful Degradation
# -----------------------------------

def fallback_response(question):

    return {
        "status": "fallback",
        "answer":
        "AI service is busy. Please try again later."
    }

# -----------------------------------
# Step 5: Main Endpoint
# -----------------------------------

@app.post("/ask")

def ask(request: QueryRequest):

    result = call_llm(
        request.question
    )

    if result["status"] in [
        "error",
        "fallback"
    ]:

        return fallback_response(
            request.question
        )

    return result

# -----------------------------------
# Step 6: Health Check Endpoint
# -----------------------------------

@app.get("/health")

def health():

    return {

        "status":
        "healthy",

        "circuit_open":
        circuit_open,

        "failures":
        failure_count
    }

# -----------------------------------
# Step 7: Readiness Check
# -----------------------------------

@app.get("/ready")

def ready():

    return {
        "ready": True
    }

# -----------------------------------
# Step 8: Liveness Check
# -----------------------------------

@app.get("/live")

def live():

    return {
        "alive": True
    }

# -----------------------------------
# Step 9: Run Application
# -----------------------------------

# uvicorn main:app --reload

# -----------------------------------
# Step 10: Integration Tests
# File: test_app.py
# -----------------------------------

"""
from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_health():

    response = client.get('/health')

    assert response.status_code == 200

def test_ready():

    response = client.get('/ready')

    assert response.status_code == 200

def test_live():

    response = client.get('/live')

    assert response.status_code == 200

def test_ask():

    response = client.post(
        '/ask',
        json={
            'question':
            'What is AI?'
        }
    )

    assert response.status_code == 200
"""

# Run Tests:
# pytest test_app.py

# -----------------------------------
# Step 11: Reliability Features
# -----------------------------------

features = [

    "Circuit Breaker",

    "Health Checks",

    "Readiness Checks",

    "Liveness Checks",

    "Graceful Degradation",

    "Integration Testing"
]

print(
    "\n🛡 Reliability Features:\n"
)

for item in features:

    print(f"✔ {item}")

# -----------------------------------
# Step 12: Key Learning
# -----------------------------------

print(
    "\n💡 Production AI systems must remain reliable even when dependencies fail. Reliability engineering is as important as model quality."
)