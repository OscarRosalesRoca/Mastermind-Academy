age = int(input("Tell me your age pls: "))
situation = input("Are you a student, pensioner or do you belong to a large family? "
               "(S for a student)/(P for a pensioner)/(L for a large family)/(N for nothing)")

if ((25 <= age <= 35 and situation == "S") or age <= 10 or (age >= 65 and situation == "P") or situation == "L"):
    print("You earned a discount")
else:
    print("You haven't earned a discount")