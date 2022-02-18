'''8. Koliko ima riječi koje počinju prvim slovom tvog imena u tvojoj najdražoj knjizi?'''

from nltk.tokenize import word_tokenize


with open('knjige/carobnjaci.txt') as f:
    content = f.read()
    tokens = word_tokenize(content)
    counter = 0
    for token in tokens:
        if token[0].lower() == 'h':
            counter += 1
    print(counter)



