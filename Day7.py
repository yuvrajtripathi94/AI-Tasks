# Day 7: Your First Classifier - Sentiment Analysis

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.pipeline import Pipeline
from sklearn.metrics import accuracy_score, classification_report

# Sample sentiment dataset
data = {
    "text": [
        "I love this movie",
        "This film was amazing",
        "I really enjoyed the story",
        "Best movie ever",
        "Fantastic acting and direction",
        "I hate this movie",
        "Worst film I have seen",
        "The story was boring",
        "Terrible experience",
        "Not worth watching"
    ],
    "sentiment": [
        "positive",
        "positive",
        "positive",
        "positive",
        "positive",
        "negative",
        "negative",
        "negative",
        "negative",
        "negative"
    ]
}

# Create DataFrame
df = pd.DataFrame(data)

# Split dataset
X_train, X_test, y_train, y_test = train_test_split(
    df["text"],
    df["sentiment"],
    test_size=0.2,
    random_state=42
)

# Build pipeline
model = Pipeline([
    ("vectorizer", CountVectorizer()),
    ("classifier", MultinomialNB())
])

# Train model
model.fit(X_train, y_train)

# Predictions
y_pred = model.predict(X_test)

# Accuracy
print("Accuracy:", accuracy_score(y_test, y_pred))

# Detailed report
print("\nClassification Report:\n")
print(classification_report(y_test, y_pred))

# Manual test cases
test_sentences = [
    "I really liked this film",
    "This was a horrible movie",
    "Amazing experience and great acting",
    "Waste of time",
    "The movie was okay"
]

print("\nManual Test Predictions:\n")

for sentence in test_sentences:
    prediction = model.predict([sentence])[0]
    print(f"Text: {sentence}")
    print(f"Prediction: {prediction}")
    print("-" * 40)