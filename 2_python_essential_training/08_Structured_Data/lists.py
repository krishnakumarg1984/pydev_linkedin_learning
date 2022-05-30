#!/usr/bin/env python3


def main():
    # game = ["Rock", "Paper", "Scissors", "Lizard", "Spock"]
    game = ("Rock", "Paper", "Scissors", "Lizard", "Spock")
    # print(game[1])  # begin
    # print(game[1:3])  # begin: end
    # print(game[1:5:2])  # begin:end:step
    # i = game.index("Paper")  # search for "Paper" in the list 'game'
    # print(game[i])
    # game.append("Computer")
    # game.insert(1, "Cellphone")
    # game.remove("Scissors")
    # x = game.pop()
    # print(x)
    # y = game.pop(3)
    # print(y)
    # del game[3]
    # del game[1:3]
    # del game[1:5:2]
    print(", ".join(game))
    print(len(game))
    print_list(game)


def print_list(o):
    for i in o:
        print(i, end=" ", flush=True)
    print()


if __name__ == "__main__":
    main()
