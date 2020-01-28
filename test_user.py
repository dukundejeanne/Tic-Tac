import unittest # Importing the unittest module
from tac_toe import TicTacToe # Importing the tictactoe  class

class TestTicTacToe(unittest.TestCase):

    '''
    Test class that defines test cases for the TicTacToe class behaviours.

    Args:
        unittest.TestCase: TestCase class that helps in creating test cases
    '''

       # Items up here .......

    def setUp(self):
        '''
        Set up method to run before each test cases.
        '''
        self.new_board = TicTacToe() # create contact object


    def test_init(self):
        '''
        test_init test case to test if the object is initialized properly
        '''

        self.assertEqual(self.new_board.position,1)
        # self.assertEqual(self.new_board.last_name,"Muriuki")
        # self.assertEqual(self.new_contact.phone_number,"0712345678")
        # self.assertEqual(self.new_contact.email,"james@ms.com")

    def test_save_board(self):
        '''
        test_save_contact test case to test if the contact object is saved into
         the contact list
        '''
        self.new_board.save() # saving the new contact
        # self.assertEqual(len(Contact.contact_list),1)
if __name__ == '__main__':
    unittest.main()