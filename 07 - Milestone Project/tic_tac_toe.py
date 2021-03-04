# write a function that can print out a board. Set up the board as a list where each index 1-9 corresponds with a
# number on a number pad
from IPython.display import clear_output


def display_board(board):
    # clear output will clear our table each time we run the function
    clear_output()
    print(board[7] + ' | ' + board[8] + ' | ' + board[9])
    print(board[4] + ' | ' + board[5] + ' | ' + board[6])
    print(board[1] + ' | ' + board[2] + ' | ' + board[3])


test_board = ['#', 'X', 'O', 'X', 'O', 'X', 'O', 'X', 'O', 'X', ]
# display_board(test_board)


#  Write a function taht can take a player input and assign their marker X or O.
def player_input():
    '''
    OUTPUT = (Plqyer 1 mqrker, Plqyer 2 marker)
    '''
    marker = ''
    while marker != 'X' and marker != 'O':
        marker = input('Player1: Choose X or O: ').upper()
    if marker == 'X':
        return ('X', 'O')
    else:
        return ('O', 'X')


# player1_marker, player2_marker = player_input()


# Write a function that takes in the board list object, a marker X or O and a desired position (1-9) and assigns it
# to the board
def place_marker(board, marker, position):
    board[position] = marker


# place_marker(test_board, '$', 8)
# display_board(test_board)


# Write a function that takes in a board and a mark X or O and checks to see if that mark has won
def win_check(board, mark):
    #  all rows, columns, and diagonals and check to see if they have the same marker
    return ((board[7] == board[8] == board[9] == mark) or
            (board[4] == board[5] == board[6] == mark) or
            (board[7] == board[8] == board[9] == mark) or
            (board[7] == board[4] == board[1] == mark) or
            (board[8] == board[5] == board[2] == mark) or
            (board[9] == board[6] == board[3] == mark) or
            (board[7] == board[5] == board[3] == mark) or
            (board[9] == board[5] == board[1] == mark))

    #  win tic tac toe


display_board(test_board)
print(win_check(test_board, 'X'))
