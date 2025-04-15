user_numbers = []

introduce_number = int(input("Write one number: "))
user_numbers.append(introduce_number)

lower_number = introduce_number
upper_number = introduce_number

while input("Do you want to write another number? (Y/N)") == "Y":
    introduce_number = int(input("Write one number: "))
    user_numbers.append(introduce_number)

for number in user_numbers[1:]:
    if number > upper_number:
        upper_number = number
    if number < lower_number:
        lower_number = number

print("In the list of numbers: ")
print(user_numbers)
print("The smallest number in the list is {} and the largest number is {}".format(lower_number, upper_number))