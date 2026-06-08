# Day 38: Collecting and Structuring Real User Feedback

# Install Required Libraries
# pip install fastapi uvicorn sqlalchemy

from fastapi import FastAPI
from pydantic import BaseModel
from sqlalchemy import (
    create_engine,
    Column,
    Integer,
    String,
    Float
)
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# ------------------------------------
# FastAPI App
# ------------------------------------

app = FastAPI(
    title="AI Feedback System"
)

# ------------------------------------
# SQLite Database
# ------------------------------------

DATABASE_URL = "sqlite:///feedback.db"

engine = create_engine(
    DATABASE_URL,
    connect_args={
        "check_same_thread": False
    }
)

SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine
)

Base = declarative_base()

# ------------------------------------
# Feedback Table
# ------------------------------------

class Feedback(Base):

    __tablename__ = "feedback"

    id = Column(
        Integer,
        primary_key=True,
        index=True
    )

    question = Column(String)

    answer = Column(String)

    rating = Column(Integer)

    comment = Column(String)

Base.metadata.create_all(
    bind=engine
)

# ------------------------------------
# Request Schema
# ------------------------------------

class FeedbackRequest(
    BaseModel
):

    question: str

    answer: str

    rating: int

    comment: str = ""

# ------------------------------------
# Submit Feedback
# ------------------------------------

@app.post("/feedback")

def submit_feedback(
    data: FeedbackRequest
):

    db = SessionLocal()

    record = Feedback(

        question=data.question,

        answer=data.answer,

        rating=data.rating,

        comment=data.comment
    )

    db.add(record)

    db.commit()

    db.refresh(record)

    db.close()

    return {

        "message":
        "Feedback stored successfully",

        "feedback_id":
        record.id
    }

# ------------------------------------
# Analytics Endpoint
# ------------------------------------

@app.get("/analytics")

def analytics():

    db = SessionLocal()

    feedback_list = db.query(
        Feedback
    ).all()

    total = len(
        feedback_list
    )

    if total == 0:

        return {

            "total_feedback":
            0,

            "average_rating":
            0
        }

    avg_rating = sum(

        item.rating

        for item in feedback_list

    ) / total

    db.close()

    return {

        "total_feedback":
        total,

        "average_rating":
        round(
            avg_rating,
            2
        )
    }

# ------------------------------------
# Recent Feedback
# ------------------------------------

@app.get("/feedbacks")

def get_feedbacks():

    db = SessionLocal()

    records = db.query(
        Feedback
    ).all()

    output = []

    for item in records:

        output.append({

            "id":
            item.id,

            "question":
            item.question,

            "rating":
            item.rating,

            "comment":
            item.comment
        })

    db.close()

    return output

# ------------------------------------
# Health Check
# ------------------------------------

@app.get("/health")

def health():

    return {

        "status":
        "healthy"
    }

# ------------------------------------
# Run Server
# ------------------------------------

# uvicorn main:app --reload

# ------------------------------------
# Example API Calls
# ------------------------------------

"""
POST /feedback

{
  "question":
  "What is RAG?",

  "answer":
  "RAG combines retrieval and generation.",

  "rating": 5,

  "comment":
  "Very helpful answer"
}
"""

"""
GET /analytics

Response:

{
  "total_feedback": 20,
  "average_rating": 4.6
}
"""

# ------------------------------------
# Key Learning
# ------------------------------------

print(
    "User feedback provides insights that automated evaluation cannot capture."
)