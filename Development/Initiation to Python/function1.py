def calculator(num1, num2):
    result = num1 + num2
    return result

def main():
    print("Hello world!")

    number_1 = int(input("Type one number: "))
    number_2 = int(input("Type another number: "))

    print(calculator(number_1, number_2))

if __name__ == "__main__":
    main()