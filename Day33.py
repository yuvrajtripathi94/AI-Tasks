import os
from openai import OpenAI
from langsmith import traceable

# Environment Variables
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

client = OpenAI(api_key=OPENAI_API_KEY)

# -----------------------------
# Sample Knowledge Base
# -----------------------------

KNOWLEDGE_BASE = {
    "python":
        """
        Python is a high-level programming language.
        It is widely used for web development,
        machine learning, automation, and data science.
        """,

    "ai":
        """
        Artificial Intelligence is the simulation
        of human intelligence by machines.
        """,

    "machine learning":
        """
        Machine Learning is a subset of AI
        that enables systems to learn from data.
        """
}


# -----------------------------
# Retrieval Component
# -----------------------------

@traceable
def retrieve_context(query):

    query_lower = query.lower()

    for key in KNOWLEDGE_BASE:

        if key in query_lower:
            return KNOWLEDGE_BASE[key]

    return "No relevant context found."


# -----------------------------
# Prompt Builder Component
# -----------------------------

@traceable
def build_prompt(question, context):

    prompt = f"""
You are a helpful AI assistant.

Context:
{context}

Question:
{question}

Instructions:
- Answer using the provided context.
- If context is unavailable, clearly mention it.
- Do not hallucinate.

Answer:
"""

    return prompt


# -----------------------------
# LLM Component
# -----------------------------

@traceable
def call_llm(prompt):

    response = client.chat.completions.create(
        model="gpt-4.1-mini",
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ]
    )

    return response.choices[0].message.content


# -----------------------------
# Complete AI Pipeline
# -----------------------------

@traceable
def ai_pipeline(question):

    context = retrieve_context(question)

    prompt = build_prompt(
        question=question,
        context=context
    )

    answer = call_llm(prompt)

    return {
        "question": question,
        "context": context,
        "answer": answer
    }


# -----------------------------
# Failure Test Cases
# -----------------------------

@traceable
def run_evaluation():

    test_cases = [

        # Works
        "Explain Python",

        # Works
        "What is AI?",

        # Works
        "Explain Machine Learning",

        # Retrieval Failure
        "What is the capital of Mars?",

        # Unknown Data
        "Who won IPL 2050?",

        # Ambiguous Query
        "Tell me everything"
    ]

    results = []

    for question in test_cases:

        result = ai_pipeline(question)

        results.append(result)

    return results


# -----------------------------
# Main
# -----------------------------

if __name__ == "__main__":

    print("=" * 70)
    print("DAY 33 - DEBUGGING AI SYSTEMS")
    print("=" * 70)

    outputs = run_evaluation()

    for item in outputs:

        print("\n" + "=" * 70)

        print("QUESTION:")
        print(item["question"])

        print("\nCONTEXT:")
        print(item["context"])

        print("\nANSWER:")
        print(item["answer"])

        print("=" * 70)