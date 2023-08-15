import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.pipeline import make_pipeline

# Sample data
data = {
    'text': ['I love this product!', 'This is terrible.', 'It works well.']
}

df = pd.DataFrame(data)

# Prepare features and labels
X = df['text']
y = [1, 0, 1]  # 1: Positive, 0: Negative

# Build and train the model
model = make_pipeline(CountVectorizer(), MultinomialNB())
model.fit(X, y)

# Test the model
test_text = 'This is amazing!'
result = model.predict([test_text])
print('Sentiment:', 'Positive' if result[0] == 1 else 'Negative')
