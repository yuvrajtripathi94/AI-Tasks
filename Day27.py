# Day 27: Structured Tool Calling with OpenAI Functions API
# Reliable AI Agent using Function Calling

# Install required libraries
# pip install openai fastapi uvicorn

from openai import OpenAI
from fastapi import FastAPI
from pydantic import BaseModel
import json

# -----------------------------
# Step 1: Initialize OpenAI Client
# -----------------------------

client = OpenAI(
    api_key="YOUR_API_KEY"
)

# -----------------------------
# Step 2: Create FastAPI App
# -----------------------------

app = FastAPI(
    title="Function Calling Agent API"
)

# -----------------------------
# Step 3: Define Tools
# -----------------------------

def calculator(expression):

    try:
        return str(eval(expression))

    except Exception:
        return "Calculation Error"

def search_knowledge(query):

    knowledge_base = {
        "rag":
        "RAG stands for Retrieval-Augmented Generation.",

        "faiss":
        "FAISS is used for vector similarity search.",

        "embedding":
        "Embeddings convert text into vectors."
    }

    return knowledge_base.get(
        query.lower(),
        "No information found."
    )

# -----------------------------
# Step 4: Function Definitions
# -----------------------------

tools = [

    {
        "type": "function",

        "function": {
            "name": "calculator",

            "description":
            "Perform mathematical calculations.",

            "parameters": {
                "type": "object",

                "properties": {
                    "expression": {
                        "type": "string"
                    }
                },

                "required": ["expression"]
            }
        }
    },

    {
        "type": "function",

        "function": {
            "name": "search_knowledge",

            "description":
            "Search AI knowledge base.",

            "parameters": {
                "type": "object",

                "properties": {
                    "query": {
                        "type": "string"
                    }
                },

                "required": ["query"]
            }
        }
    }
]

# -----------------------------
# Step 5: Request Schema
# -----------------------------

class ChatRequest(BaseModel):
    question: str

# -----------------------------
# Step 6: Function Calling Agent
# -----------------------------

@app.post("/chat")

def chat(request: ChatRequest):

    messages = [
        {
            "role": "user",
            "content": request.question
        }
    ]

    # First LLM call
    response = client.chat.completions.create(
        model="gpt-4o-mini",

        messages=messages,

        tools=tools,

        tool_choice="auto"
    )

    message = response.choices[0].message

    # -----------------------------
    # Step 7: Handle Tool Calls
    # -----------------------------

    if message.tool_calls:

        tool_outputs = []

        for tool_call in message.tool_calls:

            function_name = (
                tool_call.function.name
            )

            arguments = json.loads(
                tool_call.function.arguments
            )

            # Execute function
            if function_name == "calculator":

                result = calculator(
                    arguments["expression"]
                )

            elif function_name == "search_knowledge":

                result = search_knowledge(
                    arguments["query"]
                )

            else:
                result = "Unknown function"

            tool_outputs.append({
                "tool": function_name,
                "result": result
            })

            # Add tool response
            messages.append(message)

            messages.append({
                "role": "tool",

                "tool_call_id": tool_call.id,

                "content": result
            })

        # -----------------------------
        # Step 8: Final LLM Response
        # -----------------------------

        final_response = client.chat.completions.create(
            model="gpt-4o-mini",

            messages=messages
        )

        final_answer = (
            final_response
            .choices[0]
            .message.content
        )

        return {
            "question": request.question,
            "tool_outputs": tool_outputs,
            "final_answer": final_answer
        }

    # If no tool used
    return {
        "question": request.question,
        "final_answer": message.content
    }

# -----------------------------
# Step 9: Run Server
# -----------------------------

# Run using:
# uvicorn main:app --reload

# -----------------------------
# Step 10: Example Request
# -----------------------------

# POST /chat
# {
#   "question":
#   "What is RAG and calculate 45 * 12"
# }

# -----------------------------
# Step 11: Reliability Comparison
# -----------------------------

print("\n📊 Reliability Improvements:\n")

improvements = [
    "No fragile text parsing",
    "Structured JSON tool calls",
    "Reliable argument extraction",
    "Reduced formatting errors",
    "Better autonomous execution",
    "Safer tool orchestration"
]

for item in improvements:
    print(f"- {item}")

# -----------------------------
# Step 12: Key Learning
# -----------------------------

print("\n💡 Key Learning:")
print("Function calling makes AI agents more reliable by replacing fragile text parsing with structured tool invocation.")