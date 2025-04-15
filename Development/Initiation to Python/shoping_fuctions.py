EXIT = "EXIT"
OPEN_FILE_MODE = "w"
INVENTORY = [
    "milk",
    "bread",
    "eggs",
    "cheese",
    "chicken",
    "apples",
    "rice",
    "pasta",
    "tomatoes",
    "juice"
]

def asking_products():
    return input("[Type {} to exit and INVENTORY to check the available products]\n"
                 "Type a product or a command: ".format(EXIT)).lower()


def asking_name_file():
    return input("\nType the name of the .txt file where you want to write in the shopping list: ")


def show_list():
    return print(INVENTORY, "\n")


def alert_not_in_list(product):
    return print("The product: {} is not available. Add only the products in the INVENTORY".format(product))


def save_txt(shop_list, file_name, mode):
    with open(file_name + ".txt", mode) as my_file:
        my_file.write("\n".join(shop_list))

    """
    a = open(file_name + ".txt", mode)
    a.write("\n".join(shop_list))
    a.close()
    """


def main():
    shopping_list = []

    input_user = asking_products()

    while input_user != EXIT:
        if input_user == "INVENTORY":
            show_list()
        else:
            if input_user in INVENTORY:
                shopping_list.append(input_user)
                print(" ")
                print("\n".join(shopping_list))
                print(" ")
            else:
                alert_not_in_list(input_user)
        input_user = asking_products()
        #End of while


    file_name = asking_name_file()

    save_txt(shopping_list, file_name, OPEN_FILE_MODE)


if __name__ == "__main__":
    main()



"""
[a.lowe() for a in shop_list]

second_shop_list = []
for a in shop_list:
    second_shop_list.append(a.lower())
"""