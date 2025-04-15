title ="Welcome to the tests of cheese"
print("\n" + title + "\n" + "-" * len(title) + "\n")

points = 0

option1 = input("Question 1: What do you do if you see a table of cheese?\n"
                "A - Run away\n"
                "B - Taste some of them\n"
                "C - I can't stop devouring them\n"
                "(A/B/C)")

if option1 == "A":
    points += 0
elif option1 == "B":
    points += 5
elif option1 == "C":
    points += 10
else:
    print("The options are A, B and C")
    exit()

option2 = input("Question 2: How do you like de hamburgers?\n"
                "A - Without cheese\n"
                "B - With cheese\n"
                "C - Just cheese, no need of meat\n"
                "(A/B/C)")

if option1 == "A":
    points += 0
elif option1 == "B":
    points += 5
elif option1 == "C":
    points += 10
else:
    print("The options are A, B and C")
    exit()

option3 = input("Question 3: Are you lactose intolerant?\n"
                "A - Yes\n"
                "B - Sometimes\n"
                "C - No\n"
                "(A/B/C)")

if option1 == "A":
    points += 0
elif option1 == "B":
    points += 5
elif option1 == "C":
    points += 10
else:
    print("The options are A, B and C")
    exit()

if points < 15:
    print("Result: You don't like the cheese. Score: {}".format(points))
elif 15 <= points < 25:
    print("Result: You really like the cheese. Score: {}".format(points))
elif points >=25:
    print("Result: YOU ARE A FAN OF CHEESE. Score: {}".format(points))
