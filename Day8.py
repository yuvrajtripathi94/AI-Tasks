# Day 8: How Machines Clean and Understand Text

import nltk
import string
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords

# Download required resources
nltk.download('punkt')
nltk.download('stopwords')

# Sample text
text = """
Artificial Intelligence is changing the world!
Machines can now understand human language, analyze data,
and make smart decisions.
"""

print("🔹 Original Text:\n")
print(text)

# Step 1: Tokenization
tokens = word_tokenize(text)
print("\n🔹 Tokens:\n")
print(tokens)

# Step 2: Convert to lowercase
tokens = [word.lower() for word in tokens]

# Step 3: Remove punctuation
tokens = [word for word in tokens if word not in string.punctuation]
print("\n🔹 After Removing Punctuation:\n")
print(tokens)

# Step 4: Remove stopwords
stop_words = set(stopwords.words('english'))

clean_tokens = [
    word for word in tokens
    if word not in stop_words
]

print("\n🔹 Cleaned Tokens:\n")
print(clean_tokens)

# Step 5: Join cleaned text
clean_text = " ".join(clean_tokens)

print("\n🔹 Final Cleaned Text:\n")
print(clean_text)