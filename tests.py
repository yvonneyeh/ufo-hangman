import game
from game import Game
import unittest
from unittest import mock, TestCase
from unittest.mock import patch
import io

UFO = Game('WORD')


class TestGame(TestCase):

    def test_guess_correct(self):
        """
        Test for when user guesses a correct letter.
        """
        guess = 'O'
        result = Game.process_guess(UFO, guess)
        self.assertEqual(result, game.STATUS_CORRECT)


    def test_guess_incorrect(self):
        """
        Test for when user guesses an incorrect letter.
        """
        guess = 'A'
        result = Game.process_guess(UFO, guess)
        self.assertEqual(result, game.STATUS_INCORRECT)


    def test_6_lives(self):
        """
        Test for 6 lives at start of game.
        """
        UFO = Game('word')
        self.assertEqual(UFO.lives, 6)


    # Test:
    #  - When it's their last guess and they guess wrong
    #  - When they guess the full word
    #  - When invalid character is entered
    #  - Showing remaining guesses / state of word
    #  - Ensure for incorrect letter that we increment attempts
    #  - Ensure for correct letter that we do not incrememnt attempts
    #  - Showing correct image

if __name__ == '__main__':
    unittest.main()