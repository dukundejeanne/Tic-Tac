from math import inf as infinity
from random import choice
import platform
import time
from os import system

HUMAN = -1
COMPUTER = +1
# Game board
board = [
    [0, 0, 0],
    [0, 0, 0],
    [0, 0, 0],
]

def evaluate(state):
    """
    Function to heuristic evaluation of state.
     the state of the current board
    return +1 if the computer wins; -1 if the human wins; 0 draw
    """
    if wins(state, COMPUTER):
        score = +1
    elif wins(state, HUMAN):
        score = -1
    else:
        score = 0

    return score


def wins(state, player):
    """
    This function tests if a specific player wins. Possibilities:
    * Three rows    [X X X] or [O O O]
    * Three cols    [X X X] or [O O O]
    * Two diagonals [X X X] or [O O O]
     the state of the current board
     a human or a computer
    return True if the player wins
    """
    win_state = [
        [state[0][0], state[0][1], state[0][2]],
        [state[1][0], state[1][1], state[1][2]],
        [state[2][0], state[2][1], state[2][2]],
        [state[0][0], state[1][0], state[2][0]],
        [state[0][1], state[1][1], state[2][1]],
        [state[0][2], state[1][2], state[2][2]],
        [state[0][0], state[1][1], state[2][2]],
        [state[2][0], state[1][1], state[0][2]],
    ]
    if [player, player, player] in win_state:
        return True
    else:
        return False


def game_over(state):
    """
    This function test if the human or computer winshe state of the current board
    return True if the human or computer wins
    """
    return wins(state, HUMAN) or wins(state, COMPUTER)


def empty_cells(state):
    """
    Each empty cell will be added into cells' list
     the state of the current board and return a list of empty cells
    """
    cells = []

    for x, row in enumerate(state):
        for y, cell in enumerate(row):
            if cell == 0: cells.append([x, y])
    return cells


def valid_move(x, y):
    """
    A move is valid if the chosen cell is empty
     X coordinate, Y coordinate,True if the board[x][y] is empty
    """
    if [x, y] in empty_cells(board):
        return True
    else:
        return False


def set_move(x, y, player):
    """
    Set the move on board, if the coordinates are valid
    X coordinate,Y coordinate,the current player
    """
    if valid_move(x, y):
        board[x][y] = player
        return True
    else:
        return False


def minimax(state, depth, player):
    """
    AI function that choice the best move, current state of the board
    node index in the tree (0 <= depth <= 9),
    but never nine in this case (see iaturn() function)
     an human or a computer and return a list with [the best row, best col, best score]
    """
    if player == COMPUTER:
        best = [-1, -1, -infinity]
    else:
        best = [-1, -1, +infinity]

    if depth == 0 or game_over(state):
        score = evaluate(state)
        return [-1, -1, score]

    for cell in empty_cells(state):
        x, y = cell[0], cell[1]
        state[x][y] = player
        score = minimax(state, depth - 1, -player)
        state[x][y] = 0
        score[0], score[1] = x, y

        if player == COMPUTER:
            if score[2] > best[2]:
                best = score  # max value
        else:
            if score[2] < best[2]:
                best = score  # min value

    return best


def clean():
    """
    Clears the console
    """
    os_name = platform.system().lower()
    if 'windows' in os_name:
        system('cls')
    else:
        system('clear')


def render(state, c_choice, h_choice):
    """
    Print the board 
    """
    print('----------------')
    for row in state:
        print('\n----------------')
        for cell in row:
            if cell == +1:
                print('|', c_choice, '|', end='')
            elif cell == -1:
                print('|', h_choice, '|', end='')
            else:
                print('|', ' ', '|', end='')
    print('\n----------------')


def ai_turn(c_choice, h_choice):
    """
    It calls the minimax function if the depth < 9,
    else it choices a random coordinate.
    computer's choice and human's choice X or O
    
    """
    depth = len(empty_cells(board))
    if depth == 0 or game_over(board):
        return

    clean()
    print('Computer turn [{}]'.format(c_choice))
    render(board, c_choice, h_choice)

    if depth == 9:
        x = choice([0, 1, 2])
        y = choice([0, 1, 2])
    else:
        move = minimax(board, depth, COMPUTER)
        x, y = move[0], move[1]

    set_move(x, y, COMPUTER)
    time.sleep(1)


def human_turn(c_choice, h_choice):
    """
    The Human plays choosing a valid move.between computer's choice X or O
     human's choice X or O
   
    """
    depth = len(empty_cells(board))
    if depth == 0 or game_over(board):
        return

    # Dictionary of valid moves
    move = -1
    moves = {
        1: [0, 0], 2: [0, 1], 3: [0, 2],
        4: [1, 0], 5: [1, 1], 6: [1, 2],
        7: [2, 0], 8: [2, 1], 9: [2, 2],
    }

    clean()
    print('Human turn [{}]'.format(h_choice))
    render(board, c_choice, h_choice)

    while (move < 1 or move > 9):
        try:
            move = int(input('Use numpad (1..9): '))
            coord = moves[move]
            try_move = set_move(coord[0], coord[1], HUMAN)

            if try_move == False:
                print('Bad move')
                move = -1
        except KeyboardInterrupt:
            print('Bye')
            exit()
        except:
            print('Bad choice')


def main():
    """
    Main function that calls all functions
    """
    clean()
    h_choice = '' # X or O
    c_choice = '' # X or O
    first = ''  # if human is the first

    # Human chooses X or O to play
    while h_choice != 'O' and h_choice != 'X':
        try:
            print('')
            h_choice = input('Choose X for your: ').upper()
        except KeyboardInterrupt:
            print('Bye')
            exit()
        except:
            print('Bad choice')

    # Setting computer's choice
    if h_choice == 'X':
        c_choice = 'O'
    else:
        c_choice = 'X'

    # Human may starts first
    clean()
    while first != 'Y' and first != 'N':
        try:
            first = input('First to start?[yes/no]: ').upper()
        except KeyboardInterrupt:
            print('Bye')
            exit()
        except:
            print('Bad choice')

    # Main loop of this game
    while len(empty_cells(board)) > 0 and not game_over(board):
        if first == 'N':
            ai_turn(c_choice, h_choice)
            first = ''

        human_turn(c_choice, h_choice)
        ai_turn(c_choice, h_choice)

    # Game over message
    if wins(board, HUMAN):
        clean()
        print('Human turn [{}]'.format(h_choice))
        render(board, c_choice, h_choice)
        print('YOU WIN!')
    elif wins(board, COMPUTER):
        clean()
        print('Computer turn [{}]'.format(c_choice))
        render(board, c_choice, h_choice)
        print('YOU LOSE!')
    else:
        clean()
        render(board, c_choice, h_choice)
        print('TIE!')

    exit()


if __name__ == '__main__':
    main()