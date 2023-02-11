username = input("Hello, what\'s your name? ")
password = int(input("password "))
passwordlenght = len(str(password))
finalpass = passwordlenght * "*"
print(f"{username}, your password {finalpass} is {passwordlenght} letters long ")
