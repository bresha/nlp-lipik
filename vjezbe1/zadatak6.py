'''6. Primjeni (4) na nekoj drugoj knjizi.'''


def count_chars(content):
    characters = {}
    for line in content:
        for c in line:
            if c not in characters.keys():
                characters[c] = 1
            else:
                characters[c] += 1
    characters = {k: v for k, v in sorted(characters.items(), key=lambda item: item[1])}
    return characters

def random_char_sequence(content, num_chars):
    content_without_space = content.replace(' ', '')
    rand = random.randint(0, (len(content_without_space) - num_chars))
    seq_of_chars = content_without_space[rand: rand + num_chars]
    return seq_of_chars


with open("knjige/najbolji-na-svijetu.txt") as f:
    content = f.read()

    characters = []
    for line in content:
        for c in line:
            if c not in characters:
                characters.append(c)
    
    chars_to_remove = ['\x0c', '1', '.', '2', ',', '8', '…', '”', '“', ':', '!', '3', '?', '4', '5', '6', '–', '7', '9', '0', '’', '-', '‘', '*', '(', ')', 'â', ';', 'ü', '©', '\n', '\t']

    for c in chars_to_remove:
        content = content.replace(c, "")
    
    chars_count = count_chars(content)

    for key in chars_count.keys():
        print(key, chars_count[key])

    