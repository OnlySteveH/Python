# draw grid
# pick random location for player
# pick random location for door
# pick random location for monster
# draw player in the grid
# take input for movement
# move player unless beyond grid limits
# check for win/lose
# clear screen & redraw grid
import random
import os
first_run = True
CELLS =     [(0, 0), (1, 0), (2, 0), (3, 0), (4, 0),
		    (0, 1), (1, 1), (2, 1), (3, 1), (4, 1),
		    (0, 2), (1, 2), (2, 2), (3, 2), (4, 2),
		    (0, 3), (1, 3), (2, 3), (3, 3), (4, 3),
		    (0, 4), (1, 4), (2, 4), (3, 4), (4, 4)]

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def get_locations():
    return random.sample(CELLS, 3)

# def set_locations():
#     return random.sample(CELLS, 3)

def move_player(player, move):
    # get player location
    x, y = player
    if move == "LEFT":
        x -= 1
    # if move == RIGHT, x + 1
    if move == "RIGHT":
        x += 1
    # if move == UP, y + 1
    if move == "UP":
        y -= 1
    # if move == DOWN, y - 1
    if move == "DOWN":
        y += 1
    return x, y

def get_moves(player):
    moves = ["LEFT", "RIGHT", "UP", "DOWN"]
    # if player y == 0, can't move UP
    if player[1] == 0:
        moves.remove("UP")
    # if player y == 4, can't move DOWN
    if player[1] == 4:
        moves.remove("DOWN")
    # if player x == 0, can't move LEFT
    if player[0] == 0:
        moves.remove("LEFT")
    # if player x == 4, can't move RIGHT
    if player[0] == 4:
        moves.remove("RIGHT")
    return moves

player, monster, door = get_locations()

while True:
    valid_moves = get_moves(player)
    clear_screen()
    if first_run:
        print("Welcome to the Dungeon!")
    first_run = False
    print("You are currently in room {}".format(player))  # fill with player position
    print("You can move {}".format(", ".join(valid_moves)))  # fill with available moves
    print("Enter QUIT or Q to quit.")

    move = input("> ")
    move = move.upper()

    if move == 'QUIT':
        break
    # good move? change position
    if move in valid_moves:
        player = move_player(player, move)
    else:
        # bad move - reject & retry
        print("Walls are hard. Don't run into them!")
        # print("You can move {}".format(valid_moves))
    # on the door? Win!
    # on the monster? lose
    # else loop