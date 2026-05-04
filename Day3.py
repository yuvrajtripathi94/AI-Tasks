# Day 3: Text Preprocessing - Turning Words into Numbers

# Install (run once if needed)
# !pip install nltk

import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
import string
from sklearn.feature_extraction.text import CountVectorizer

# Download required resources (run once)
nltk.download('punkt')
nltk.download('stopwords')

# Sample text
text = """
Machine learning is amazing! It allows computers to learn from data and make decisions.
Natural Language Processing is a part of AI that deals with text data.
"""

print("Original Text:\n", text)

# Step 1: Tokenization
tokens = word_tokenize(text)
print("\nTokens:\n", tokens)

# Step 2: Remove punctuation
tokens_no_punct = [word for word in tokens if word not in string.punctuation]
print("\nWithout Punctuation:\n", tokens_no_punct)

# Step 3: Remove stopwords
stop_words = set(stopwords.words('english'))
filtered_tokens = [word for word in tokens_no_punct if word.lower() not in stop_words]
print("\nAfter Removing Stopwords:\n", filtered_tokens)

# Step 4: Lowercasing
processed_tokens = [word.lower() for word in filtered_tokens]
print("\nFinal Processed Tokens:\n", processed_tokens)

# Step 5: Convert to Bag of Words
corpus = [" ".join(processed_tokens)]

vectorizer = CountVectorizer()
X = vectorizer.fit_transform(corpus)

print("\nBag of Words Vocabulary:\n", vectorizer.vocabulary_)
print("\nBag of Words Vector:\n", X.toarray())