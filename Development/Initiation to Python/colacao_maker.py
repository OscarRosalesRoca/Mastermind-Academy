print("I'm going to the kitchen")
print("I open the fridge")

milk = input("Is there milk? (Y/N)")
colacao = input("Is there Colacao? (Y/N)")

if milk != "Y" or colacao != "Y":
    print("I'm going to the supermarket")
    if milk != "Y":
        print("I buy milk")
    if colacao != "Y":
        print("I buy Colacao")

print("We put the milk in the glass with the Colacao and mix it")
