# Itertools
import itertools

# Infinite Counting
# for x in itertools.count(50):
for x in itertools.count(50, 5):
    print(x)
    if x == 80:
        break

x = 0
# Infinite Cycling
# for c in itertools.cycle("RACECAR"):
for c in itertools.cycle([1, 2, 3, 4]):
    print(c)
    # x = x + 1
    x += 1
    if x > 15:
        break

# Infinite Repeating
# x = 0
for r in itertools.repeat(True):
    print(r)
    x += 1
    if x > 10:
        break
