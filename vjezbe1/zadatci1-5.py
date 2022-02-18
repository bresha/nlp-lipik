'''1. Izaberi knjigu. To je danas tvoja najdraža knjiga. Učitaj je u varijablu.

2. Popiši sve znakove koji se pojavljuju u tvojoj najdražoj knjizi.

3. Odluči koje znakove želiš zadržati. Očisti svoju knjigu
od nepoželjnih znakova. Jasno, ovaj će korak ovisit o tvojim namjerama.
(I o sljedećim zadatcima.) Ne spremati promjene u file.

4. Napravi funkciju koja će u odabranoj knjizi prebrojati koliko ima kojih slova.
Podijeli statistiku sa svojim najdražim kolegom/kolegicom. Usporedite statistike.

5. Učitaj slučajnih 100 znakova (slijedno, i ne broje se space-ovi), prebroj koliko ima kojih slova. 
Usporedi s rezultatima nad cijelom knjigom. Zanimljivo? Što se događa sa slučajnih 1000 znakova?'''


import random


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


with open("knjige/carobnjaci.txt") as f:
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

    num_chars = 1000
    rand_seq_of_chars = random_char_sequence(content, num_chars)
    counted_rand_seq_of_chars = count_chars(rand_seq_of_chars)

    for key in counted_rand_seq_of_chars.keys():
        print(key, counted_rand_seq_of_chars[key])


    
