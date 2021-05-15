import re
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


def get_word():
    """ Randomly selects playable word from noun list. """

    word = random.choice(noun_list)
    while '-' in word or ' ' in word or word == '':
        word = random.choice(noun_list)

    return word.upper()


def get_message():
    """ Show a random encouraging message when the user guesses an incorrect letter. """
    
    message = random.choice(msg_list)

    return message


def show_ufo(attempts):
    """ Return current UFO for attempt number."""

    return ufo[attempts]


def play(word):
    word_letters = set(word) # unique letters in target word
    alphabet = set(string.ascii_uppercase) # all valid playable letters
    guessed_letters = set() # letters guessed by user
    attempts = 0
    lives = 6

    print("UFO: The Game")
    print("Instructions: save us from alien abduction by guessing letters in the codeword.")

    while len(word_letters) > 0 and lives > 0:

        current_codeword = [letter if letter in guessed_letters else '_' for letter in word]
        print(show_ufo(attempts))
        print("Incorrect Guesses:")
        print(' '.join(guessed_letters))
        print("Codeword:")
        print(' '.join(current_codeword))

        guess = input('Please enter your guess: ').upper()
        # CORRECT LETTER
        if guess in alphabet - guessed_letters: 
            guessed_letters.add(guess)
            if guess in word_letters:
                word_letters.remove(guess)
                print("Correct! You're closer to cracking the codeword.")
            # INCORRECT LETTER
            else:
                lives -= 1
                attempts += 1 
                print('\nIncorrect! The tractor beam pulls the person in further.')
                print(get_message())

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