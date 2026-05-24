# Day 23: Connect a Frontend to Your AI Backend
# Full-Stack AI Integration using Next.js + React + FastAPI

# =============================
# BACKEND (FastAPI)
# =============================

# Install:
# pip install fastapi uvicorn openai

from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware
from openai import OpenAI

app = FastAPI()

# Enable CORS for frontend access
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

client = OpenAI(
    api_key="YOUR_API_KEY"
)

# -----------------------------
# Request Schema
# -----------------------------

class ChatRequest(BaseModel):
    question: str

# -----------------------------
# AI Endpoint
# -----------------------------

@app.post("/chat")

def chat(request: ChatRequest):

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

    # Example source citations
    sources = [
        "Document 1",
        "Knowledge Base"
    ]

    return {
        "answer": answer,
        "sources": sources
    }

# Run Backend:
# uvicorn main:app --reload


# =============================
# FRONTEND (Next.js + React)
# =============================

# Install:
# npm install

# File:
# app/page.js

"""
'use client'

import { useState } from 'react'

export default function Home() {

  const [question, setQuestion] = useState('')
  const [answer, setAnswer] = useState('')
  const [sources, setSources] = useState([])
  const [loading, setLoading] = useState(false)
  const [error, setError] = useState('')

  async function askAI() {

    setLoading(true)
    setError('')
    setAnswer('')

    try {

      const response = await fetch(
        'http://127.0.0.1:8000/chat',
        {
          method: 'POST',

          headers: {
            'Content-Type': 'application/json'
          },

          body: JSON.stringify({
            question
          })
        }
      )

      if (!response.ok) {
        throw new Error('API Error')
      }

      const data = await response.json()

      setAnswer(data.answer)
      setSources(data.sources)

    } catch (err) {

      setError('Something went wrong.')

    } finally {

      setLoading(false)
    }
  }

  return (

    <main style={{ padding: '40px' }}>

      <h1>AI Knowledge Assistant</h1>

      <textarea
        rows={5}
        cols={60}
        placeholder="Ask your question..."
        value={question}
        onChange={(e) =>
          setQuestion(e.target.value)
        }
      />

      <br /><br />

      <button onClick={askAI}>
        Ask AI
      </button>

      <br /><br />

      {loading && <p>Loading response...</p>}

      {error && (
        <p style={{ color: 'red' }}>
          {error}
        </p>
      )}

      {answer && (
        <div>

          <h3>Answer:</h3>

          <p>{answer}</p>

          <h4>Sources:</h4>

          <ul>
            {sources.map((src, index) => (
              <li key={index}>{src}</li>
            ))}
          </ul>

        </div>
      )}

    </main>
  )
}
"""

# =============================
# Step 3: Key Learning
# =============================

print("✅ Full-Stack AI Application Ready")
print("Frontend connected successfully with FastAPI AI backend.")