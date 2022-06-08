# Command Line Arguments
import sys

# Print Arguments
print("Number of arguments: ", len(sys.argv), " arguments.")
print("Arguments ", sys.argv)

# Remove Arguments
# sys.argv.remove(sys.argv[0])
# sys.argv.pop(0)

# print("Arguments", sys.argv)

# Sum up the Arguments
arguments = sys.argv[1:]
total = 0
for arg in arguments:
    try:
        number = int(arg)
        total += number
    except Exception:
        print("Bad input")

print(f"Sum is {total}")
