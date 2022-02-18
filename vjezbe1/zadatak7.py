'''7. Primjeni (4) na svim knjigama. Zapiši statistiku usporedno, u tablici. U lijepom formatu.'''

import os
import re
import csv
import string


def count_chars(content):
    ascii_lower = string.ascii_lowercase
    ascii_upper = string.ascii_uppercase
    all_chars = ascii_lower + ascii_upper + 'čćđšžČĆĐŠŽ'
    characters = {k: 0 for k in all_chars}
    for line in content:
        for c in line:
            if c not in characters.keys():
                characters[c] = 1
            else:
                characters[c] += 1
    characters = {key: value for key, value in sorted(characters.items())}
    return characters


def chars_count_from_file(filename):
    with open(filename) as f:
        content = f.read()

        content = re.sub("[^a-zA-ZčćđšžČĆĐŠŽ]+", "", content)
        
        chars_count = count_chars(content)

        return chars_count

def save_to_csv(filename, list_of_data):
    
    with open(filename, 'w', newline='') as csvfile:
        fieldnames = [i for i in list_of_data[0].keys()]
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        writer.writeheader()
        for item in list_of_data:
            writer.writerow(item)


def helper(list_paths):
    all_chars = []

    for path in list_paths:
        full_path = os.path.join('knjige', path)
        with open(full_path) as f:
            content = f.read()
            for line in content:
                for c in line:
                    if c not in all_chars:
                        all_chars.append(c)

    return all_chars 

def main():
    files = os.listdir('knjige')

    data = []
    for f in files:
        full_path = os.path.join('knjige', f)
        chars_count = chars_count_from_file(full_path)
        data.append(chars_count)

    filename = 'letters.csv'
    save_to_csv(filename, data)

if __name__ == '__main__':
    main()