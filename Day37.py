// Day 37: Deploy Your AI Frontend
// Full Next.js Frontend for AI Research Assistant

// ============================================
// File Structure
// ============================================

/*
ai-frontend/
│
├── pages/
│   ├── _app.js
│   └── index.js
│
├── styles/
│   └── globals.css
│
├── .env.local
│
├── package.json
│
└── next.config.js
*/

// ============================================
// File: package.json
// ============================================

{
  "name": "ai-research-assistant",
  "version": "1.0.0",

  "scripts": {

    "dev": "next dev",

    "build": "next build",

    "start": "next start"
  },

  "dependencies": {

    "next": "^14.2.0",

    "react": "^18.2.0",

    "react-dom": "^18.2.0"
  }
}

// ============================================
// File: .env.local
// ============================================

NEXT_PUBLIC_API_URL=https://your-railway-app.up.railway.app

// ============================================
// File: pages/_app.js
// ============================================

import "../styles/globals.css";

export default function App({

  Component,

  pageProps

}) {

  return (

    <Component {...pageProps} />

  );
}

// ============================================
// File: pages/index.js
// ============================================

import { useState } from "react";

export default function Home() {

  const [question, setQuestion] =
    useState("");

  const [answer, setAnswer] =
    useState("");

  const [loading, setLoading] =
    useState(false);

  const [error, setError] =
    useState("");

  async function askQuestion() {

    if (!question.trim()) {

      setError(
        "Please enter a question."
      );

      return;
    }

    setLoading(true);

    setError("");

    setAnswer("");

    try {

      const response = await fetch(

        `${process.env.NEXT_PUBLIC_API_URL}/ask`,

        {

          method: "POST",

          headers: {

            "Content-Type":
              "application/json",
          },

          body: JSON.stringify({

            question:
              question,
          }),
        }
      );

      if (!response.ok) {

        throw new Error(
          "Backend error"
        );
      }

      const data =
        await response.json();

      setAnswer(
        data.answer
      );

    } catch (err) {

      setError(

        "Unable to connect to AI backend."

      );

    } finally {

      setLoading(false);
    }
  }

  return (

    <div className="container">

      <h1>
        AI Research Assistant
      </h1>

      <p>
        Ask questions about your
        uploaded documents.
      </p>

      <textarea

        rows="6"

        placeholder="Enter your question..."

        value={question}

        onChange={(e) =>
          setQuestion(
            e.target.value
          )
        }

      />

      <button

        onClick={
          askQuestion
        }

        disabled={
          loading
        }

      >

        {loading
          ? "Thinking..."
          : "Ask AI"}

      </button>

      {error && (

        <div
          className="error"
        >

          {error}

        </div>
      )}

      {answer && (

        <div
          className="answer"
        >

          <h3>
            Answer
          </h3>

          <p>
            {answer}
          </p>

        </div>
      )}

    </div>
  );
}

// ============================================
// File: styles/globals.css
// ============================================

body {

  margin: 0;

  padding: 0;

  font-family:
    Arial, sans-serif;

  background:
    #f5f5f5;
}

.container {

  max-width: 900px;

  margin: 50px auto;

  background: white;

  padding: 30px;

  border-radius: 10px;

  box-shadow:
    0 0 10px
    rgba(
      0,
      0,
      0,
      0.1
    );
}

h1 {

  margin-bottom: 10px;
}

textarea {

  width: 100%;

  padding: 12px;

  margin-top: 10px;

  border: 1px solid #ddd;

  border-radius: 5px;

  resize: vertical;
}

button {

  margin-top: 15px;

  padding:
    12px 20px;

  cursor: pointer;

  border: none;

  background: black;

  color: white;

  border-radius: 5px;
}

button:disabled {

  opacity: 0.6;
}

.answer {

  margin-top: 25px;

  padding: 15px;

  background:
    #f8f8f8;

  border-radius: 5px;
}

.error {

  margin-top: 20px;

  color: red;
}

// ============================================
// FastAPI Backend CORS
// main.py
// ============================================

from fastapi import FastAPI

from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(

    CORSMiddleware,

    allow_origins=[

        "https://your-app.vercel.app"

    ],

    allow_credentials=True,

    allow_methods=["*"],

    allow_headers=["*"]

)

@app.post("/ask")

def ask_ai(data: dict):

    return {

        "answer":

        "This is a sample AI response."

    }

// ============================================
// Deployment Commands
// ============================================

/*

# Run Frontend

npm install

npm run dev


# Build Production

npm run build

npm start


# Deploy to Vercel

npm install -g vercel

vercel


