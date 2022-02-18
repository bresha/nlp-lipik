'''9. Koliko ih ima koje počinju slovom 'nj'?'''

from nltk.tokenize import word_tokenize


with open('knjige/carobnjaci.txt') as f:
    content = f.read()
    tokens = word_tokenize(content)
    counter = 0
    for token in tokens:
        if token[0: 2].lower() == 'nj':
            counter += 1
    print(counter)