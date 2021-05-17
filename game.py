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

# GAME STATUS CATEGORIES
STATUS_WIN = "win"
STATUS_LOSE = "lose"
STATUS_PLAYING = "playing"


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


class Game(object):
    """ A UFO Hangman Game object. """

    def __init__(self, word):
        self.word_letters = set(word) # unique letters in target word
        self.alphabet = set(string.ascii_uppercase) # all valid playable letters
        self.guessed_letters = set() # letters guessed by player
        self.attempts = 0
        self.lives = 6
        self.status = STATUS_PLAYING
        self.word = word


    def start():
        """ Display the title and instructions of the game """

        print("UFO: The Game")
        print("Instructions: save us from alien abduction by guessing letters in the codeword.")


    def play(self, word):
    # def generate_gameboard(self, word):
        """ Generate the gameboard during game play. """

        while len(self.word_letters) > 0 and self.lives > 0:

            current_codeword = [letter if letter in self.guessed_letters else '_' for letter in word]
            print(show_ufo(self.attempts))
            print("Incorrect Guesses:")
            print(' '.join(self.guessed_letters))
            print("Codeword:")
            print(' '.join(current_codeword))
            guess = input('Please enter your guess: ').upper()
            Game.process_guess(self, guess)


    def check_status(self):
        """ Check current gameplay status. """

        if self.status == STATUS_LOSE:
            raise ValueError("You already lost!")
        elif self.status == STATUS_WIN:
            raise ValueError("You already won!")         

        # Check for win or lose
        if self.lives < 0:
            self.status = STATUS_LOSE
        # If all letters guessed correctly
        if all([l in self.guessed_letters for l in self.word]):
            self.status = STATUS_WIN


    def retrieve_guess(self):
        """ Get user input for a guess. """
        
        guess = input('Please enter your guess: ').upper()

        return guess


    def process_guess(self, guess):
        """ Process a player's guess during the game. """

        # CORRECT LETTER
        if guess in self.alphabet - self.guessed_letters: 
            self.guessed_letters.add(guess)
            if guess in self.word_letters:
                self.word_letters.remove(guess)
                print("Correct! You're closer to cracking the codeword.")
            # INCORRECT LETTER
            else:
                self.lives -= 1
                self.attempts += 1 
                print('\nIncorrect! The tractor beam pulls the person in further.')
                print(get_message())

        elif guess in self.guessed_letters:
            print('\nYou can only guess that letter once, please try again.')

        else:
            print('\nI cannot understand your input. Please guess a single letter.')

        # len(word_letters) == 0 OR lives == 0
        if self.lives == 0:
            # LOSING PLAY ...
            print(show_ufo(self.attempts))
            print('You lost! The UFO abducted the person! The codeword was', self.word)
        if all([letters in self.guessed_letters for letters in self.word]):
            # WINNING PLAY!
            print('Correct! You saved the person and earned a medal of honor!')
            print('The codeword is:', self.word)


    def get_status(self):
        """ Get the current status of gameplay. """

        return self.status


def play_game():
    """ Initiate gameplay. """

    word = get_word()
    UFO = Game(word)
    Game.start()
    Game.play(UFO, word)
    while input('Would you like to play again (Y/N)? ').upper() == 'Y':
        word = get_word()
        UFO = Game(word)
        Game.start()
        Game.play(UFO, word)
    print('Goodbye!')



if __name__ == '__main__':
    play_game()