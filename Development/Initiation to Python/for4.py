user_number = int(input("Which number do you want to multiply"))

for number in range(11):
    if number != 0:
        solution = user_number * number
        if number % 2 == 0:
            print(f"{user_number} x {number} = {solution}")

