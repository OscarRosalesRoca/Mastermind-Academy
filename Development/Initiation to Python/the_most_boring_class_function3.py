def even_odd (number):
    if number % 2 == 0:
        print("{} is even".format(number))
    elif number % 2 != 0:
        print("{} is odd".format(number))
    else:
        print("{} out of logic")


def main():
    user_num = int(input("Type one number and we will see if is even or odd: "))
    even_odd(user_num)


if __name__ == "__main__":
    main()