# Day 36: Deploy Your AI Backend to the Cloud
# FastAPI + Docker + Railway

# ==========================================
# File: main.py
# ==========================================

from fastapi import FastAPI
from pydantic import BaseModel
import os

app = FastAPI(
    title="Cloud AI Assistant"
)

class Query(BaseModel):
    question: str

@app.get("/")
def home():

    return {
        "message":
        "AI Backend Running on Railway 🚀"
    }

@app.get("/health")
def health():

    return {
        "status": "healthy"
    }

@app.post("/ask")
def ask(query: Query):

    return {

        "question":
        query.question,

        "answer":
        f"Generated response for: {query.question}"
    }

# ==========================================
# File: requirements.txt
# ==========================================

"""
fastapi
uvicorn
pydantic
"""

# ==========================================
# File: Dockerfile
# ==========================================

"""
FROM python:3.11-slim

WORKDIR /app

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 8000

CMD ["uvicorn",
     "main:app",
     "--host",
     "0.0.0.0",
     "--port",
     "8000"]
"""

# ==========================================
# File: railway.json
# ==========================================

"""
{
  "$schema":
  "https://railway.app/railway.schema.json",

  "deploy": {
    "restartPolicyType":
    "ON_FAILURE",

    "restartPolicyMaxRetries":
    10
  }
}
"""

# ==========================================
# Local Run
# ==========================================

"""
uvicorn main:app --reload
"""

# ==========================================
# Docker Commands
# ==========================================

"""
docker build -t ai-backend .

docker run -p 8000:8000 ai-backend
"""

# ==========================================
# Railway Deployment Steps
# ==========================================

deployment_steps = [

    "Push code to GitHub",

    "Create Railway Project",

    "Connect GitHub Repository",

    "Railway detects Dockerfile",

    "Configure Environment Variables",

    "Deploy Application",

    "Receive Public URL",

    "Test API Endpoints"
]

print("\n☁️ Railway Deployment Flow:\n")

for step in deployment_steps:

    print(f"✔ {step}")

# ==========================================
# API Verification
# ==========================================

verification = [

    "GET /",

    "GET /health",

    "POST /ask"
]

print("\n🧪 Deployment Verification:\n")

for item in verification:

    print(f"✔ {item}")

# ==========================================
# Key Learning
# ==========================================

print(
    "\n💡 Cloud deployment transforms a local AI application into a publicly accessible service with automatic restarts and environment isolation."
)