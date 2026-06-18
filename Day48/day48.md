To build product-specific memory, think beyond storing chat history. The goal is to capture **structured knowledge about the user** that improves future experiences.

For example:

* A fitness app remembers workout preferences, injuries, and progress.
* A learning platform remembers skill level, completed lessons, and weak topics.
* A finance app remembers goals, risk tolerance, and spending patterns.

The key question is:

> **"What information will help my product provide a better experience next time?"**

## Step 1: Define Your Memory Model

Separate memory into categories relevant to your product.

| Memory Type         | Example                                     | Update Frequency |
| ------------------- | ------------------------------------------- | ---------------- |
| Preferences         | Dark mode, learning style, favourite topics | Rarely           |
| Profile             | Skill level, goals, role                    | Occasionally     |
| Progress            | Completed lessons, streaks, milestones      | Frequently       |
| Interaction History | Recent questions, actions taken             | Frequently       |
| Derived Insights    | Weak areas, interests, habits               | Periodically     |

### Example: AI Learning Assistant

```json
{
  "user_id": 123,
  "preferences": {
    "difficulty": "beginner",
    "learning_style": "visual"
  },
  "progress": {
    "completed_topics": ["Python Basics"],
    "quiz_score": 78
  },
  "insights": {
    "weak_topics": ["Recursion"]
  }
}
```

---

## Step 2: Design a SQLite Schema

Create tables for users, memories, and events.

```sql
CREATE TABLE users (
    id INTEGER PRIMARY KEY,
    name TEXT
);

CREATE TABLE memories (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    user_id INTEGER NOT NULL,
    category TEXT NOT NULL,
    key TEXT NOT NULL,
    value TEXT NOT NULL,
    confidence REAL DEFAULT 1.0,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    UNIQUE(user_id, category, key)
);

CREATE TABLE events (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    user_id INTEGER NOT NULL,
    event_type TEXT,
    data TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
```

### Why separate events from memories?

* **Events** are raw interactions.
* **Memories** are distilled information extracted from events.

For example:

* Event: User completed a Python quiz and scored 40%.
* Memory: User struggles with Python functions.

---

## Step 3: Extract Memories Using an LLM

After each interaction:

1. Store the raw event.
2. Send recent context to the model.
3. Ask the model to determine whether anything important should be remembered.
4. Save structured memory updates.

### Prompt Example

```text
You are a memory extraction system.

Given the interaction, extract only information that will improve future experiences.

Return JSON:

{
  "memories": [
    {
      "category": "",
      "key": "",
      "value": "",
      "confidence": 0.0
    }
  ]
}
```

User interaction:

"I prefer short video lessons and struggle with recursion."

````

Expected output:

```json
{
  "memories": [
    {
      "category": "preferences",
      "key": "learning_style",
      "value": "short_video_lessons",
      "confidence": 0.95
    },
    {
      "category": "insights",
      "key": "weak_topic",
      "value": "recursion",
      "confidence": 0.90
    }
  ]
}
````

---

## Step 4: Build the Memory Service with FastAPI

```python
from fastapi import FastAPI
import sqlite3
import json

app = FastAPI()

def get_db():
    return sqlite3.connect("memory.db")

@app.post("/memory")
def save_memory(user_id: int, category: str,
                key: str, value: str,
                confidence: float = 1.0):

    conn = get_db()
    cursor = conn.cursor()

    cursor.execute("""
        INSERT INTO memories
        (user_id, category, key, value, confidence)

        VALUES (?, ?, ?, ?, ?)

        ON CONFLICT(user_id, category, key)
        DO UPDATE SET
            value = excluded.value,
            confidence = excluded.confidence,
            updated_at = CURRENT_TIMESTAMP
    """, (user_id, category, key, value, confidence))

    conn.commit()
    conn.close()

    return {"status": "saved"}
```

---

## Step 5: Retrieve Relevant Memories

Do not inject all memories into every prompt.

Retrieve only what is relevant to the current request.

Example:

```python
def get_relevant_memories(user_id, categories):
    conn = get_db()
    cursor = conn.cursor()

    placeholders = ",".join("?" * len(categories))

    query = f"""
        SELECT category, key, value
        FROM memories
        WHERE user_id = ?
        AND category IN ({placeholders})
    """

    cursor.execute(query, [user_id] + categories)

    results = cursor.fetchall()
    conn.close()

    return results
```

For a tutoring query, retrieve:

* Learning preferences
* Skill level
* Weak topics

Ignore unrelated memories.

---

## Step 6: Personalise Responses

Build prompts using relevant memories.

```text
User profile:

- Skill level: Beginner
- Prefers visual explanations
- Weak topic: Recursion

Current question:

"Explain binary trees."
```

Result:

* Simpler explanations
* Visual analogies
* Extra attention to recursive concepts

---

## Step 7: Manage Memory Lifecycle

Memory should evolve over time.

Implement:

* **Confidence scores**
* **Expiration rules**
* **User editing**
* **Memory deletion**
* **Conflict resolution**

Example:

```text
Old memory: Prefers beginner content
New behaviour: Consistently solves advanced problems

Update memory:
Skill level = Intermediate
```

---

## Step 8: Integrate the OpenAI API

Example extraction workflow:

```python
from openai import OpenAI

client = OpenAI()

response = client.responses.create(
    model="gpt-5-mini",
    input=prompt
)

memory_updates = response.output_text
```

Recommended pipeline:

```text
User Action
    ↓
Store Event
    ↓
Extract Memory
    ↓
Save Structured Memory
    ↓
Retrieve Relevant Memory
    ↓
Generate Personalised Response
```

## Best Practices

* Remember only high-value information.
* Separate facts from temporary context.
* Keep memories structured and searchable.
* Let users view and delete memories.
* Retrieve selectively.
* Continuously update memories based on behaviour.

A successful memory system answers three questions:

1. **What should be remembered?**
2. **When should it be updated?**
3. **When should it be forgotten?**
