import random

print(random.randint(1, 10))
print(random.random())

answer = random.randint(1, 3)
if answer == 1:
    print("yes")
elif answer == 2:
    print("no")
else:
    print("maybe")
