import play
import unittest
# from unittest import TestCase
from unittest.mock import patch


class TestGame(unittest.TestCase):

    def test_correct_letter(self):
        """
        Test for when user guesses a correct letter.
        """
        self.assertIn("Correct! You're closer to cracking the codeword.")

    def test_incorrect_letter(self):
        """
        Test for when user guesses an incorrect letter.
        """
        self.assertIn("Incorrect! The tractor beam pulls the person in further.")


if __name__ == '__main__':
    unittest.main()