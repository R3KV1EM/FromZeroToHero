# Main functions of Roulette
import random
print("Welcome to Casino Royale")
table = list(range(37))
red = [32, 19, 21, 25, 34, 27, 36, 30, 23, 5, 16, 1, 14, 9, 18, 7, 12, 3]
black = [15, 4, 2, 17, 6, 13, 11, 8, 10, 24, 33, 20, 31, 22, 29, 28, 35, 26]
low = list(range(1, 19))
high = list(range(19, 37))
bet = input.("Place your bet \nLow or High \nRed or Black \nOr choose a number if you want: ")
spin = random.choice(table)
print(spin)
if bet == str(spin):
    print("You are crazy ass, get x36")
elif bet == "low" and low.count(spin):
    print("Wow, you won! Take x2")
elif bet == "high" and high.count(spin):
    print("Wow, You win")
elif bet == "red" and red.count(spin):
    print("Good choice to place in red, you get multiply")
elif bet == "black" and black.count(spin):
    print("Good choice to place in black, get multiply")
else:
    print("Better luck next")
