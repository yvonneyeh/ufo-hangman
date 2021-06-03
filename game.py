import re
import random
import string
from ufo import ufo

ALPHABET = set(string.ascii_uppercase)  # all valid playable letters

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
STATUS_CORRECT = "correct"
STATUS_INCORRECT = "incorrect"
STATUS_INVALID = "invalid"
STATUS_DUPE = "duplicate"

# DEFAULT MESSAGES
INTRO = "UFO: The Game\nInstructions: save us from alien abduction by guessing letters in the codeword."
CORRECT = "Correct! You're closer to cracking the codeword."
INCORRECT = "Incorrect! The tractor beam pulls the person in further."
ALREADY_GUESSED = "You can only guess that letter once, please try again."
INVALID_GUESS = "I cannot understand your input. Please guess a single letter."
LOSE_MSG = "You lost! The UFO abducted the person! The codeword was:"
WIN_MSG = "Correct! You saved the person and earned a medal of honor!\nThe codeword is:"


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
        self.guessed_letters = set() # letters guessed by player
        self.attempts = 0
        self.lives = 6
        self.status = STATUS_PLAYING
        self.word = word


    def start():
        """ Display the title and instructions of the game """

        print(INTRO)


    def play(self, word):
        """ Play UFO Hangman! """

        while len(self.word_letters) > 0 and self.lives > 0:

            self.generate_gameboard(word)
            guess = self.retrieve_guess()
            self.process_guess(guess)


    def generate_gameboard(self, word):
        """ Generate the gameboard during game play. """

        current_codeword = [letter if letter in self.guessed_letters else '_' for letter in word]
        print(show_ufo(self.attempts))
        print("Incorrect Guesses:")
        print(' '.join(self.guessed_letters))
        print("Codeword:")
        print(' '.join(current_codeword))


    def calculate_progress(self):
        """ Future feature: more efficient runtime with dictionary implementation of current progress.  """

        # Something like:
        # self.word = dict{'a': {index: [0, 2], guessed: false}}
        # self.word = dict{0: {letter: a, guessed: false}}
        # Rather than recalculating "current_codeword" every time, tracking differences would be easier
        pass


    def check_status(self):
        """ Check current gameplay status. """

        if self.status == STATUS_LOSE:
            raise ValueError("You already lost!")
        elif self.status == STATUS_WIN:
            raise ValueError("You already won!")

        # Check for win or lose
        if self.lives <= 0:
            self.status = STATUS_LOSE
        # If all letters guessed correctly
        if all([letter in self.guessed_letters for letter in self.word]):
            self.status = STATUS_WIN

        return self.status


    def retrieve_guess(self):
        """ Get user input for a guess. """

        guess = input('Please enter your guess: ').upper()

        return guess


    def process_guess(self, guess):
        """ Process a player's guess during the game. """

        if type(guess) != str or len(guess) != 1 or guess not in ALPHABET:
            print(INVALID_GUESS)
            return STATUS_INVALID

        guess = guess.upper()

        if guess in self.guessed_letters:
            print(ALREADY_GUESSED)
            return STATUS_DUPE

        # CORRECT LETTER
        if guess in ALPHABET - self.guessed_letters:
            self.guessed_letters.add(guess)
            if guess in self.word_letters:
                self.word_letters.remove(guess)
                if all([letters in self.guessed_letters for letters in self.word]):
                # if self.guessed_letters == self.word_letters:
                    # WINNING PLAY!
                    self.status = STATUS_WIN
                    print(WIN_MSG, self.word)
                    return STATUS_WIN
                print(CORRECT)
                return STATUS_CORRECT

            # INCORRECT LETTER
            else:
                self.lives -= 1
                self.attempts += 1
                # len(word_letters) == 0 OR lives == 0
                if self.lives == 0:
                    # LOSING PLAY ...
                    self.status = STATUS_LOSE
                    print(show_ufo(self.attempts))
                    print(LOSE_MSG, self.word)
                    return STATUS_LOSE
                print(INCORRECT)
                print(get_message())
                return STATUS_INCORRECT

        else:
            print(INVALID_GUESS)
            return STATUS_INVALID

    def get_status(self):
        """ Get the current status of gameplay. """

        return self.status


    def playing():
        """ Return True if the game is in session. """

        return self.status == STATUS_PLAYING


def play_game():
    """ Initiate gameplay. """

    playing = True

    while playing:
        word = get_word()
        UFO = Game(word)
        Game.start()
        Game.play(UFO, word)
        keep_playing = input('Would you like to play again (Y/N)? ').upper()
        while keep_playing == 'N':
            playing = False
            print('Goodbye!')
            break



if __name__ == '__main__':
    play_game()
