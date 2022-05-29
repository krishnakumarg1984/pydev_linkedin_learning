user_text = input("Enter some text: ")
# print(user_text.upper())

upper_or_lower = input("Enter 1 to uppercase, 2 to lowercase ...")
if upper_or_lower == "1":
    print(user_text.upper())
else:
    print(user_text.lower())

user_number = input("What do you want to double? ")
print(int(user_number) * 2)
