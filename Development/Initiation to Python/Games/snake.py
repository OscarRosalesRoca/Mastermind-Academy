import os
import readchar
from random import randint

#Constants
POS_X = 0
POS_Y = 1
NUM_MAP_OBJECTS = 5
GAME_NAME = "SNAKE GAME"
MAP_WIDTH = 20
MAP_HEIGHT = 15

#Snake
my_position = [randint(0, MAP_WIDTH - 1), randint(0, MAP_HEIGHT- 1)]
tail_length = 0
tail = []
score = 0

#Snake's food
map_objects = []

game_over = False

while not game_over:
    os.system("cls")

    #Creation of 10 random position objects
    if len(map_objects) < NUM_MAP_OBJECTS:
        while len(map_objects) < NUM_MAP_OBJECTS:
            create_object = [randint(0, MAP_WIDTH - 1), randint(0, MAP_HEIGHT - 1)]
            if create_object not in map_objects and create_object != my_position:
                map_objects.append(create_object)

    #Print TITLE GAME
    print("+" + "-" * (MAP_WIDTH * 3) + "+")

    total_width = MAP_WIDTH * 3
    title_length = len(GAME_NAME) + 2 #Add two blank spaces
    side_dashes = (total_width - title_length) // 2

    len_to_print = "|" + " " * side_dashes + " " + GAME_NAME + " " + " " * (total_width - title_length - side_dashes) + "|"

    print(len_to_print)
    print("+" + "-" * (MAP_WIDTH * 3) + "+")

    #Draw MAP
    for coordinate_y in range(MAP_HEIGHT):
        print("|", end="")
        for coordinate_x in range(MAP_WIDTH):
            char_to_draw = "   "
            object_in_cell = None

            #Draw objects
            for map_object in map_objects:
                if coordinate_x == map_object[POS_X] and coordinate_y == map_object[POS_Y]:
                    char_to_draw = " * "
                    object_in_cell = map_object

            #Draw snake
            if coordinate_x == my_position[POS_X] and coordinate_y == my_position[POS_Y]:
                char_to_draw = " @ "
                #Snake eat
                if object_in_cell:
                    map_objects.remove(object_in_cell)
                    tail_length += 1
                    score += 10

            #Draw tail
            for tail_piece in tail:
                if coordinate_x == tail_piece[POS_X] and coordinate_y == tail_piece[POS_Y]:
                    char_to_draw = " @ "

            print("{}".format(char_to_draw), end="")
        print("|")
    print("+" + "-" * MAP_WIDTH * 3 + "+")
    print("[Type WASD to move]")
    print("[Type Q to exit]")
    if not game_over:
        print("SCORE: {}".format(score))


    # Movement
    direction = readchar.readchar()
    new_position = my_position.copy()

    if direction == "w":
        new_position = [my_position[POS_X], (my_position[POS_Y] - 1) % MAP_HEIGHT]  # Mover hacia arriba

    elif direction == "s":
        new_position = [my_position[POS_X], (my_position[POS_Y] + 1) % MAP_HEIGHT]  # Mover hacia abajo

    elif direction == "a":
        new_position = [(my_position[POS_X] - 1) % MAP_WIDTH, my_position[POS_Y]]  # Mover hacia izquierda

    elif direction == "d":
        new_position = [(my_position[POS_X] + 1) % MAP_WIDTH, my_position[POS_Y]]  # Mover hacia derecha

    elif direction == "q":
        print("Exit...")
        break

    if len(tail) > 0 and new_position == tail[0]:
        print("You can't go backwards")
        print("Press any key to continue...")
        readchar.readchar()
        continue

    if len(tail) > 1 and new_position in tail[2:]:
        game_over = True
        print("YOU LOSE")
        break  # Termina el juego

    tail.insert(0, my_position.copy())
    tail = tail[:tail_length]
    my_position = new_position