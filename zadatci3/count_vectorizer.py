from sklearn.feature_extraction.text import CountVectorizer

text= ['Marko trenira nogomet, te igra nogomet']

vectorizer = CountVectorizer()
vectorizer.fit(text)

vector = vectorizer.transform(text)

print(vectorizer.vocabulary_)
print(vector.toarray())