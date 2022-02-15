from nltk.tokenize import sent_tokenize, word_tokenize

string = " Today is a sunny day and I can go to work without an umbrella. I do not need it."

print(sent_tokenize(string))

print(word_tokenize(string))