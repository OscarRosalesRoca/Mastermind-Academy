def main():
    num1 = 0
    num2 = 1

    for f in range(8):
        num3 = num1 + num2
        print(num3)

        if num3 == 1:
            print(num3)

        num1 = num2
        num2 = num3


if __name__ == "__main__":
    main()

"""    
      0
      1
0+1 = 1
1+1 = 2
1+2 = 3
2+3 = 5
3+5 = 8
5+8 = 13

"""