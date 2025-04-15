def upper_case(phrase):
    letters_phrase = []

    for letter in phrase:
        if letter == "a":
            letter = "A"
        elif letter == "b":
            letter = "B"
        elif letter == "c":
            letter = "C"
        elif letter == "d":
            letter = "D"
        elif letter == "e":
            letter = "E"
        elif letter == "f":
            letter = "F"
        elif letter == "g":
            letter = "G"
        elif letter == "h":
            letter = "H"
        elif letter == "i":
            letter = "I"
        elif letter == "j":
            letter = "J"
        elif letter == "k":
            letter = "K"
        elif letter == "l":
            letter = "L"
        elif letter == "m":
            letter = "M"
        elif letter == "n":
            letter = "N"
        elif letter == "o":
            letter = "O"
        elif letter == "p":
            letter = "P"
        elif letter == "q":
            letter = "Q"
        elif letter == "r":
            letter = "R"
        elif letter == "s":
            letter = "S"
        elif letter == "t":
            letter = "T"
        elif letter == "u":
            letter = "U"
        elif letter == "v":
            letter = "V"
        elif letter == "w":
            letter = "W"
        elif letter == "x":
            letter = "X"
        elif letter == "y":
            letter = "Y"
        elif letter == "z":
            letter = "Z"
        else:
            letter = " "

        letters_phrase.append(letter)

    print("".join(letters_phrase))

def main():
    user_phrase = input("Write a phrase in lower case: ")
    upper_case(user_phrase)


if __name__ == "__main__":
    main()