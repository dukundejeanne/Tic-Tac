#------Globol variables--------

#Game board

board=["-","-","-",
        "-","-","-",
        "-","-","-"]

#if game is still game_still_going
game_still_going=True

# who Winn
winner=None

##who turn is
current_player="x"

# class TicTacToe:
  
#   def __init__(self):

#     '''
#     __init__ method that helps us define properties for our objects.

#         Args:
#         board:takes new position
#         player:start with x tun end with 0 turn
    
#     '''
#     self.board=[None,None,None,
#                 None,None,None,
#                 None,None,None]
#     self.player=["x","0"]



def display_board():
  '''
  print the design board  display board 
  '''
  print (board[0] + " | " +board[1] + " | " + board[2])
  print (board[3] + " | " +board[4] + " | " + board[5])
  print (board[6] + " | " +board[7] + " | " + board[8])


def play_game():
  '''
  start playing game by display, and check if the player has win or tie.
  '''
  #display initial board
  display_board()

  #while the game is still going
  while game_still_going:

    #handle a single turn player of an arbitrary
    handle_turn(current_player)

    #check if game is over
    check_if_game_over()

    #flip to the other player
    flip_player()


  #the game has ended
  if winner == "x" or winner =="0":
    print(winner + " Congratulations you have winne!!!.")
    
  elif winner == None:
    print("Tie the board is full.")
  # print(winner "tie")

#handle a single turn player of an arbitrary 
def handle_turn(player):
  '''
  check if the player choose the valid position 
  '''

  print(player + " 's turn.")
  position = input("choose a position between 1-9:")

  valid = False
  while not valid:

    while position not in ["1","2","3","4","5","6","7","8","9"]:
      position = input("invalid input !!!! choose a position between 1-9:")
    position=int(position)-1

    if board[position] == "-":
      valid=True
    else:
      
      print("the positon is outside boards, Play again")

  board[position] = player
  display_board()


def check_if_game_over():
  '''
  function to check is the game is over
  '''
  check_for_winner()
  check_if_tie()

def check_for_winner():
  '''
  check the winner 
  '''

  #set up for global winner
  global winner
  #check rows
  row_winner=check_rows()
  #check columnns
  column_winner=check_columns()
  #check diagonis
  diagonal_winner=check_diagonals()


  
  if row_winner:
    winner=row_winner

  elif column_winner:
    winner=column_winner
    
  elif diagonal_winner:
    winner=diagonal_winner
  else:
    #there was no win
    winner=None

  return

def check_rows():
  '''
  chech the rows side if there is a winner
  '''
  #set up gloal variables
  global game_still_going

  #check if row has same values
  row_1 = board[0] == board[1] == board[2] !="-"
  row_2 = board[3] == board[4] == board[5] !="-"
  row_3 = board[6] == board[7] == board[8] !="-"

  # if any row does have a match, flag that there is a win
  if row_1 or row_2 or row_3:
    game_still_going= False
  # return the winner X or 0
    if row_1:
      return board[0]
    elif row_2:
      return board[3]
    elif row_3:
      return board[6]
  return

def check_columns():
  '''
  chech the columns side if there is a winner
  '''
    #set up gloal variables
  global game_still_going

  #check if column has same values
  column_1= board[0] == board[3] == board[6] !="-"
  column_2= board[1] == board[4] == board[7] !="-"
  column_3= board[2] == board[5] == board[8] !="-"

  # if any column does have a match, flag that there is a win
  if column_1 or column_2 or column_3:
    game_still_going= False
  # return the winner X or 0
    if column_1:
      return board[0]
    elif column_2:
      return board[1]
    elif column_3:
      return board[2]
  return

def check_diagonals():
  '''
  chech the diagonals side if there is a winner
  '''
  #set up gloal variables
  global game_still_going

  #check if diagonal has same values
  diagonal_1= board[0] == board[4] == board[8] !="-"
  diagonal_2= board[6] == board[4] == board[2] !="-"
  

  # if any diagonal does have a match, flag that there is a win
  if diagonal_1 or diagonal_2:
    game_still_going= False
  # return the winner X or 0
    if diagonal_1:
      return board[0]
    elif diagonal_2:
      return board[6]

  return

  
def check_if_tie():
  '''
  if the player has end to play
  '''
#global variables
  global game_still_going
  if "-" not in board:
    game_still_going=False
  return

def flip_player():
  '''
  if current player is x then change to 0 ,if current player is 0 change to x
  '''

  #global variables
  global current_player
  #if current player is x then change to 0 ,if current player is 0 change to x
  if current_player == "x":
    current_player = "0"
  elif current_player == "0":
    current_player = "x"
  return

play_game()





#board
#display board
#play games
#handle turn
#check Win
  #check rows
  #check column
  #check diagonis
#check tie
#flip player
