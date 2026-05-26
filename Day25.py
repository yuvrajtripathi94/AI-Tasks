# Day 25: AI System Architecture Review and Refactoring
# Focus: Code Cleanup, Modularity, Testing, Maintainability

# Install required libraries
# pip install fastapi uvicorn pytest

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import Dict

# -----------------------------
# Step 1: Configuration
# -----------------------------

class Settings:

    APP_NAME = "Refactored AI API"
    VERSION = "1.0"
    MAX_INPUT_LENGTH = 200

settings = Settings()

# -----------------------------
# Step 2: Initialize FastAPI
# -----------------------------

app = FastAPI(
    title=settings.APP_NAME,
    version=settings.VERSION
)

# -----------------------------
# Step 3: Request Schema
# -----------------------------

class ChatRequest(BaseModel):
    message: str

# -----------------------------
# Step 4: Utility Functions
# -----------------------------

def validate_input(text: str):

    if not text.strip():

        raise HTTPException(
            status_code=400,
            detail="Input cannot be empty"
        )

    if len(text) > settings.MAX_INPUT_LENGTH:

        raise HTTPException(
            status_code=400,
            detail="Input exceeds limit"
        )

def generate_response(text: str) -> Dict:

    # Simulated AI response
    return {
        "response": f"AI says: {text}"
    }

# -----------------------------
# Step 5: API Endpoint
# -----------------------------

@app.post("/chat")

def chat(request: ChatRequest):

    validate_input(request.message)

    result = generate_response(
        request.message
    )

    return result

# -----------------------------
# Step 6: Health Endpoint
# -----------------------------

@app.get("/health")

def health():

    return {
        "status": "healthy"
    }

# -----------------------------
# Step 7: Pytest Unit Tests
# -----------------------------

"""
# test_app.py

from app import validate_input

def test_empty_input():

    try:
        validate_input("")
        assert False

    except:
        assert True

def test_valid_input():

    try:
        validate_input("Hello AI")
        assert True

    except:
        assert False
"""

# -----------------------------
# Step 8: Run Server
# -----------------------------

# Run API:
# uvicorn app:app --reload

# Run Tests:
# pytest

# -----------------------------
# Step 9: Key Refactoring Goals
# -----------------------------

print("\n🚀 Refactoring Improvements:\n")

improvements = [
    "Separated configuration logic",
    "Removed duplicated validation",
    "Created reusable utility functions",
    "Added unit tests",
    "Improved maintainability",
    "Prepared codebase for scaling"
]

for item in improvements:
    print(f"- {item}")

# -----------------------------
# Step 10: Key Learning
# -----------------------------

print("\n💡 Key Learning:")
print("Clean architecture and testing are essential for scaling AI systems beyond prototypes.")