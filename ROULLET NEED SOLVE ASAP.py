import random
print("Hello Welcome to Roullete")
roulettable = tuple(range(0, 37))
balance = 1000
st1 = list(range(1, 18))
st2 = list(range(19, 36))
print(roulettable)
print("If you want to place 1-18 write X or 19-36 write Z")
bet = input("Place a bet, from 0 to 36, ")
drop = random.choice(roulettable)
print(drop)
st1.count(drop)
st2.count(drop)
if st1.count(drop) == 1:
    print("Congrats, you won ")
elif st2.count(drop) == 1:
    print("Congrats, you won ")
else:
    print("You lost, GL next time")
