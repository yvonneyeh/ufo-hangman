import game
import unittest
from unittest import mock
from unittest.mock import patch
import io


class TestGame(unittest.TestCase):

    # # # Solution one: testing print with @patch
    # # @patch('sys.stdout', new_callable=io.StringIO)
    # # def test_foo_one(mock_stdout):
    # #     foo()
    # #     assert mock_stdout.getvalue() == 'Something\n'

    # # Solution one: testing print with @patch
    # @patch('sys.stdout', new_callable=io.StringIO)
    # def test_foo_one(mock_stdout):
    #     play.play('word')
    #     assert mock_stdout.getvalue() == 'Something\n'

    # def test_correct_guess():
    #     with mock.patch('sys.stdout') as fake_stdout:
    #         play.play('word')

    #     fake_stdout.assert_has_calls([
    #         mock.call.write('Something'),
    #         mock.call.write('\n')
    #     ])
 
    def test_game():
        input_values = ['a']
        output = []
    
        def mock_input(s):
            output.append(s)
            return input_values.pop(0)
        play.input = mock_input
        play.print = lambda s : output.append(s)
    
        play.play_game()
    
        assert output == [
            'Incorrect! The tractor beam pulls the person in further.',
        ]


    @patch('sys.stdout', return_value='o')
    def test_correct_letter(self, input):
        """
        Test for when user guesses a correct letter.
        """
        play.play('word')
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