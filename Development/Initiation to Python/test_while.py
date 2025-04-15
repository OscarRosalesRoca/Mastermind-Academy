answer = None

while answer != "A" and answer != "B" and answer != "C":

    answer = input("¿Which option do you prefer? [A, B, C]")
    if answer == "A":
        print("You've chosen correctly")
    elif answer == "B":
        print("You could have chosen better")
    elif answer == "C":
        print("You've chosen incorrectly")
    else:
        print("You have to type 'A', 'B' or 'C'")