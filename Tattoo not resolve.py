print("We glad to see you in our tattoo studio")
print("Please, tell us a bit about yourself")
age = int(input("How old r u?: "))
name = input("What's your name?")
budget = int(input("Budget for tattoo?"))
print("Let check the summary info about you")
print(f"Your name is {name}, Your age is {age}, and your budget is {budget}")
agree = input("Correct? Yes or Not ")
if agree == "Yes" or "yes":
    print("Info accepted, W8 for managers call")
elif agree == "Not" or "not":
    print("Info not accepted, try again")
else:
    print("I can't understand you, go away")