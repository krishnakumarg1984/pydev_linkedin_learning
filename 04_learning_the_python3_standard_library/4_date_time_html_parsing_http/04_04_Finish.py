# Create a Timer with the Time module
import time

run = input("Start? >")

# seconds = 0
seconds = 10

if run == "yes":
    # while seconds != 10:
    while seconds >= 0:
        print(">", seconds)
        time.sleep(1)
        # seconds += 1
        seconds -= 1
    # print(">", seconds)
