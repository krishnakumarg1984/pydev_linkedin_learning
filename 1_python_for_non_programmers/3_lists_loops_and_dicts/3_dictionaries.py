cats = {"Jane": 6, "Tom": 14, "Sarah": 8}
print(cats)
print(cats["Tom"])
# print(cats["tom"])
print(cats["Jane"])
# print(cats[8])

cats["Wilson"] = 1
print(cats)

del cats["Tom"]
print(cats)

print(len(cats))

ints_and_bools = {5: True, 7: False, 144: False}
print(ints_and_bools)
