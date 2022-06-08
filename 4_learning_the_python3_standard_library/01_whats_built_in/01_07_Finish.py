# Least to Greatest
pointsInaGame = [0, -10, 15, -2, 1, 12]
sortedGame = sorted(pointsInaGame)
print(sortedGame)

# Alphabetically
children = ["Sue", "Jerry", "Linda"]
print(sorted(children))
print(sorted(["Sue", "jerry", "linda"]))
print(sorted(["Sue", "jerry", "linda"], key=str.upper))

# Key Parameters
print(sorted("My favorite child is Linda".split(), key=str.upper))
print(sorted(pointsInaGame, reverse=True))

# leaderBoard = {231: "CKL", 123: "ABC", 432: "JKC"}
leaderBoard = {231: "CKL", 104: "DEF", 123: "ABC", 432: "JKC"}

# print({k: v for k, v in sorted(leaderBoard.items(), key=lambda item: item[1])})
print(dict(sorted(leaderBoard.items(), key=lambda item: item[1])))

print(sorted(leaderBoard, reverse=True))
print(leaderBoard.get(432))

students = [("alice", "B", 12), ("eliza", "A", 16), ("tae", "C", 15)]
print(sorted(students))
print(sorted(students, key=lambda student: student[0]))
print(sorted(students, key=lambda student: student[1]))
print(sorted(students, key=lambda student: student[2]))
