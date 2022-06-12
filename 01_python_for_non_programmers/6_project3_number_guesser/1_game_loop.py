guess = int(input("What) is your guess?: "))
correct_number = 5
guess_count = 1

while guess != correct_number:
    guess_count += 1
    guess = int(input("What) is your guess?: "))

print(
    f"Congrats! The right answer was {correct_number}. It took you {guess_count} guesses."
)
