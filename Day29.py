# Day 29: Building AI Evaluation Systems
# LLM-as-a-Judge Evaluation Framework

# Install required libraries
# pip install openai pandas

from openai import OpenAI
import pandas as pd

# -----------------------------
# Step 1: Initialize OpenAI Client
# -----------------------------

client = OpenAI(
    api_key="YOUR_API_KEY"
)

# -----------------------------
# Step 2: Test Dataset
# -----------------------------

test_cases = [

    {
        "question": "What is RAG?",
        "reference_answer":
        "RAG stands for Retrieval-Augmented Generation."
    },

    {
        "question": "What are embeddings?",
        "reference_answer":
        "Embeddings are numerical vector representations of text."
    },

    {
        "question": "What is FAISS?",
        "reference_answer":
        "FAISS is a vector similarity search library."
    }
]

# -----------------------------
# Step 3: Generate Assistant Answer
# -----------------------------

def generate_answer(question):

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

# -----------------------------
# Step 4: LLM-as-a-Judge
# -----------------------------

def evaluate_answer(
    question,
    reference_answer,
    candidate_answer
):

    evaluation_prompt = f"""
You are an AI evaluator.

Question:
{question}

Reference Answer:
{reference_answer}

Candidate Answer:
{candidate_answer}

Score the answer from 1 to 10 based on:
1. Correctness
2. Relevance
3. Completeness

Return ONLY a number.
"""

    evaluation = client.chat.completions.create(
        model="gpt-4o-mini",

        messages=[
            {
                "role": "user",
                "content": evaluation_prompt
            }
        ]
    )

    return evaluation.choices[0].message.content

# -----------------------------
# Step 5: Run Evaluation
# -----------------------------

results = []

print("\n🔍 Running Evaluation...\n")

for case in test_cases:

    answer = generate_answer(
        case["question"]
    )

    score = evaluate_answer(
        case["question"],
        case["reference_answer"],
        answer
    )

    results.append({
        "Question": case["question"],
        "Score": score
    })

    print("Question:",
          case["question"])

    print("Score:",
          score)

    print("-" * 50)

# -----------------------------
# Step 6: Create Report
# -----------------------------

df = pd.DataFrame(results)

print("\n📊 Evaluation Summary:\n")
print(df)

# -----------------------------
# Step 7: Regression Check
# -----------------------------

average_score = (
    pd.to_numeric(df["Score"])
    .mean()
)

threshold = 7.0

print("\n📈 Average Score:",
      round(average_score, 2))

if average_score >= threshold:

    print(
        "\n✅ Deployment Approved"
    )

else:

    print(
        "\n❌ Deployment Blocked"
    )

# -----------------------------
# Step 8: Key Learning
# -----------------------------

print("\n💡 Key Learning:")
print(
    "AI systems improve faster when evaluation is automated and measured consistently before deployment."
)