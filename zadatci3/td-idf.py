from sklearn.feature_extraction.text import TfidfVectorizer

text = ["The big yellow car was faster than the small red bike", "The car", "The bike"]

vectorizer = TfidfVectorizer()
vectorizer.fit(text)

print(vectorizer.vocabulary_)
print(vectorizer.idf_)

print('-' * 15)

vector = vectorizer.transform(text)
print(vector.toarray())