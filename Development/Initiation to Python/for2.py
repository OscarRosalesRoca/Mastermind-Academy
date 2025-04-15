import string

user_text = input("Write a phrase: ")
upper_case_found = 0

for item in user_text:
    if item in string.ascii_uppercase:
        upper_case_found += 1

print("I found {} upper cases in the user phrase:".format(upper_case_found))
print(user_text)