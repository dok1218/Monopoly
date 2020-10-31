# this bit of code is intended to move a single player around a board game containing 40 unique possible positions,
# whilst also keeping a tally of how many times each unique position is landed on

# import the "random" module to allow the use of random number generator for the dice throws
import random

# define the number of games to play and how many dice throws each game should have, also defines the variable "board"
# which will be the list that stores the number of times each position is landed on
n_games = 10
n_throws = 120
board = []

# define the list variable which will store information about how many times each position is landed on
for _ in range(0, 40):
    board.append(0)

# code to run the game
for _ in range(n_games):
    position = 0 # sets the starting position for the game
    for _ in range(n_throws):
        dice_sum = random.randint(1, 6) + random.randint(1, 6) # stores the sum of two random integers betweem 1 and 6
        if (position + dice_sum) <= 39:
            position = position + dice_sum # updates the new postion of the piece
            board[position] = board[position] + 1 # logs that the new position was landed on
        else: # deals with the case when piece has moved all the way around the board
            while position < 39:
                dice_sum = dice_sum - 1
                position = position + 1
            position = 0 # moved around the board once so sets position back to starting position
            position = position + dice_sum
            board[position] = board[position] + 1

print(board) # need to find out how to record number of times position 0 is landed on exactly
