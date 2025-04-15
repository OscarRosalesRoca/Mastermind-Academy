from random import randint

def guess_number (number):
    secret_number = randint(1, 100)
    if number == secret_number:
        print("You guessed the secret number!")
        game = False
    else:
        print("Try again.")

def main():
    game = True

    while game:
        user_number = int(input("Type a number between 1 and 100: "))
        while user_number not in range(100):
            user_number = int(input("Type a number between 1 and 100: "))
        guess_number(user_number)



if __name__ == "__main__":
    main()