user_number = int(input("Which number do you want to multiply"))

for number in range(11):
    if number != 0:
        solution = user_number * number
        print("{} x {} = {}".format(user_number, number, solution))