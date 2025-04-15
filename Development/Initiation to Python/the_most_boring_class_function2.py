def plus_list (list):
    total = 0
    for each in list:
        total += each

    return total


def main():
    my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    print("If we add up all the numbers in our list the result is: {}".format(plus_list(my_list)))


if __name__ == "__main__":
    main()