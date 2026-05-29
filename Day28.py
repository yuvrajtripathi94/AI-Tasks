# Day 28: Multi-Step AI Workflows with State Management
# Stateful Multi-Step AI Agent using LangChain + OpenAI

# Install required libraries
# pip install langchain langchain-openai openai

from langchain_openai import ChatOpenAI
import json
import os

# -----------------------------
# Step 1: Initialize LLM
# -----------------------------

llm = ChatOpenAI(
    api_key="YOUR_API_KEY",
    model="gpt-3.5-turbo"
)

# -----------------------------
# Step 2: Persistent State File
# -----------------------------

STATE_FILE = "workflow_state.json"

# -----------------------------
# Step 3: Save Workflow State
# -----------------------------

def save_state(state):

    with open(STATE_FILE, "w") as f:
        json.dump(state, f, indent=4)

# -----------------------------
# Step 4: Load Workflow State
# -----------------------------

def load_state():

    if os.path.exists(STATE_FILE):

        with open(STATE_FILE, "r") as f:
            return json.load(f)

    return {
        "step": 0,
        "topic": "",
        "search_results": "",
        "summary": "",
        "final_report": ""
    }

# -----------------------------
# Step 5: Workflow Steps
# -----------------------------

def search_information(topic):

    # Simulated search step
    return f"""
AI agents are systems that can reason,
use tools, and complete tasks autonomously.

Multi-step workflows allow AI systems
to complete complex tasks sequentially.
"""

def summarize_information(text):

    prompt = f"""
Summarize the following text:

{text}
"""

    response = llm.invoke(prompt)

    return response.content

def generate_report(summary):

    prompt = f"""
Generate a professional research report
using this summary:

{summary}
"""

    response = llm.invoke(prompt)

    return response.content

# -----------------------------
# Step 6: Start Workflow
# -----------------------------

state = load_state()

# User Topic
topic = "AI Multi-Step Agent Workflows"

# -----------------------------
# Step 7: Step 1 - Search
# -----------------------------

if state["step"] < 1:

    print("\n🔍 Step 1: Searching Information...\n")

    search_results = search_information(topic)

    state["topic"] = topic
    state["search_results"] = search_results
    state["step"] = 1

    save_state(state)

    print(search_results)

# -----------------------------
# Step 8: Step 2 - Summarization
# -----------------------------

if state["step"] < 2:

    print("\n🧠 Step 2: Summarizing Information...\n")

    summary = summarize_information(
        state["search_results"]
    )

    state["summary"] = summary
    state["step"] = 2

    save_state(state)

    print(summary)

# -----------------------------
# Step 9: Step 3 - Report Generation
# -----------------------------

if state["step"] < 3:

    print("\n📄 Step 3: Generating Final Report...\n")

    report = generate_report(
        state["summary"]
    )

    state["final_report"] = report
    state["step"] = 3

    save_state(state)

    print(report)

# -----------------------------
# Step 10: Workflow Complete
# -----------------------------

print("\n✅ Workflow Completed Successfully")

# -----------------------------
# Step 11: Why State Management Matters
# -----------------------------

print("\n🚀 Benefits of Persistent State:\n")

benefits = [
    "Resume interrupted workflows",
    "Avoid recomputing completed steps",
    "Track workflow progress",
    "Improve reliability",
    "Enable long-running AI tasks",
    "Reduce API costs"
]

for item in benefits:
    print(f"- {item}")

# -----------------------------
# Step 12: Key Learning
# -----------------------------

print("\n💡 Key Learning:")
print("State management is essential for reliable multi-step AI workflows where tasks depend on previous outputs.")