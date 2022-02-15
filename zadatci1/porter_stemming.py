from nltk.stem import PorterStemmer
from nltk.tokenize import word_tokenize

root = PorterStemmer()

string = " Today is a sunny day and I can go to work without an umbrella. I do not need it."

tokens = word_tokenize(string)

roots = [root.stem(word) for word in tokens]

print(roots)