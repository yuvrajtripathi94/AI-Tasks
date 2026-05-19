# Day 18: Why LLMs Hallucinate and How to Measure It
# Focus: Hallucination Detection & Quantification Experiment

# Install required libraries
# pip install openai langchain langchain-openai numpy

from openai import OpenAI
import numpy as np

# -----------------------------
# Step 1: Initialize OpenAI Client
# -----------------------------

client = OpenAI(
    api_key="YOUR_API_KEY"
)

# -----------------------------
# Step 2: Create Ground Truth Dataset
# -----------------------------

dataset = [
    {
        "question": "What is FAISS used for?",
        "ground_truth": "FAISS is used for similarity search over vector embeddings."
    },
    {
        "question": "What does RAG stand for?",
        "ground_truth": "RAG stands for Retrieval Augmented Generation."
    },
    {
        "question": "What is an embedding?",
        "ground_truth": "Embeddings are vector representations of text."
    },
    {
        "question": "What is overfitting in ML?",
        "ground_truth": "Overfitting happens when a model learns noise instead of patterns."
    }
]

# -----------------------------
# Step 3: LLM Answer Function (Closed Book)
# -----------------------------

def get_llm_answer(question):
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "user", "content": question}
        ]
    )
    return response.choices[0].message.content

# -----------------------------
# Step 4: Hallucination Checker (LLM-as-Judge)
# -----------------------------

def check_hallucination(question, answer, ground_truth):
    prompt = f"""
You are a strict evaluator.

Check if the model answer is factually consistent with the ground truth.

Return only:
- "TRUE" if answer is correct and supported
- "FALSE" if answer contains hallucination or incorrect info

Ground Truth:
{ground_truth}

Model Answer:
{answer}
"""

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": prompt}]
    )

    verdict = response.choices[0].message.content.strip().upper()
    return "FALSE" in verdict  # hallucination = True/False


# -----------------------------
# Step 5: Run Experiment
# -----------------------------

results = []

print("\n🔍 Running Hallucination Measurement Experiment...\n")

for item in dataset:
    question = item["question"]
    ground_truth = item["ground_truth"]

    answer = get_llm_answer(question)
    is_hallucinated = check_hallucination(question, answer, ground_truth)

    results.append(is_hallucinated)

    print("Q:", question)
    print("Answer:", answer)
    print("Hallucination:", is_hallucinated)
    print("-" * 60)

# -----------------------------
# Step 6: Compute Hallucination Rate
# -----------------------------

hallucination_rate = np.mean(results)

print("\n📊 Final Metrics:")
print(f"Total Questions: {len(dataset)}")
print(f"Hallucinations Detected: {sum(results)}")
print(f"Hallucination Rate: {hallucination_rate:.2f}")

# -----------------------------
# Step 7: Categorizing Why Hallucination Happens
# -----------------------------

print("\n🧠 Possible Causes of Hallucination:\n")

causes = [
    "Model lacks factual grounding (no retrieval context)",
    "Training data ambiguity or conflict",
    "Overgeneralization from learned patterns",
    "Prompt misinterpretation",
    "Guessing when uncertain instead of abstaining"
]

for c in causes:
    print("- " + c)

# -----------------------------
# Step 8: Insight
# -----------------------------

print("\n💡 Insight:")
print("Hallucination is measurable by comparing model outputs against ground truth and evaluating factual consistency.")
print("Reducing hallucination requires grounding (RAG), better prompts, and verification layers.")