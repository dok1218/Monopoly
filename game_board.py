# this bit of code is intended to move a single player around a board game containing 40 unique possible positions,
# whilst also keeping a tally of how many times each unique position is landed on

# import modules needed for the code
import random

# define the number of games to play and how many dice throws each game should have, also defines the variable "board"
# which will be the list that stores the number of times each position is landed on
n_games = 1000
n_throws = 120
board = []

# create arrays to represent the Chance and Community chest cards and the corresponding positions they move to
Chance = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
Community_chest = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]

# function to deal with the chance positions
def chance_card(position_x):
    if position_x == 7 or 22 or 36:
        current_card = Chance[0]
        global position # makes sure that the variable "position" refers to the global variable
        if current_card == 0:
            position = 0
        elif current_card == 1:
            position = 24
        elif current_card == 2:
            position = 11
        elif current_card == 3:
            position = 13 # need to change this bit to deal with move to nearest utility
        elif current_card == 4:
            positon = 6 # need to change this bit to deal with move to nearest station
        elif current_card == 8:
            position = 10
        elif current_card == 11:
            position = 5
        elif current_card == 12:
            position = 39
        else:
            position = position
        Chance.append(Chance.pop(0)) # deletes the first item in the list and moves it to the end of the list

# function to deal with the community card poistions
def community_card(position_x):
    if position_x == 2 or 17 or 33:
        current_card = Community_chest[0]
        global position # makes sure that the variable "position" refers to the global variable
        if current_card == 0:
            position = 0
        elif current_card == 5:
            position = 10
        else:
            position = position
        Community_chest.append(Community_chest.pop(0)) # deletes the first item in the list and moves it to the end of the list

# define the list variable which will store information about how many times each position is landed on
for _ in range(0, 40):
    board.append(0)

# code to run the game
for _ in range(n_games):
    random.shuffle(Chance) # shuffles the Chance and Community chest cards
    random.shuffle(Community_chest)
    position = 0 # sets the starting position for the game
    for _ in range(n_throws):
        dice_sum = random.randint(1, 6) + random.randint(1, 6) # stores the sum of two random integers betweem 1 and 6
        if (position + dice_sum) <= 39:
            position = position + dice_sum # updates the new postion of the piece
            community_card(position) # checks if the new position is a community card and if so, draws and applies effect
            chance_card(position) # checks if the new position is a chance card and if so, draws and applies effect
            board[position] = board[position] + 1 # logs that the new position was landed on
        else: # deals with the case when piece has moved all the way around the board
            while position < 39:
                dice_sum = dice_sum - 1
                position = position + 1
            position = -1 # allows the piece to carry on from position 39 without exceeding the limit of 40 positions
            position = position + dice_sum
            community_card(position) # checks if the new position is a community card and if so, draws and applies effect
            chance_card(position) # checks if the new position is a chance card and if so, draws and applies effect
            board[position] = board[position] + 1
print(board) # just exists to check that nothing is very wrong with the code