from textblob import TextBlob

text = "Ja učim NLP"

print(TextBlob(text).ngrams(1))
print(TextBlob(text).ngrams(2))
print(TextBlob(text).ngrams(3))