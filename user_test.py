import unittest # Importing the unittest module
# from tac_toe import TicTacToe # Importing the tictactoe  class

class TestTicTacToe(unittest.TestCase):

    '''
    Test class that defines test cases for the TicTacToe class behaviours.

    Args:
        unittest.TestCase: TestCase class that helps in creating test cases
    '''
     
    board="x"
    board="0"
    def setUp(self): 
        '''
        Set up method to run before each test cases.
        '''
        pass
    
       # Items up here .......
   
    def make_board(self):
        return Board()

    def test_handle_player(self):
        """
        Test that numbers between 0 and 5 are all even.
        """
        for i in range(0, 8):
            with self.subTest(i<i):
                self.assertEqual(i < 9, 1)

    def test_check_rows(self):
        player_1=[None,None,None]
        # self.assertEqual(self.player_1)
    
    def test_upper(self):         
        self.assertEqual('x'.upper(), 'X') 
  

  
    # Returns winne if the board contains 3 x. 
    def test_check_for_winner(self): 
        self.assertEqual( 'x'*3, 'xxx') 


    def test_check_tie(self):
        
        self.assertFalse(self.board.is_full())
 
if __name__ == '__main__':
    unittest.main()



#board
#print board
#play games
#handle players
#check Win
  #check rows
  #check column
  #check diagonis
#check tie
#flip player
