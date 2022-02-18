'''11. Koliko je riječi koje počinju velikim slovom, a nisu na početku rečenice?'''

import re
from nltk.tokenize import word_tokenize

with open('knjige/carobnjaci.txt') as f:
    content = f.read()
    tokens = word_tokenize(content)

    counter = 0
    for token in tokens:
        if re.search("[a-z]+[A-Z]", token):
            counter += 1
    print(counter)
