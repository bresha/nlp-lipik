import nltk
from nltk.tokenize import word_tokenize

string = " Today is a sunny day and I can go to work without an umbrella. I do not need it. "

words = word_tokenize(string)

print(nltk.pos_tag(words))

print(nltk.help.upenn_tagset())