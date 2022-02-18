'''10. Koliko je riječi u kojima nalazimo sljedove znakova 'do', 're', 'mi', 'fa', 'sol', 'la' i 'ti'?'''

from nltk.tokenize import word_tokenize
import re

with open('knjige/carobnjaci.txt') as f:
    content = f.read()
    tokens = word_tokenize(content)
    music = ['do', 're', 'mi', 'fa', 'sol', 'la', 'ti']

    counter = 0
    for token in tokens:
        for x in music:
            if re.search(x, token):
                counter += 1

    print(counter)

