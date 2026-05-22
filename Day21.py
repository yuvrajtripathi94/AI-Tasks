# Day 21: What Makes AI Products Actually Good
# Focus: AI Product Quality Evaluation

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
# Step 2: Define Test Cases
# -----------------------------

test_cases = [
    {
        "question": "What is RAG?",
        "expected_behavior": "Should explain Retrieval-Augmented Generation clearly."
    },

    {
        "question": "Explain embeddings in simple words.",
        "expected_behavior": "Should provide beginner-friendly explanation."
    },

    {
        "question": "Tell me about quantum biology.",
        "expected_behavior": "Should admit lack of knowledge if context unavailable."
    },

    {
        "question": "",
        "expected_behavior": "Should handle empty input gracefully."
    },

    {
        "question": "asdfghjkl",
        "expected_behavior": "Should identify meaningless input."
    }
]

# -----------------------------
# Step 3: AI Assistant Function
# -----------------------------

def ask_ai(question):

    prompt = f"""
You are an AI knowledge assistant.

Answer clearly and honestly.
If information is uncertain, say so.

Question:
{question}
"""

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "user", "content": prompt}
        ]
    )

    return response.choices[0].message.content

# -----------------------------
# Step 4: Product Quality Audit
# -----------------------------

results = []

print("\n🔍 Running AI Product Quality Audit...\n")

for case in test_cases:

    question = case["question"]

    answer = ask_ai(question)

    # Simple quality checks
    helpfulness = len(answer) > 20
    handles_edge_case = (
        "don't know" in answer.lower()
        or "uncertain" in answer.lower()
        or len(question.strip()) == 0
        or question == "asdfghjkl"
    )

    results.append({
        "Question": question,
        "Answer": answer,
        "Helpful": helpfulness,
        "Handled Edge Case": handles_edge_case
    })

    print("Question:", question)
    print("Answer:", answer)
    print("-" * 60)

# -----------------------------
# Step 5: Convert Results to DataFrame
# -----------------------------

df = pd.DataFrame(results)

# -----------------------------
# Step 6: Product Quality Metrics
# -----------------------------

helpfulness_score = df["Helpful"].mean() * 100
edge_case_score = df["Handled Edge Case"].mean() * 100

print("\n📊 Product Quality Metrics:\n")

print(f"Helpfulness Score: {helpfulness_score:.2f}%")
print(f"Edge Case Handling Score: {edge_case_score:.2f}%")

# -----------------------------
# Step 7: Key Product Quality Areas
# -----------------------------

print("\n🚀 What Makes AI Products Good?\n")

quality_factors = [
    "Reliable answers",
    "Graceful failure handling",
    "Low hallucination rate",
    "Good user experience",
    "Fast response time",
    "Clear explanations",
    "Robustness to weird inputs",
    "Transparency and honesty"
]

for factor in quality_factors:
    print(f"- {factor}")

# -----------------------------
# Step 8: Key Learning
# -----------------------------

print("\n💡 Key Learning:")
print("A good AI product is not just accurate — it must be reliable, robust, honest, and useful under real-world conditions.")