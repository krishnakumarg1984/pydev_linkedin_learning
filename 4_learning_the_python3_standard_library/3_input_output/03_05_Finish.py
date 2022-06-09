# Iterative Files
myFile = open("scores.txt", "r")

# Read one line at a time
print("My one line: \n" + myFile.readline())

myFile.seek(0)

# Iterate through each line of a file
for line in myFile:
    newHighScorer = line.replace("BBB", "PDJ")
    print(newHighScorer, end="")

myFile.close()
