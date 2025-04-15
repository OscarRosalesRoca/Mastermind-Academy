def the_largest_string (*args):
    largest_string = ""

    if args:
        largest = []
        for string in args:
            largest.append(string)

        for each in largest:
            if len(each) > len(largest_string):
                largest_string = each

    return  largest_string


def main():
    print("The largest string between: hello - beautiful - world, is: {}".format(the_largest_string
                                                                                 ("hello", "beautiful", "world")))

if __name__ == "__main__":
    main()