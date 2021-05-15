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


# def play():
#     word = get_word()
#     word_letters = set(word)
#     alphabet = set(string.ascii_uppercase)
#     codeword = "_ " * len(word)
#     guessed = False
#     guessed_letters = set()
#     attempts = 0
#     lives = 6
#     incorrect = None

#     print("UFO: The Game")
#     print("Instructions: save us from alien abduction by guessing letters in the codeword.")
#     print("\n")
#     print(show_ufo(attempts))
#     print("\n")
#     print("Incorrect Guesses:")
#     print(None)
#     print("\n")
#     print("Codeword:")
#     print(codeword)
#     print("\n")


def play(word):
    word_letters = set(word) # unique letters in target word
    alphabet = set(string.ascii_uppercase)
    codeword = "_ " * len(word)
    guessed = False
    guessed_letters = set() # letters guessed by user
    attempts = 0
    lives = 6
    incorrect = None

    print("UFO: The Game")
    print("Instructions: save us from alien abduction by guessing letters in the codeword.")
    # print("\n")
    # print(show_ufo(attempts))
    # print("\n")
    # print("Incorrect Guesses:")
    # print(None)
    # print("\n")
    # print("Codeword:")
    # print(codeword)
    # print("\n")

    while len(word_letters) > 0 and lives > 0:

        current_codeword = [letter if letter in guessed_letters else '_' for letter in word]
        print(show_ufo(attempts))
        # print("\n")
        print("Incorrect Guesses:")
        print(' '.join(guessed_letters))
        print("Codeword:")
        # print("\n")
        print(' '.join(current_codeword))

        guess = input('Please enter your guess: ').upper()
        if guess in alphabet - guessed_letters:
            guessed_letters.add(guess)
            if guess in word_letters:
                word_letters.remove(guess)
                print("Correct! You're closer to cracking the codeword.")

            else:
                lives -= 1
                attempts += 1 
                print('\nIncorrect! The tractor beam pulls the person in further.')

        elif guess in guessed_letters:
            print('\nYou can only guess that letter once, please try again.')

        else:
            print('\nI cannot understand your input. Please guess a single letter.')

    # len(word_letters) == 0 OR lives == 0
    if lives == 0:
        print(show_ufo(attempts))
        print('You lost! The UFO abducted the person! The codeword was', word)
    else:
        print('Correct! You saved the person and earned a medal of honor!')
        print('The codeword is:', word)


def play_game():
    word = get_word()
    play(word)
    while input('Would you like to play again (Y/N)? ').upper() == 'Y':
        word = get_word()
        play(word)
    print('Goodbye!')


if __name__ == '__main__':
    play_game()