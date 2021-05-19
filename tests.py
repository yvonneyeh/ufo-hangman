import game
from game import Game
import unittest
from unittest import mock, TestCase
from unittest.mock import patch
import io


class TestGame(TestCase):
    

    # def test_correct_letter(self, return_value='w'):
    #     """
    #     Test for when user guesses a correct letter.
    #     """
    #     UFO = Game('word')
    #     Game.play(UFO, 'word')
    #     result = Game.process_guess(UFO, return_value)
    #     self.assertEqual(result, game.CORRECT)


    # def test_incorrect_letter(self, input):
    #     """
    #     Test for when user guesses an incorrect letter.
    #     """
    #     UFO = Game('word')
    #     Game.play(UFO, 'word')
    #     self.assertIn(Game.play(UFO, 'word'), "Incorrect! The tractor beam pulls the person in further.")


    def test_6_lives(self):
        UFO = Game('word')
        self.assertEqual(UFO.lives, 6)


    # @mock.patch('game.input', return_value='a')
    # def test_guess_incorrect(self, mocked_input):
    #     # mocked_input.side_effect = 'a'
    #     UFO = Game('word')
    #     Game.play(UFO, 'word')
    #     result = Game.process_guess(UFO, return_value)
    #     self.assertIn(result, "Incorrect! The tractor beam pulls the person in further.")


    # @mock.patch('game.input', create=True)
    # def test_guess_correct(self, mocked_input):
    #     mocked_input.side_effect = 'o'
    #     UFO = Game('word')
    #     Game.play(UFO, 'word')
    #     result = Game.process_guess(UFO, mocked_input.side_effect)
    #     self.assertIn(result, "Correct! You're closer to cracking the codeword.")


    


# Game.play(UFO, 'word'), "Correct! You're closer to cracking the codeword."

# class TestGame(unittest.TestCase):

#     # # Solution one: testing print with @patch
#     # @patch('sys.stdout', new_callable=io.StringIO)
#     # def test_foo_one(mock_stdout):
#     #     foo()
#     #     assert mock_stdout.getvalue() == 'Something\n'

#     # @patch('sys.stdout', new_callable=io.StringIO)
#     # def test_bar_yes():
#     #     original_input = mock.builtins.input
#     #     mock.builtins.input = lambda _: "o"
#     #     self.assertEqual(bar(), "you entered yes")
#     #     mock.builtins.input = original_input
#     #     assert mock_stdout.getvalue() == "Correct! You're closer to cracking the codeword."


#     @patch('sys.stdout', return_value='o')
#     def test_correct_letter(self, input):
#         """
#         Test for when user guesses a correct letter.
#         """
#         UFO = Game('word')
#         Game.play(UFO, 'word')
#         self.assertIn(Game.play(UFO, 'word'), "Correct! You're closer to cracking the codeword.")


#     @patch('sys.stdout', return_value='a')
#     def test_incorrect_letter(self, input):
#         """
#         Test for when user guesses an incorrect letter.
#         """
#         UFO = Game('word')
#         Game.play(UFO, 'word')
#         self.assertIn(Game.play(UFO, 'word'), "Incorrect! The tractor beam pulls the person in further.")


#     # @patch('game.play_game()', return_value='N')
#     # def test_no_play_again(self, input):
#     #     """
#     #     Test for when user does not want to continue game.
#     #     """
#     #     self.assertEqual(game.play_game(), 'Goodbye!')


if __name__ == '__main__':
    unittest.main()