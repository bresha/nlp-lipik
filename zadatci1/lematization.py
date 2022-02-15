from nltk.stem import WordNetLemmatizer
from nltk.tokenize import word_tokenize

lem = WordNetLemmatizer()

string = "If mountains were bigger, we would be smaller"

words = word_tokenize(string)

lem_words = [lem.lemmatize(word) for word in words]

print(lem_words)