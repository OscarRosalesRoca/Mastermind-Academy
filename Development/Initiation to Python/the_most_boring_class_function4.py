def are_you_sure (answer):
    if answer == "Y":
        sure = True
        print(sure)
    elif answer == "N":
        sure = False
        print(sure)
    else:
        print("Error typing...")



def main():
    sure = None
    answer = input("Are you sure? (Y/N)")
    are_you_sure(answer)


if __name__ == "__main__":
    main()