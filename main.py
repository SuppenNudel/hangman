import csv
import random
import re

asked_letters = set()
lifes = 6


def let_guess():
    while(not re.match("[A-Za-z]", guess := input('guess letter: '))):
        print('please enter only a letter. try again')
    else:
        return guess.upper()


def get_word():
    words = list()
    with open('gen1.csv', encoding='utf-8') as csvfile:
        reader = csv.reader(csvfile)  # , delimiter=' ', quotechar='|'
        for idx, row in enumerate(reader):
            if idx != 0:
                words.append(row[1])
    return random.choice(words).upper()


def is_solved(the_word, display):
    return the_word == display


def display_state(the_word):
    display = ''
    for letter in the_word:
        if letter == ' ' or letter in asked_letters:
            display += letter
        else:
            display += '_'
    print(' '.join(display))
    return display


def start_game():
    print('starting game')
    the_word = get_word()
    while not is_solved(the_word, display_state(the_word)):
        global lifes
        print(f'{lifes} lifes left')
        if lifes == 0:
            print('you run out of lifes')
            print(f'the word was {the_word}')
            return
        letter = let_guess()
        if not letter in the_word:
            lifes -= 1
        asked_letters.add(letter)
        print()
        print(sorted(asked_letters))
    print('you won')


if __name__ == "__main__":
    start_game()
