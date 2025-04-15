def power_of_number(base, exponent=2):
    if exponent:
        result = pow(base, exponent)
    else:
        result = pow(base, 2)

    return result


def main():
    print(power_of_number(2))
    print(power_of_number(2, 5))


if __name__ == "__main__":
    main()