import game
from game import Game
import unittest
from unittest import mock, TestCase
from unittest.mock import patch


class TestGame(TestCase):


    def test_guess_correct(self):
        """
        Test for when user guesses a correct letter.
        """
        guess = 'O'
        UFO = Game('WORD')
        result = Game.process_guess(UFO, guess)
        self.assertEqual(result, game.STATUS_CORRECT)


    def test_guess_incorrect(self):
        """
        Test for when user guesses an incorrect letter.
        """
        guess = 'A'
        UFO = Game('WORD')
        result = Game.process_guess(UFO, guess)
        self.assertEqual(result, game.STATUS_INCORRECT)


    def test_6_lives(self):
        """
        Test for 6 lives at start of game.
        """
        UFO = Game('word')
        self.assertEqual(UFO.lives, 6)


    def test_playing_game(self):
        """
        Test for in progress game.
        """

        UFO = Game('playing')
        letters = ['z','y','x','w','v','t','s','q']
        for i in range(len(letters)):
            result = UFO.process_guess(letters[i])

        self.assertEqual(UFO.get_status(), game.STATUS_PLAYING)


    def test_game_over(self):
        """
        Test for lost game.
        """

        UFO = Game('failure')
        UFO.lives = 0
        result = Game.check_status(UFO)

        self.assertEqual(result, game.STATUS_LOSE)


    def test_winning_guess(self):
        """
        Test for winning gameplay.
        """
        UFO = Game('WORD')
        UFO.guessed_letters = {'W', 'O', 'R'}
        UFO.word_letters = {'D'}
        guess = 'D'
        result = Game.process_guess(UFO, guess)
        self.assertEqual(result, game.STATUS_WIN)


    def test_guess_number(self):
        """
        Test for invalid character guess (integer).
        """
        guess = 0
        UFO = Game('WORD')
        result = Game.process_guess(UFO, guess)
        self.assertEqual(result, game.STATUS_INVALID)


    def test_invalid_letter(self):
        """
        Test for invalid double character guess.
        """
        guess = 'YY'
        UFO = Game('WORD')
        result = Game.process_guess(UFO, guess)
        self.assertEqual(result, game.STATUS_INVALID)


if __name__ == '__main__':
    unittest.main()