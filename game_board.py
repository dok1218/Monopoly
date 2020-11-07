# this bit of code is intended to move a single player around a board game containing 40 unique possible positions,
# whilst also keeping a tally of how many times each unique position is landed on

# import modules needed for the code
import random
import numpy as np
# import openpyxl # currentyly there is a windows bug preventing openpyxl module from working

# define the number of games to play and how many dice throws each game should have, also defines the variable "board"
# which will be the list that stores the number of times each position is landed on, variables "house", "hotel" and "streets"
# govern which set of streets you will own and the program will calculate financial outcome based on this
n_games = 100
n_throws = 120
board = []
house = 0
hotel = 0
streets = [11, 13, 14]
rent_amount = []
total_hits = 0
percentage_hits = []

# create list which will store the total money earnt from rent on selected owned properties
for _ in range(0, 40):
    rent_amount.append(0)

# create lists to represent the Chance and Community chest cards and the corresponding positions they move to
Chance = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
Community_chest = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]

# create array to store rent amounts 0 = base rent, 1 = 1 house, 2 = 2 houses, 3 = 3 houses, 4 = 4houses, 5 = hotel
rent = np.array([[0, 2, 0, 4, 0, 0, 6, 0, 6, 8, 0, 10, 0, 10, 12, 0, 14, 0, 14, 16, 0, 18, 0, 18, 20, 0, 22, 22, 0, 22, 0, 26, 26, 0, 28, 0, 0, 35, 0, 50],
                 [0, 10, 0, 20, 0, 0, 30, 0, 30, 40, 0, 50, 0, 50, 60, 0, 70, 0, 70, 80, 0, 90, 0, 90, 100, 0, 110, 110, 0, 120, 0, 130, 130, 0, 150, 0, 0, 175, 0, 200],
                 [0, 30, 0, 60, 0, 0, 90, 0, 90, 100, 0, 150, 0, 150, 180, 0, 200, 0, 200, 220, 0, 250, 0, 250, 300, 0, 330, 330, 0, 360, 0, 390, 390, 0, 450, 0, 0, 500, 0, 600],
                 [0, 90, 0, 180, 0, 0, 270, 0, 270, 300, 0, 450, 0, 450, 500, 0, 550, 0, 550, 600, 0, 700, 0, 700, 750, 0, 800, 800, 0, 850, 0, 900, 900, 0, 1000, 0, 0, 1100, 0, 1400],
                 [0, 160, 0, 320, 0, 0, 400, 0, 400, 450, 0, 625, 0, 625, 700, 0, 750, 0, 750, 800, 0, 875, 0, 875, 925, 0, 975, 975, 0, 1025, 0, 1100, 1100, 0, 1200, 0, 0, 1300, 0, 1700],
                 [0, 250, 0, 450, 0, 0, 550, 0, 550, 600, 0, 750, 0, 750, 900, 0, 950, 0, 950, 1000, 0, 1050, 0, 1050, 1100, 0, 1150, 1150, 0, 1200, 0, 1275, 1275, 0, 1400, 0, 0, 1500, 0, 2000]])

# creates list to store percentage hits
for _ in range(0, 40):
    percentage_hits.append(0)

# function to deal with moving to the nearest station card
def nearest_station(position_x):
    global position
    if position_x == 7:
        position = 15
    elif position_x == 22:
        position = 25
    elif position_x == 36:
        position = 5

# function to deal with moving to the nearest utility card
def nearest_utility(position_x):
    global position
    if position_x == 7:
        position = 12
    elif position_x == 22:
        position = 28
    elif position_x == 36:
        position = 12

# function to deal with the chance positions
def chance_card(position_x):
    if (position_x == 7) or (position_x == 22) or (position_x == 36):
        current_card = Chance[0]
        global position # makes sure that the variable "position" refers to the global variable
        if current_card == 0:
            position = 0
        elif current_card == 1:
            position = 24
        elif current_card == 2:
            position = 11
        elif current_card == 3:
            nearest_utility(position_x)
        elif current_card == 4:
            nearest_station(position_x)
        elif current_card == 7:
            position = position - 3
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
    if (position_x == 2) or (position_x == 17) or (position_x == 33):
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

file_name = ["base_rent.txt", "1_house.txt", "2_houses.txt", "3_houses.txt", "4_houses.txt", "hotel.txt"]

# code to run the game
for i in range(0, 5):
    for _ in range(n_games):
        random.shuffle(Chance)  # shuffles the Chance and Community chest cards
        random.shuffle(Community_chest)
        position = 0  # sets the starting position for the game
        for _ in range(n_throws):
            dice_sum = random.randint(1, 6) + random.randint(1,6)  # stores the sum of two random integers betweem 1 and 6
            if (position + dice_sum) <= 39:
                if (position + dice_sum) == 30:  # scenario where "go to jail" is landed on
                    position = 11
                else:
                    position = position + dice_sum  # updates the new postion of the piece
                    community_card(position)  # checks if the new position is a community card and if so, draws and applies effect
                    chance_card(position)  # checks if the new position is a chance card and if so, draws and applies effect
                board[position] = board[position] + 1  # logs that the new position was landed on
                rent_amount[position] = rent_amount[position] + rent[i, position]  # logs the amount of rent incurred from landing on the position
            elif (position + dice_sum) > 39:  # deals with the case when piece has moved all the way around the board
                position = position + dice_sum - 40  # resets the board
                community_card(position)  # checks if the new position is a community card and if so, draws and applies effect
                chance_card(position)  # checks if the new position is a chance card and if so, draws and applies effect
                board[position] = board[position] + 1
                rent_amount[position] = rent_amount[position] + rent[i, position]  # logs the amount of rent incurred from landing on the position

    # calculate the percentage of total positions landed on each street constitutes
    for x in range(len(board)):
        total_hits = total_hits + board[x]
    for y in range(len(percentage_hits)):
        percentage_hits[y] = 100 * (board[y] / total_hits)

    # store results in a text file
    f = open(file_name[i], "w")  # creates a text file
    f.close()  # closes the newly created text file
    with open(file_name[i], "w") as f:
        f.write("Percentage hits:")
        f.write("\n")
        f.write("\n")
        f.write("\n".join(str(w) for w in percentage_hits))
        f.write("\n")
        f.write("\n")
        f.write("Rent amounts:")
        f.write("\n")
        f.write("\n")
        f.write("\n".join(str(w) for w in rent_amount))

    # set all variables to 0 for the next iteration of the code (total_hits, board, rent_amount, percentage_hits)
    total_hits = 0
    for z in range(len(board)):
        board[z] = 0
    for a in range(len(rent_amount)):
        rent_amount[a] = 0
    for b in range(len(percentage_hits)):
        percentage_hits[b] = 0
