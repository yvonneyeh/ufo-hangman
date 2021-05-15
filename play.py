import random
import string 
from ufo import ufo

# NOUN LIST
noun_file = open("nouns.txt", "r")
content = noun_file.read()
noun_list = content.split("\n")
noun_file.close()

# MESSAGE LIST
msg_file = open("messages.txt", "r")
content = msg_file.read()
msg_list = content.split("\n")
msg_file.close()

# print(noun_list)
# print(msg_list)
# print(ufo[0])

def get_word():
    """ Randomly selects playable word from noun list. """

    word = random.choice(noun_list)
    while '-' in word or ' ' in word or word == '':
        word = random.choice(noun_list)
    # print(word.upper())
    return word.upper()


def show_ufo(attempts):
    """ Return current UFO for attempt number."""

    return ufo[attempts]


def play():
    word = get_word()
    word_letters = set(word)
    alphabet = set(string.ascii_uppercase)
    codeword = "_ " * len(word)
    guessed = False
    guessed_letters = set()
    attempts = 0
    incorrect = None

    print("UFO: The Game")
    print("Instructions: save us from alien abduction by guessing letters in the codeword.")
    print("\n")
    print(show_ufo(attempts))
    print("\n")
    print("Incorrect Guesses:")
    print(incorrect)
    print("\n")
    print("Codeword:")
    print(codeword)
    print("\n")


def play_ufo():
    pass

if __name__ == '__main__':
    play()