from fastapi import FastAPI
from pydantic import BaseModel

from rag import get_rag_response
from feedback import save_feedback, get_stats

app = FastAPI(title="AI Portfolio System")

# -----------------------------
# Request Schema
# -----------------------------

class QueryRequest(BaseModel):
    question: str

class FeedbackRequest(BaseModel):
    question: str
    answer: str
    rating: int


# -----------------------------
# AI Endpoint
# -----------------------------

@app.post("/ask")
def ask(req: QueryRequest):

    result = get_rag_response(req.question)

    return {
        "question": req.question,
        "answer": result["answer"],
        "source": result["source"],
        "latency": result["latency"]
    }


# -----------------------------
# Feedback Endpoint
# -----------------------------

@app.post("/feedback")
def feedback(req: FeedbackRequest):

    save_feedback(req.question, req.answer, req.rating)

    return {"message": "Feedback saved successfully"}


# -----------------------------
# Analytics Endpoint
# -----------------------------

@app.get("/analytics")
def analytics():

    return get_stats()


# -----------------------------
# Health Check
# -----------------------------

@app.get("/health")
def health():

    return {"status": "ok"}