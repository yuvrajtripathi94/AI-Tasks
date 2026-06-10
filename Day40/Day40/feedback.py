feedback_store = []

def save_feedback(question, answer, rating):

    feedback_store.append({
        "question": question,
        "answer": answer,
        "rating": rating
    })

def get_stats():

    if not feedback_store:
        return {
            "total_feedback": 0,
            "avg_rating": 0
        }

    avg = sum(f["rating"] for f in feedback_store) / len(feedback_store)

    return {
        "total_feedback": len(feedback_store),
        "avg_rating": round(avg, 2)
    }