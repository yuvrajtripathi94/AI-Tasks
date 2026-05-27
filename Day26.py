# Day 26: Introduction to AI Agents and the ReAct Pattern
# Manual ReAct Agent using Python + OpenAI API

# Install required libraries
# pip install openai

from openai import OpenAI

# -----------------------------
# Step 1: Initialize OpenAI Client
# -----------------------------

client = OpenAI(
    api_key="YOUR_API_KEY"
)

# -----------------------------
# Step 2: Define Simple Tools
# -----------------------------

def calculator(expression):

    try:
        return eval(expression)

    except Exception:
        return "Calculation Error"

def search_knowledge_base(query):

    knowledge = {
        "rag":
        "RAG stands for Retrieval-Augmented Generation.",

        "faiss":
        "FAISS is used for vector similarity search.",

        "embedding":
        "Embeddings convert text into vectors."
    }

    return knowledge.get(
        query.lower(),
        "No information found."
    )

# -----------------------------
# Step 3: Tool Dispatcher
# -----------------------------

def use_tool(tool_name, tool_input):

    if tool_name == "calculator":
        return calculator(tool_input)

    elif tool_name == "search":
        return search_knowledge_base(tool_input)

    else:
        return "Unknown Tool"

# -----------------------------
# Step 4: ReAct Prompt
# -----------------------------

SYSTEM_PROMPT = """
You are a ReAct AI Agent.

You must think step-by-step.

Available tools:
1. calculator
2. search

Response Format:

Thought: think about the problem
Action: tool_name
Action Input: input for tool

When you know the answer:

Final Answer: answer here
"""

# -----------------------------
# Step 5: User Query
# -----------------------------

user_query = "What is RAG and what is 25 * 4?"

# -----------------------------
# Step 6: Agent Loop
# -----------------------------

conversation = [
    {
        "role": "system",
        "content": SYSTEM_PROMPT
    },

    {
        "role": "user",
        "content": user_query
    }
]

print("\n🤖 Running ReAct Agent...\n")

for step in range(5):

    response = client.chat.completions.create(
        model="gpt-4o-mini",

        messages=conversation
    )

    agent_reply = response.choices[0].message.content

    print(f"\nStep {step + 1}:\n")
    print(agent_reply)

    # Stop if final answer reached
    if "Final Answer:" in agent_reply:
        break

    # Parse Action
    try:

        lines = agent_reply.split("\n")

        action = None
        action_input = None

        for line in lines:

            if line.startswith("Action:"):
                action = line.replace(
                    "Action:",
                    ""
                ).strip()

            if line.startswith("Action Input:"):
                action_input = line.replace(
                    "Action Input:",
                    ""
                ).strip()

        # Execute Tool
        observation = use_tool(
            action,
            action_input
        )

        print("\nObservation:")
        print(observation)

        # Add observation back to conversation
        conversation.append({
            "role": "assistant",
            "content": agent_reply
        })

        conversation.append({
            "role": "user",
            "content": f"Observation: {observation}"
        })

    except Exception as e:

        print("Parsing Error:", e)
        break

# -----------------------------
# Step 7: Key Learning
# -----------------------------

print("\n💡 Key Learning:")
print("AI agents combine reasoning and tool usage to solve problems step-by-step instead of generating answers in one shot.")