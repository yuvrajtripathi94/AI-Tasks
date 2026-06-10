import time
from cache import get_cache, set_cache
from vector_db import retrieve_docs

def get_rag_response(question):

    # Step 1: Cache Check
    cached = get_cache(question)

    if cached:
        return {
            "answer": cached,
            "source": "cache",
            "latency": 0
        }

    start = time.time()

    # Step 2: Retrieve context
    docs = retrieve_docs(question)

    context = "\n".join(docs)

    # Step 3: Simulated LLM response
    answer = f"Answer based on context: {context}"

    # Step 4: Save cache
    set_cache(question, answer)

    latency = round(time.time() - start, 2)

    return {
        "answer": answer,
        "source": "llm",
        "latency": latency
    }