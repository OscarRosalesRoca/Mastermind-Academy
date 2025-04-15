from random import randint
import os

#HEALTH STATS
SIZE_HEALTH_BAR = 10
MAX_HEALTH_PIKACHU = 80
MAX_HEALTH_SQUIRTLE = 90
health_pikachu = MAX_HEALTH_PIKACHU
health_squirtle = MAX_HEALTH_SQUIRTLE

#ATACK STATS
#Pikachu
thunderbolt = 10
iron_tail = 12
#Squirtle
water_gun = 13
bubbles = 9
tackle = 10


#Begging of the combat
title = "THE COMBAT BETWEEN PIKACHU AND SQUIRTLE HAS STARTED"
print("\n" + title + "\n" + "-" * len(title) + "\n")

percentage_health_pikachu = int((health_pikachu * SIZE_HEALTH_BAR) / MAX_HEALTH_PIKACHU)
print("Pikachu HP: [{}{}] {}HP".format("*" * percentage_health_pikachu,
                                       " " * (SIZE_HEALTH_BAR - percentage_health_pikachu), health_pikachu))
percentage_health_squirtle = int((health_squirtle * SIZE_HEALTH_BAR) / MAX_HEALTH_SQUIRTLE)
print("Pikachu HP: [{}{}] {}HP".format("*" * percentage_health_squirtle,
                                       " " * (SIZE_HEALTH_BAR - percentage_health_squirtle), health_squirtle))
input("Press enter to begin...")
os.system("cls")



while health_pikachu > 0 and health_squirtle > 0:

    #Pikachu's turn
    print("\nPikachu's turn!")
    rand_atak_pikachu = randint(1,2)
    if rand_atak_pikachu == 1:
        print("Pikachu use Thunderbolt... Squirtle -{}HP".format(thunderbolt))
        health_squirtle -= thunderbolt
    else:
        print("Pikachu use Iron Tail... Squirtle -{}HP".format(iron_tail))
        health_squirtle -= iron_tail

    if health_pikachu < 0:
        health_pikachu = 0
    elif health_squirtle < 0:
        health_squirtle = 0

    percentage_health_pikachu = int((health_pikachu * SIZE_HEALTH_BAR) / MAX_HEALTH_PIKACHU)
    print("Pikachu HP: [{}{}] {}HP".format("*" * percentage_health_pikachu,
                                           " " * (SIZE_HEALTH_BAR - percentage_health_pikachu), health_pikachu))
    percentage_health_squirtle = int((health_squirtle * SIZE_HEALTH_BAR) / MAX_HEALTH_SQUIRTLE)
    print("Pikachu HP: [{}{}] {}HP".format("*" * percentage_health_squirtle,
                                           " " * (SIZE_HEALTH_BAR - percentage_health_squirtle), health_squirtle))
    input("Press enter to continue...")
    os.system("cls")

    #Squirtle's turn
    #Atacks: Water (G)un, (B)ubble, (T)ackle
    print("\nSquirtle's turn!")
    option = None
    while option not in ["G", "B", "T", "N"]:
        option = input("Which atack do you want to use? Water (G)un, (B)ubble, (T)ackle. Or (N)othing and pass the turn.")
        if option == "G":
            print("Squirtle use Water Gun... Pikachu -{}HP".format(water_gun))
            health_pikachu -= water_gun
        elif option == "B":
            print("Squirtle use Bubble... Pikachu -{}HP".format(bubbles))
            health_pikachu -= bubbles
        elif option == "T":
            print("Squirtle use Tackle... Pikachu -{}HP".format(tackle))
            health_pikachu -= tackle
        elif option == "N":
            print("Squirtle does nothing")

    if health_pikachu < 0:
        health_pikachu = 0
    elif health_squirtle < 0:
        health_squirtle = 0

    percentage_health_pikachu = int((health_pikachu * SIZE_HEALTH_BAR) / MAX_HEALTH_PIKACHU)
    print("Squirtle HP: [{}{}] {}HP".format("*" * percentage_health_pikachu,
                                           " " * (SIZE_HEALTH_BAR - percentage_health_pikachu), health_pikachu))
    percentage_health_squirtle = int((health_squirtle * SIZE_HEALTH_BAR) / MAX_HEALTH_SQUIRTLE)
    print("Squirtle HP: [{}{}] {}HP".format("*" * percentage_health_squirtle,
                                           " " * (SIZE_HEALTH_BAR - percentage_health_squirtle), health_squirtle))
    input("Press enter to continue...")
    os.system("cls")


if health_squirtle > health_pikachu:
    print("\nSquirtle won the battle!!")
    percentage_health_pikachu = int((health_pikachu * SIZE_HEALTH_BAR) / MAX_HEALTH_PIKACHU)
    print("Squirtle HP: [{}{}] {}HP".format("*" * percentage_health_pikachu,
                                           " " * (SIZE_HEALTH_BAR - percentage_health_pikachu), health_pikachu))
    percentage_health_squirtle = int((health_squirtle * SIZE_HEALTH_BAR) / MAX_HEALTH_SQUIRTLE)
    print("Squirtle HP: [{}{}] {}HP".format("*" * percentage_health_squirtle,
                                           " " * (SIZE_HEALTH_BAR - percentage_health_squirtle), health_squirtle))
else:
    print("\nPikachu won the battle!!")
    percentage_health_pikachu = int((health_pikachu * SIZE_HEALTH_BAR) / MAX_HEALTH_PIKACHU)
    print("Squirtle HP: [{}{}] {}HP".format("*" * percentage_health_pikachu,
                                           " " * (SIZE_HEALTH_BAR - percentage_health_pikachu), health_pikachu))
    percentage_health_squirtle = int((health_squirtle * SIZE_HEALTH_BAR) / MAX_HEALTH_SQUIRTLE)
    print("Squirtle HP: [{}{}] {}HP".format("*" * percentage_health_squirtle,
                                           " " * (SIZE_HEALTH_BAR - percentage_health_squirtle), health_squirtle))