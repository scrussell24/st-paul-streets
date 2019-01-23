import sys
import json


def load_streets():
    with open('streets.json', 'r') as f:
        streets = json.loads(f.read())
    return streets


def search_word(streets, word):
    '''
    Match street if contains word
    '''
    return [st for st in streets if word.lower() in st.lower()]


def search_words(streets, *words):
    '''
    Match street if it contains each word in words
    '''
    matches = streets
    for word in words:
        matches = list(filter(lambda x: word.lower() in x.lower(), matches))
    return matches


def search_letters(streets, letters):
    '''
    Match street name if it contains each char in letters
    '''
    matches = streets
    for letter in letters:
        matches = list(filter(lambda x: letter.lower() in x.lower(), matches))
    return matches


if __name__ =='__main__':
    command = sys.argv[1]
    words = sys.argv[2:]
    streets = load_streets()
    if command == 'word':
        matches = search_word(streets, words[0])
    if command == 'words':
        matches = search_words(streets, *words)
    if command == 'letters':
        matches = search_letters(streets, words[0])
    for match in matches:
        print(match)
