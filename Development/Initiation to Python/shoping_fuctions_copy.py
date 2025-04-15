EXIT = "EXIT"
OPEN_FILE_MODE_WRITE = "w"
OPEN_FILE_MODE_READ = "r"
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
FILE_LIST = "shopping.txt"

def asking_products():
    return input("[Type {} to exit and INVENTORY to check the available products]\n"
                 "Type a product or a command: ".format(EXIT)).lower()


def asking_name_file():
    return input("\nType the name of the .txt file where you want to write in the shopping list: ")


def show_inventory():
    return print(INVENTORY, "\n")


def show_shopping_list(shop_list):
    return print(shop_list)


def alert_not_in_list(product):
    return print("The product: {} is not available. Add only the products in the INVENTORY".format(product))


def save_item_in_shopping_list(shop_list, user_item):
    if user_item.lower() in [a.lower() for a in shop_list]:
        alert_not_in_list(user_item)
    else:
        shop_list.append(user_item)


def save_txt(shop_list, file_name, mode):
    with open(file_name + ".txt", mode) as my_file:
        my_file.write("\n".join(shop_list))


def load_create_file_list():
    shop_list = []
    if input("Do you want to load the last shopping list? [Y/N]") == "Y":
        try:
            with open(FILE_LIST, OPEN_FILE_MODE_READ) as a:
                shop_list = a.read().split("\n")
        except FileNotFoundError:
            print("File not found.")
    return shop_list


def main():
    shopping_list = load_create_file_list()
    show_shopping_list(shopping_list)

    input_user = asking_products()

    while input_user != EXIT:
        save_item_in_shopping_list(shopping_list)
        show_shopping_list(shopping_list)
        input_user = asking_products()

    file_name = asking_name_file()
    save_txt(shopping_list, file_name, OPEN_FILE_MODE_WRITE)


if __name__ == "__main__":
    main()

