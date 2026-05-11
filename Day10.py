# Day 10: Build Your First NLP Pipeline

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import accuracy_score, classification_report

# Sample dataset
data = {
    "text": [
        "I love this movie",
        "Amazing experience and great acting",
        "This film was fantastic",
        "I hate this movie",
        "Worst movie ever",
        "Very boring story",
        "Excellent direction and screenplay",
        "Terrible acting and poor script"
    ],
    "label": [
        "positive",
        "positive",
        "positive",
        "negative",
        "negative",
        "negative",
        "positive",
        "negative"
    ]
}

# Create DataFrame
df = pd.DataFrame(data)

# Split data
X_train, X_test, y_train, y_test = train_test_split(
    df["text"],
    df["label"],
    test_size=0.25,
    random_state=42
)

# Build NLP Pipeline
pipeline = Pipeline([
    ("tfidf", TfidfVectorizer()),      # Text → Numerical Features
    ("model", MultinomialNB())         # Classifier
])

# Train model
pipeline.fit(X_train, y_train)

# Predictions
y_pred = pipeline.predict(X_test)

# Evaluation
print("🔹 Accuracy:", accuracy_score(y_test, y_pred))

print("\n🔹 Classification Report:\n")
print(classification_report(y_test, y_pred))

# Manual testing
test_sentences = [
    "I really enjoyed this film",
    "This was a terrible experience"
]

print("\n🔹 Manual Predictions:\n")

for sentence in test_sentences:
    prediction = pipeline.predict([sentence])[0]
    print(f"Text: {sentence}")
    print(f"Prediction: {prediction}")
    print("-" * 50)