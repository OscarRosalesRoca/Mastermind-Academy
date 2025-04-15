import os
import readchar
from random import randint

#Constants
POS_X = 0
POS_Y = 1
GAME_NAME = "POKEMON GAME"

#Create  map
obstacle_definition = """\
####   ######  ######
#####           ### #
##           ###### #
########            #
###          ########\
"""

obstacle_definition = [list(row) for row in obstacle_definition.split("\n")]
MAP_WIDTH = len(obstacle_definition[0])
MAP_HEIGHT = len(obstacle_definition)


#Trainers info
"""
0: Trainer's name
1: Pokemon's name
2: Pokemon's health
3: Pokemon attack
4: Damage points
5: Pokemon attack
6: Damage points
(...)
"""

# Trainers info (Modified to store full info)
TRAINERS = [
    {"name": "Rodolfo", "pokemon": {"name": "Pikipek", "health": 35, "attacks": [
        {"name": "Peak", "damage": 7},
        {"name": "Hyper Voice", "damage": 9},
        {"name": "Feather Dance", "damage": 10}
    ]}},
    {"name": "Astri", "pokemon": {"name": "Bonsly", "health": 50, "attacks": [
        {"name": "Fake Tears", "damage": 9},
        {"name": "Rock Tomb", "damage": 12}
    ]}},
    {"name": "Marcos", "pokemon": {"name": "Ledian", "health": 55, "attacks": [
        {"name": "Tackle", "damage": 10},
        {"name": "Struggle Bug", "damage": 11}
    ]}}
]
NUM_POKEMON_TRAINERS = len(TRAINERS)


#User
my_position = [randint(0, MAP_WIDTH - 1), randint(0, MAP_HEIGHT- 1)]
while obstacle_definition[my_position[POS_Y]][my_position[POS_X]] == "#":
        my_position = [randint(0, MAP_WIDTH - 1), randint(0, MAP_HEIGHT- 1)]

os.system("cls")
user_name = input("Type your user name: ")
USER = {"name": user_name, "pokemon": {"name": "Pikachu", "health": 70, "attacks": [
    {"name": "Iron Tail", "damage": 13},
    {"name": "Spark", "damage": 8},
    {"name": "Thunder", "damage": 15}
]}}
os.system("cls")

#Welcome
print("Welcome {}".format(user_name))
input("Press enter to start the game...")


# Create random positions for Pokémon trainers
pokemon_trainers = []
for trainer_info in TRAINERS:
    while True:
        create_trainer = [randint(0, MAP_WIDTH - 1), randint(0, MAP_HEIGHT - 1)]
        if (obstacle_definition[create_trainer[POS_Y]][create_trainer[POS_X]] != "#" and
                create_trainer not in [t["position"] for t in pokemon_trainers] and
                create_trainer != my_position):
            pokemon_trainers.append({"position": create_trainer, **trainer_info})
            break


game_over = False

while not game_over:
    os.system("cls")

    #Print TITLE GAME
    print("+" + "-" * (MAP_WIDTH * 3) + "+")
    total_width = MAP_WIDTH * 3
    title_length = len(GAME_NAME) + 2 #Add two blank spaces
    side_dashes = (total_width - title_length) // 2
    len_to_print = "|" + " " * side_dashes + " " + GAME_NAME + " " + " " * (total_width - title_length - side_dashes) + "|"
    print(len_to_print)
    print("+" + "-" * (MAP_WIDTH * 3) + "+")

    #Draw MAP
    trainer_in_cell = None
    for coordinate_y in range(MAP_HEIGHT):
        print("|", end="")
        for coordinate_x in range(MAP_WIDTH):
            char_to_draw = "   "

            # Draw pokemon trainers
            for trainer in pokemon_trainers:
                if coordinate_x == trainer["position"][POS_X] and coordinate_y == trainer["position"][POS_Y]:
                    char_to_draw = " * "
                    if my_position == trainer["position"]:
                        trainer_in_cell = trainer

            #Draw USER
            if coordinate_x == my_position[POS_X] and coordinate_y == my_position[POS_Y]:
                char_to_draw = " @ "

            #Draw walls
            if obstacle_definition[coordinate_y][coordinate_x] == "#":
                char_to_draw = "###"

            print("{}".format(char_to_draw), end="")
        print("|")
    print("+" + "-" * MAP_WIDTH * 3 + "+")

    #Info
    print("[Controls: Use WASD to move and Q to exit]")
    print("\nWelcome to my Pokemon Game!\n"
          "You are '@', and your mission is not to catch them all, no.\n"
          "You're here to defeat all the other trainers, each with a unique Pokémon,\n"
          "alongside your companion, Pikachu! Good luck!")
    print("\n[CURRENT MISSION: Defeat all the trainers. Pikachu will fully recover his HP after each victory.]")

    # Start Pokemon battle
    if trainer_in_cell:
        print("\nYou have found a trainer! Name: {}, Pokémon: {}.".format(
            trainer_in_cell["name"], trainer_in_cell["pokemon"]["name"]))
        print("Win this battle or lose it all.")
        input("Press enter to start the battle...")

        os.system("cls")

        #Battle start
        SIZE_HEALTH_BAR = 20
        MAX_HEALTH_USER_POKEMON = USER["pokemon"]["health"]
        MAX_HEALTH_TRAINER_POKEMON = trainer_in_cell["pokemon"]["health"]
        health_user_pokemon = MAX_HEALTH_USER_POKEMON
        health_trainer_pokemon = MAX_HEALTH_TRAINER_POKEMON

        # Begging of the combat
        title = "THE COMBAT BETWEEN {} AND {} HAS STARTED".format(
            USER["pokemon"]["name"], trainer_in_cell["pokemon"]["name"])
        print(title + "\n" + "-" * len(title) + "\n")

        percentage_health_user_pokemon = int((health_user_pokemon * SIZE_HEALTH_BAR) / MAX_HEALTH_USER_POKEMON)
        print("{} HP: [{}{}] {}HP".format(USER["pokemon"]["name"], "*" * percentage_health_user_pokemon,
                                               " " * (SIZE_HEALTH_BAR - percentage_health_user_pokemon), health_user_pokemon))
        percentage_health_trainer_pokemon = int((health_trainer_pokemon * SIZE_HEALTH_BAR) / MAX_HEALTH_TRAINER_POKEMON)
        print("{} HP: [{}{}] {}HP".format(trainer_in_cell["pokemon"]["name"], "*" * percentage_health_trainer_pokemon,
                                               " " * (SIZE_HEALTH_BAR - percentage_health_trainer_pokemon), health_trainer_pokemon))
        input("Press enter to begin...")
        os.system("cls")

        while health_user_pokemon > 0 and health_trainer_pokemon > 0:

            # Turno del Entrenador Oponente
            print("{}'s turn!".format(trainer_in_cell["pokemon"]["name"]))

            # Seleccionar un ataque aleatorio del entrenador
            opponent_attacks = trainer_in_cell["pokemon"]["attacks"]
            rand_attack = randint(0, len(opponent_attacks) - 1)
            attack_name = opponent_attacks[rand_attack]["name"]
            attack_damage = opponent_attacks[rand_attack]["damage"]

            print("\n{} used {}... {} lost {}HP".format(trainer_in_cell["pokemon"]["name"], attack_name,
                                                      USER["pokemon"]["name"], attack_damage))
            health_user_pokemon -= attack_damage

            # Evitar valores negativos
            health_user_pokemon = max(0, health_user_pokemon)

            # Mostrar las barras de vida
            percentage_health_user_pokemon = int((health_user_pokemon * SIZE_HEALTH_BAR) / MAX_HEALTH_USER_POKEMON)
            print("{} HP: [{}{}] {}HP".format(USER["pokemon"]["name"], "*" * percentage_health_user_pokemon,
                                              " " * (SIZE_HEALTH_BAR - percentage_health_user_pokemon),
                                              health_user_pokemon))
            percentage_health_trainer_pokemon = int(
                (health_trainer_pokemon * SIZE_HEALTH_BAR) / MAX_HEALTH_TRAINER_POKEMON)
            print(
                "{} HP: [{}{}] {}HP".format(trainer_in_cell["pokemon"]["name"], "*" * percentage_health_trainer_pokemon,
                                            " " * (SIZE_HEALTH_BAR - percentage_health_trainer_pokemon),
                                            health_trainer_pokemon))

            input("Press enter to continue...")
            os.system("cls")

            # Turno del Usuario
            print("{}'s turn!".format(USER["pokemon"]["name"]))

            # Mostrar ataques del usuario
            user_attacks = USER["pokemon"]["attacks"]
            print("\nChoose an attack:")
            for i, attack in enumerate(user_attacks):
                print("({}) {} - {} damage".format(i + 1, attack["name"], attack["damage"]))

            # Obtener entrada del usuario
            option = None
            while option not in range(1, len(user_attacks) + 1):
                try:
                    option = int(input("Select an attack (1-{}): ".format(len(user_attacks))))
                except ValueError:
                    continue

            # Aplicar daño
            selected_attack = user_attacks[option - 1]
            print("\n{} used {}... {} lost {}HP".format(USER["pokemon"]["name"], selected_attack["name"],
                                                      trainer_in_cell["pokemon"]["name"], selected_attack["damage"]))
            health_trainer_pokemon -= selected_attack["damage"]

            # Evitar valores negativos
            health_trainer_pokemon = max(0, health_trainer_pokemon)

            # Mostrar las barras de vida nuevamente
            percentage_health_user_pokemon = int((health_user_pokemon * SIZE_HEALTH_BAR) / MAX_HEALTH_USER_POKEMON)
            print("{} HP: [{}{}] {}HP".format(USER["pokemon"]["name"], "*" * percentage_health_user_pokemon,
                                              " " * (SIZE_HEALTH_BAR - percentage_health_user_pokemon),
                                              health_user_pokemon))
            percentage_health_trainer_pokemon = int(
                (health_trainer_pokemon * SIZE_HEALTH_BAR) / MAX_HEALTH_TRAINER_POKEMON)
            print(
                "{} HP: [{}{}] {}HP".format(trainer_in_cell["pokemon"]["name"], "*" * percentage_health_trainer_pokemon,
                                            " " * (SIZE_HEALTH_BAR - percentage_health_trainer_pokemon),
                                            health_trainer_pokemon))

            input("Press enter to continue...")
            os.system("cls")

        if health_user_pokemon > health_trainer_pokemon:
            print("{} won the battle!!".format(USER["pokemon"]["name"]))
            percentage_health_user_pokemon = int((health_user_pokemon * SIZE_HEALTH_BAR) / MAX_HEALTH_USER_POKEMON)
            print("{} HP: [{}{}] {}HP".format(USER["pokemon"]["name"], "*" * percentage_health_user_pokemon,
                                              " " * (SIZE_HEALTH_BAR - percentage_health_user_pokemon), health_user_pokemon))
            percentage_health_trainer_pokemon = int((health_trainer_pokemon * SIZE_HEALTH_BAR) / MAX_HEALTH_TRAINER_POKEMON)
            print("{} HP: [{}{}] {}HP".format(trainer_in_cell["pokemon"]["name"], "*" * percentage_health_trainer_pokemon,
                                            " " * (SIZE_HEALTH_BAR - percentage_health_trainer_pokemon), health_trainer_pokemon))

            pokemon_trainers.remove(trainer_in_cell)  # Remove trainer from map

            health_user_pokemon = MAX_HEALTH_USER_POKEMON

            if not pokemon_trainers:
                print("\nYou beat all the trainers!\n"
                      "The game has finished\n"
                      "\nCONGRATULATIONS {}!!".format(user_name))
                game_over = True

        else:
            print("{} won the battle!!".format(trainer_in_cell["pokemon"]["name"]))
            percentage_health_user_pokemon = int((health_user_pokemon * SIZE_HEALTH_BAR) / MAX_HEALTH_USER_POKEMON)
            print("{} HP: [{}{}] {}HP".format(USER["pokemon"]["name"], "*" * percentage_health_user_pokemon,
                                              " " * (SIZE_HEALTH_BAR - percentage_health_user_pokemon), health_user_pokemon))
            percentage_health_trainer_pokemon = int((health_trainer_pokemon * SIZE_HEALTH_BAR) / MAX_HEALTH_TRAINER_POKEMON)
            print("{} HP: [{}{}] {}HP".format(trainer_in_cell["pokemon"]["name"], "*" * percentage_health_trainer_pokemon,
                                            " " * (SIZE_HEALTH_BAR - percentage_health_trainer_pokemon), health_trainer_pokemon))

            print("\nYou lost the battle... GAME OVER")
            game_over = True


    # Movement
    direction = readchar.readchar()
    new_position = my_position.copy()

    if direction == "w":
        new_position = [my_position[POS_X], (my_position[POS_Y] - 1) % MAP_HEIGHT]
    elif direction == "s":
        new_position = [my_position[POS_X], (my_position[POS_Y] + 1) % MAP_HEIGHT]
    elif direction == "a":
        new_position = [(my_position[POS_X] - 1) % MAP_WIDTH, my_position[POS_Y]]
    elif direction == "d":
        new_position = [(my_position[POS_X] + 1) % MAP_WIDTH, my_position[POS_Y]]
    elif direction == "q":
        print("Exit...")
        break

    if obstacle_definition[new_position[POS_Y]][new_position[POS_X]] == "#":
        continue

    my_position = new_position