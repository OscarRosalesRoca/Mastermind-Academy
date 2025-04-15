user_phrase = input("Write a phrase:")

blank_spaces = 0
dots = 0
comma = 0

for item in user_phrase:
    if item == " ":
        blank_spaces += 1
    elif item == ".":
        dots += 1
    elif item == ",":
        comma += 1

print("In the user phrase:")
print(user_phrase)
print("I found {} blank spaces, {} dots and {} commas".format(blank_spaces, dots, comma))