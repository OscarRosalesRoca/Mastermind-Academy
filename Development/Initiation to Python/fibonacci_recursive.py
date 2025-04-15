def fibonacci(num1, num2):
    num3 = num1 + num2
    print(num3)

    if num3 == 1:
        print(num3)

    if num3 < 13:
        fibonacci(num2, num3)


def main():
    fibonacci(0, 1)

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