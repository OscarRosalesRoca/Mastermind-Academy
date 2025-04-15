def add_to_list (thing, shop_list):
    if thing not in list:
        shop_list.append(thing)
        print("{} has added to the list".format(shop_list))
    else:
        print("{} is already in the shop-list".format(shop_list))

def main():
    shop_list = [
        "water",
        "milk",
        "bread",
        "sal",
        "pepper"
    ]

    print("The shop-list has: \n"
          "{}".format(shop_list))
    user_will = input("Do you want to add one more thing to the list? (Y/N)")
    while user_will != "Y" and user_will != "N":
        user_will = input("Do you want to add one more thing to the list? (Y/N)")

    if user_will == "Y":
        new_thing = input("What do you want to add to the list? ")
        add_to_list(new_thing, shop_list)
    elif user_will == "N":
        exit()


if __name__ == "__main__":
    main()