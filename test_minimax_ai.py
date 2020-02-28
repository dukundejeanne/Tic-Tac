from tic_tac_toe import TicTacToe
from minimax_ai import MinimaxAI
import numpy as np
import unittest # Importing the unittest module

class TestMinimaxAI(unittest.TestCase):

    '''
    Test class that defines test cases for the MinimaxAI class behaviours.

    Args:
        unittest.TestCase: TestCase class that helps in creating test cases
    '''
    def setUp(self):
        '''
        Set up method to run before each test cases.
        '''
        pass

    def test_init(self):
        '''
        test_init test case to test if the object is initialized properly
        '''
        pass
    def test_makes_valid_turns(self):
        game = TicTacToe()
        ai = MinimaxAI(game)

        row, column = ai.decide_turn()

        assert 0 <= row <= 2
        assert 0 <= column <= 2


    def test_terminates(self):
        game = TicTacToe()
        game.board[:] = 1
        game.board[0, 0] = 0

        ai = MinimaxAI(game)

        row, column = ai.decide_turn()



    def test_chooses_winning_move(self):
        game = TicTacToe()
        game.x_next = True
        game.board = np.array([ [   -1,  1,  0],
                                [    1,  1, -1],
                                [   -1,  0,  1]  ])

        ai = MinimaxAI(game)

        row, column = ai.decide_turn()

        assert (row, column) == (2,1)


    def test_chooses_blocking_move(self):
        game = TicTacToe()
        game.x_next = False
        game.board = np.array([ [   -1,  1,  0],
                                [    1,  1, -1],
                                [   -1,  0,  1]  ])

        ai = MinimaxAI(game)

        row, column = ai.decide_turn()

        assert (row, column) == (2,1)

if __name__ == '__main__':
    unittest.main()