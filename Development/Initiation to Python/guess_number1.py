import random

num_guess = random.randint(1, 10)
num_user = int(input("Guess the number from 1 to 10:"))



if num_user == num_guess:
    print("¡You guessed the secret number!")
    print("The secret number was...'{}'".format(num_guess))
else:
    print("You didn't guess the secret number...")
    print("The secret number was...'{}'".format(num_guess))