# this bit of code is intended to move a single player around a board game containing 40 unique possible positions,
# whilst also keeping a tally of how many times each unique position is landed on

# import the "random" module to allow the use of random number generator for the dice throws
import random

# define the number of games to play and how many dice throws each game should have, also defines the variable "board"
# which will be the list that stores the number of times each position is landed on
n_games = 1000
n_throws = 120
board = []

# create lists to represent the Chance and Community chest cards
Chance = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
Community_chest = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]

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
            position = -1 # allows the piece to carry on from position 39 without exceeding the limit of 40 positions
            position = position + dice_sum
            board[position] = board[position] + 1
