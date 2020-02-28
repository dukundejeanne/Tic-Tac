from tic_tac_toe import TicTacToe
from random_ai import RandomAI
import unittest # Importing the unittest module

class TestRandom(unittest.TestCase):

    '''
    Test class that defines test cases for the random class behaviours.

    Args:
        unittest.TestCase: TestCase class that helps in creating test cases
    '''
    def test_init(self):
        '''
        test_init test case to test if the object is initialized properly
        '''
        pass
     

    def test_makes_valid_turns(self):
        game = TicTacToe()

        game.o_ai = RandomAI(game)

        row, column = game.o_ai.decide_turn()

        assert 0 <= row <= 2
        assert 0 <= column <= 2



if __name__ == '__main__':
    unittest.main()