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

#  write a function that uses the random module to decide which player goest first

import random


def choose_first():
    flip = random.randint(0, 1)

    if flip == 0:
        return 'Player 1'
    else:
        return 'Player 2'


#  write a function that returns a boolean indicating weather a space on the board is available
def space_check(board, position):
    return board[position] == ' '


#  write a function that checks if the board is full and returns boolean value. True full, False otherwise
def full_board_check(board):
    for i in range(1, 10):
        if space_check(board, i):
            return False

    # Return True when board is full
    return True


#  write a function that asks for a player next position(1-9) and then use the fuunction space_check()) to check if it s a free position
def player_choice(board):
    position = 0

    while position not in [1, 2, 3, 4, 5, 6, 7, 8, 9] or not space_check(board, position):
        position = int(input('Choose a position: (1-9)'))

    return position


# Write a function that asks the player if they want to play again and return a boolean
def replay():
    choice = input('Play again? enter Y or N')
    return choice == 'Yes'


#  loops over previous functions and run the game

# WHILE loop to keep running the game
print('Welcome to Tic Tac Toe')
while True:
    # Play the game

    # Set everything up(board, who's first, choose markers etc)
    the_board = [' '] * 10
    player1_marker, player2_marker = player_input()

    turn = choose_first()
    print(turn + ' will go first')

    play_game = input('Ready to play? y or n? ')

    if play_game == 'y':
        game_on = True
    else:
        game_on = False

    #  Game play
    while game_on:
        #  Player 1 turn
        if turn == 'Player 1':
            # Show the board
            display_board(the_board)
            # Choose a position
            position = player_choice(the_board)
            # Place the marker on the position
            place_marker(the_board, player1_marker, position)
            # Check if they won
            if win_check(the_board, player1_marker):
                display_board(the_board)
                print('Player 1 has won !')
                game_on = False
            # No tie and no win? Next player's turn
            else:
                # Check if the board is full
                if full_board_check(the_board):
                    display_board(the_board)
                    print('It is a tie game')
                    break
                else:
                    turn = 'Player 2'
        else:
            # Player 2 turn
            # Show the board
            display_board(the_board)
            # Choose a position
            position = player_choice(the_board)
            # Place the marker on the position
            place_marker(the_board, player2_marker, position)
            # Check if they won
            if win_check(the_board, player1_marker):
                display_board(the_board)
                print('Player 2 has won !')
                game_on = False
            # No tie and no win? Next player's turn
            else:
                # Check if the board is full
                if full_board_check(the_board):
                    display_board(the_board)
                    print('It is a tie game')
                    break
                else:
                    turn = 'Player 1'

    if not replay():
        break
# Break out of the while loop on replay()
