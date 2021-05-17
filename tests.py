import play
import unittest
# from unittest import TestCase
from unittest.mock import patch


class TestGame(unittest.TestCase):


    @patch('play.play(word)', return_value='o')
    def test_correct_letter(self, input):
        """
        Test for when user guesses a correct letter.
        """
        self.assertIn(play.play('word'), "Correct! You're closer to cracking the codeword.")


    @patch('play.play(word)', return_value='a')
    def test_incorrect_letter(self, input):
        """
        Test for when user guesses an incorrect letter.
        """
        self.assertIn(play.play('word'), "Incorrect! The tractor beam pulls the person in further.")


    @patch('play.play_game()', return_value='N')
    def test_no_play_again(self, input):
        """
        Test for when user does not want to continue game.
        """
        self.assertEqual(play.play_game(), 'Goodbye!')


if __name__ == '__main__':
    unittest.main()