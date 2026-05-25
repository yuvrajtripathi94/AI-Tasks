# Day 24: Building Conversation Memory Systems
# Stateful AI Conversations using FastAPI + LangChain

# Install required libraries
# pip install fastapi uvicorn langchain langchain-openai openai

from fastapi import FastAPI
from pydantic import BaseModel
from langchain_openai import ChatOpenAI
from langchain.memory import ConversationBufferWindowMemory
from langchain.chains import ConversationChain

# -----------------------------
# Step 1: Initialize FastAPI
# -----------------------------

app = FastAPI(
    title="Conversation Memory API",
    version="1.0"
)

# -----------------------------
# Step 2: Initialize LLM
# -----------------------------

llm = ChatOpenAI(
    api_key="YOUR_API_KEY",
    model="gpt-3.5-turbo"
)

# -----------------------------
# Step 3: Create Memory System
# -----------------------------

# Keeps only last 5 interactions
# Prevents token overflow

memory = ConversationBufferWindowMemory(
    k=5,
    return_messages=True
)

# -----------------------------
# Step 4: Create Conversation Chain
# -----------------------------

conversation = ConversationChain(
    llm=llm,
    memory=memory,
    verbose=False
)

# -----------------------------
# Step 5: Request Schema
# -----------------------------

class ChatRequest(BaseModel):
    message: str

# -----------------------------
# Step 6: Chat Endpoint
# -----------------------------

@app.post("/chat")

def chat(request: ChatRequest):

    user_message = request.message

    # Generate AI response using memory
    response = conversation.predict(
        input=user_message
    )

    # Return response
    return {
        "user_message": user_message,
        "ai_response": response
    }

# -----------------------------
# Step 7: Memory Inspection Endpoint
# -----------------------------

@app.get("/memory")

def get_memory():

    return {
        "conversation_history":
        memory.buffer_as_str
    }

# -----------------------------
# Step 8: Run Server
# -----------------------------

# Run using:
# uvicorn main:app --reload

# Example:
# uvicorn main:app --reload

# -----------------------------
# Step 9: Example Requests
# -----------------------------

# POST /chat
# {
#   "message": "My name is Yuvraj."
# }

# POST /chat
# {
#   "message": "What is my name?"
# }

# AI remembers previous context

# -----------------------------
# Step 10: Key Learning
# -----------------------------

print("✅ Stateful AI Conversation System Ready")
print("The assistant can now remember previous conversation context.")