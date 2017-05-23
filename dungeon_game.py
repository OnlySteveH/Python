# draw grid
# pick random location for player
# pick random location for door
# pick random location for monster
# draw player in the grid
# take input for movement
# move player unless beyond grid limits
# check for win/lose
# clear screen & redraw grid

CELLS = [(0, 0), (1, 0), (2, 0), (3, 0), (4, 0),
		 (0, 1), (1, 1), (2, 1), (3, 1), (4, 1),
		 (0, 2), (1, 2), (2, 2), (3, 2), (4, 2),
		 (0, 3), (1, 3), (2, 3), (3, 3), (4, 3),
		 (0, 4), (1, 4), (2, 4), (3, 4), (4, 4)]

def get_locations():
	monster = None
	door = None
	player = None
	return monster, door, player

def move_player(player, move):
    # get player location
    # if move == LEFT, x - 1
    # if move == RIGHT, x + 1
    # if move == UP, y + 1
    # if move == DOWN, y - 1
    return player

def get_moves(player):
    moves = ["LEFT", "RIGHT", "UP", "DOWN"]
    # if player y == 0, can't move UP
    # if player y == 4, can't move DOWN
    # if player x == 0, can't move LEFT
    # if player x == 4, can't move RIGHT
    return moves

while True:
	print("Welcome to the Dungeon!")
	print("You are currently in room {}") # fill with player position
	print("You can move {}") # fill with available moves
	print("Enter QUIT to quit.")

    move = input("> ")
    move = move.upper()

    if move == 'QUIT':
        break

    # good move? change position

    # bad move? don't move
    # on the door? Win!
    # on the monster? lose
    # else loop