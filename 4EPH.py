import random

table = list(range(37))
x = list(range(1, 19))
z = list(range(19, 37))

print("Welcome to Roulette, place a bet")
bet = input("Place your bet on 1-18 (input 't') or 19-36 (input 'y') : ")

spin = random.choice(table)
print(f"The ball landed on: {spin}")

if bet == "t" and spin in x:
    print("Congratulations! You win.")
elif bet == "y" and spin in z:
    print("Congratulations! You win.")
else:
    print("Sorry, better luck next time.")

    import random

    table = list(range(37))
    bet_range_1 = list(range(1, 19))
    bet_range_2 = list(range(19, 37))

    print("Welcome to Roulette, place a bet")
    bet = input("Place your bet on 1-18 (input 't') or 19-36 (input 'y') : ")

    spin = random.choice(table)
    print(f"The ball landed on: {spin}")

    if bet == "t" and spin in bet_range_1:
        print("Congratulations! You win.")
    elif bet == "y" and spin in bet_range_2:
        print("Congratulations! You win.")
    else:
        print("Sorry, better luck next time.")
