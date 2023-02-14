# Penalty Shootout
import random
good = []
bad = []
def penalty():
    shoot = [True, False]
    bam = random.choice(shoot)
    if bam == True:
        print("Goal scored")
        good.append(bam)
    else:
        print("Miss")
        bad.append(bam)
i = 100

while i > 5:
    i -= 1
    penalty()
   
print(len(bad))
print(len(good))
