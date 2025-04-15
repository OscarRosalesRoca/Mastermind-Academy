option = None
buy_list = []
while option != "Q":
    option = input("\nWhat do you want to buy? (Type [Q]uit to end the program)")

    if option == "Q":
        break

    check = input("Are you sure that want to note {} in the list? ([Y]es or [N]o)".format(option))
    while check != "Y" and check != "N":
        check = input("Please type Y/N to confirm")

    if check == "Y":
        if option in buy_list:
            print("{} is already in the list".format(option))
        else:
            buy_list.append(option)
            print("{} has been noted in the list".format(option))
    elif check == "N":
        print("Okey, {} wont be in the list".format(option))

print("The resultant list is: {}".format(buy_list))