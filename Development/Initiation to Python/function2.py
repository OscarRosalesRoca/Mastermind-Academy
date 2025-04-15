def power_of_number(base, exponent):
    result = pow(base, exponent)
    return result

def main():
    print("Hello world!")

    number_1 = int(input("Type one number: "))
    number_2 = int(input("Type another number: "))

    print("{} to the power of {} is {}".format(number_1, number_2, power_of_number(number_1, number_2)))

if __name__ == "__main__":
    main()