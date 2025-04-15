dollar_euro = 0.96385
euro_dollar = 1.03750
pound_euro = 1.2604
euro_pound = 0.7946

type_change = input("Which type of currency do you need to change?\n"
                    "Dollars to euros (DE)\n"
                    "Euros to dollars (ED)\n"
                    "Pounds to euros (PE)\n"
                    "Euros to pounds (EP)\n")

money = float(input("How many currency do you want to change?"))

if type_change == "DE":
    result = money * dollar_euro
    print("{} dollar equals to {} euros".format(money, result))
elif type_change == "ED":
    result = money * euro_dollar
    print("{} euros equals to {} dollars".format(money, result))
elif type_change == "PE":
    result = money * pound_euro
    print("{} pounds equals to {} euros".format(money, result))
elif type_change == "EP":
    result = money * euro_dollar
    print("{} euros equals to {} pounds".format(money, result))
else:
    print("You have to type DE, ED, PE or EP")
    exit()


