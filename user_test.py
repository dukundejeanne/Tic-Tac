import unittest # Importing the unittest module
# from tac_toe import TicTacToe # Importing the tictactoe  class

class TestTicTacToe(unittest.TestCase):

#     '''
#     Test class that defines test cases for the TicTacToe class behaviours.

#     Args:
#         unittest.TestCase: TestCase class that helps in creating test cases
#     '''

#        # Items up here .......

#     def setUp(self):
#         '''
#         Set up method to run before each test cases.
#         '''
#         self.new_board = TicTacToe() # create contact object


#     def test_init(self):
#         '''
#         test_init test case to test if the object is initialized properly
#         '''

#         self.assertEqual(self.new_board.position,1)
#         # self.assertEqual(self.new_board.last_name,"Muriuki")
#         # self.assertEqual(self.new_contact.phone_number,"0712345678")
#         # self.assertEqual(self.new_contact.email,"james@ms.com")

#     def test_save_board(self):
#         '''
#         test_save_contact test case to test if the contact object is saved into
#          the contact list
#         '''
#         self.new_board.save() # saving the new contact
#         # self.assertEqual(len(Contact.contact_list),1)
# class NumberTest(unittest.TestCase):
    player_1="x"
    player_2="0"
    def setUp(self): 
        pass
    
    def make_board(self):
        return Board()

    def test_even(self):
        """
        Test that numbers between 0 and 5 are all even.
        """
        for i in range(0, 8):
            with self.subTest(i<i):
                self.assertEqual(i < 9, 1)

    def test_check_rows(self):
        player_1=[board[0],board[3],board[6]]
        # self.assertEqual(self.game_still_going)


  
    # Returns winne if the board contains 3 x. 
    def test_check_for_winner(self): 
        self.assertEqual( 'x'*3, 'xxx') 

    def test_tie(self):
        assert(self.board.is_full())
    # def test_startgrid_is_empty_and_not_full(self):
    #     assert(self.grid.is_empty())
    #     self.assertFalse(self.grid.is_full())
    # def test_not_empty_and_not_full_after_play_center(self):
    #     assert(self.grid.play('center'))
    #     assert(not self.grid.is_empty())
  
    # Returns True if the string is in upper case. 
    def test_upper(self):         
        self.assertEqual('foo'.upper(), 'FOO') 
  
    # # Returns TRUE if the string is in uppercase 
    # # else returns False. 
    # def test_isupper(self):         
    #     self.assertTrue('FOO'.isupper()) 
    #     self.assertFalse('Foo'.isupper()) 
  
    # # Returns true if the string is stripped and  
    # # matches the given output. 
    # def test_strip(self):         
    #     s = 'geeksforgeeks'
    #     self.assertEqual(s.strip('geek'), 'sforgeeks') 
  
    # # Returns true if the string splits and matches 
    # # the given output. 
    # def test_split(self):         
    #     s = 'hello world'
    #     self.assertEqual(s.split(), ['hello', 'world']) 
    #     with self.assertRaises(TypeError): 
            # s.split(2) 
if __name__ == '__main__':
    unittest.main()