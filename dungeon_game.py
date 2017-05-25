import logging
import os
import random

logging.basicConfig(filename='game.log', level=logging.DEBUG)


CELLS =     [(0, 0), (1, 0), (2, 0), (3, 0), (4, 0),
		    (0, 1), (1, 1), (2, 1), (3, 1), (4, 1),
		    (0, 2), (1, 2), (2, 2), (3, 2), (4, 2),
		    (0, 3), (1, 3), (2, 3), (3, 3), (4, 3),
		    (0, 4), (1, 4), (2, 4), (3, 4), (4, 4)]

def clear_screen():
    #os.system('cls' if os.name=='nt' else 'clear')
    os.system('clear')

def get_locations():
    return random.sample(CELLS, 3)

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

def draw_map(player):
    print(" _" * 5)
    tile = "|{}"
    for cell in CELLS:
        x, y = cell
        if x < 4:
            line_end = ""
            if cell == player:
                output = tile.format('X')
            else:
                output = tile.format('_')
        else:
            line_end = "\n"
            if cell == player:
                output = tile.format("X|")
            else:
                output = tile.format('_|')
        print(output, end = line_end)

def game_loop():
    player, monster, door = get_locations()
    while True:
        clear_screen()
        unused=os.system("clear")
        draw_map(player)
        valid_moves = get_moves(player)
        print("You are currently in room {}".format(player))  # fill with player position
        print("You can move {}".format(", ".join(valid_moves)))  # fill with available moves
        print("Enter QUIT to quit.")
        # print("Door is at: {}".format(door))
        move = input("> ")
        move = move.upper()

        if move == 'QUIT':
            break
        # good move? change position
        if move in valid_moves:
            player = move_player(player, move)
        else:
            # bad move - reject & retry
            input("\n ** Walls are hard. Don't run into them! ** \n")
            # print("You can move {}".format(valid_moves))
        # on the door? Win!
        if player == door:
            clear_screen()
            print("\n ** You found the door and escaped!! ** \n")
            break
        if player == monster:
            clear_screen()
            print("\n ** You got eaten by the monster - GAME OVER! ** \n")
            break

clear_screen()
print("Welcome to the Dungeon!")
input("Press return to start ... ")
clear_screen()
game_loop()
