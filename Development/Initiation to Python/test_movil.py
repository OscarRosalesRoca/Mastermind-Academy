option = input("¿[I]iOS o [A]Android?")

if option == "A":
    option = input("Do you have money? (Y/N)")
    if option == "Y":
        option = input("The camera is important to you? (Y/N)")
        if option == "Y":
            print("Google Pixel 9 PRO")
        elif option == "N":
            print("Android affordable")
    elif option == "N":
        print("Chinese phone")
    else:
        print("Options are YES(Y) or NO(N)")
elif option == "I":
    option = input("Do you have money? (Y/N)")
    if option == "Y":
        print("iPhone 16 ULTRA")
    elif option == "N":
        print("iPhone second hand")
    else:
        print("Options are YES(Y) or NO(N)")
