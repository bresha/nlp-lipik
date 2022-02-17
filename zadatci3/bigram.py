from sklearn.feature_extraction.text import CountVectorizer


text = ["Ja igram nogomet, te ću nogomet igrati još jako dugo"]

vectorizer = CountVectorizer(ngram_range=(2, 2))
vectorizer.fit(text)

vector = vectorizer.transform(text)

print(vectorizer.vocabulary_)
print(vector.toarray())