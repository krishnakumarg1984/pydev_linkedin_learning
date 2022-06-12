# ---
# jupyter:
#   jupytext:
#     text_representation:
#       extension: .py
#       format_name: light
#       format_version: '1.5'
#       jupytext_version: 1.13.8
#   kernelspec:
#     display_name: Python 3
#     language: python
#     name: python3
# ---


class Player:

    # Initialize class variables

    # Initialize a word bank that all players have access to
    # Players cannot change this word bank
    wordBank = [
        "treetop",
        "automobile",
        "garden",
        "television",
        "radio",
        "cream",
        "world",
        "chandelier",
    ]

    # Constructor
    def __init__(self, name, age):
        """Initialize instance variables"""

        # player's age
        self.age = age

        # player's name
        self.name = name

        # Keep track of player's points
        self.points = 0

        # Keep track of whether player is alive
        self.alive = False

    def lose_points(self, num):
        """Decrement this player's points by num."""

        self.points -= num

    def gain_points(self, num):
        """Increment this player's points by num."""

        self.points += num


# +
# create Player instance for nina
nina = Player("Nina", 24)

# display nina's name, age, points
print(nina.name, nina.age, nina.points)

# create Player instance for lisa
lisa = Player("Lisa", 22)

# display lisa's name, age, points
print(lisa.name, lisa.age, lisa.points)

# display nina's name, age, points
print(nina.name, nina.age, nina.points)

# nina gains 5 points
nina.gain_points(5)

# display nina's name, age, points
print(nina.name, nina.age, nina.points)

# display lisa's name, age, points
print(lisa.name, lisa.age, lisa.points)
# -
