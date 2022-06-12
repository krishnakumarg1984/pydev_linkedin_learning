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

# Import relevant modules
import random


class Hangman:
    
    # Initialize class variables
    # Word bank from which game draws word
    word_bank = ['treetop','automobile','garden', 'television', 'radio','cream','world', 'chandelier']
    
    # Constructor
    def __init__(self):
        
        """Initialize instance variables and set up board"""
        
        # Keep track of whether player loses or wins
        self.lose = False
        
        # Keep track of correct letters picked by player
        self.correctLetters = []
        
        # Choose a word randomly from word bank
        self.word = random.choice(self.word_bank)
        
        # Keep track of number of body parts when player chooses incorrect letters
        self.bodyParts = 0
        
        # Set up board (display a "blank" for each letter in word)
        print('__ ' * len(self.word))
        
    def displayBoard(self):
        
        """Display board:
        display letters in word that were picked
        display 'blanks' for letters in word that were not picked"""
        
        for letter in self.word:
            if letter in self.correctLetters:
                print(letter, end = ' ')
            else:
                print('__', end = ' ')
                
 
    def checkForMatch(self, letterChoice):
        
        """Check if the player's current letter choice matches any of the letters in word.
        Display result accordingly.
        If there's a match, update the board.
        Otherwise, add a body part and update the lose instance variable as needed."""
        
        if letterChoice in self.word:
            for letter in self.word:
                if letter == letterChoice:
                    self.correctLetters.append(letterChoice)
            print('Match!')
        else:
            self.bodyParts += 1
            if self.bodyParts == 10:
                self.lose = True
            print('Not a match!')
        
    def play(self):
        
        """Carry out game:
        While the player has not guessed all letters in word and not all body parts have been added,
        the game proceeds (player continues to guess); otherwise, game reaches end.
        Each time player chooses a letter, check if it's a match, and then display the updated board.
        At end of game, check whether player loses or wins, and display result accordingly."""
        
        while len(self.correctLetters) != len(self.word) and self.bodyParts < 10:
            print()
            letterChoice = input('Pick a letter: ')
            self.checkForMatch(letterChoice)
            self.displayBoard()
      
        if (self.lose == True):
            print()
            print("You lost!")
        else:
            print()
            print("You won!")

        return 

# Create an instance of Hangman
HM_game1 = Hangman()
# Play a game of Hangman
HM_game1.play()


