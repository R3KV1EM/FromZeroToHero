#Scroll down to see the answers!
#1 Create a user profile for your new game. This user profile will be stored in a dictionary with keys: 'age', 'username', 'weapons', 'is_active' and 'clan'

#2 iterate and print all the keys in the above user.

#3 Add a new weapon to your user

#4 Add a new key to include 'is_banned'. Set it to false

#5 Ban the user by setting the previous key to True

#6 create a new user2 my copying the previous user and update the age value and username value.

user = {
    "age": 30,
    "Username": "Archy",
    "weapons": ["Axe", "Bow"],
    "is_active": True,
    "Clan": "Marmons"
}
print(user.keys()) # Печатаем ключи словаря
user["weapons"].append("Lantern") # Добавляем оружие в конец словаря
user.get("is_banned", False) # Устанавливаем новый ключ is_banned со значением False
user['is_banned'] = True # Меняем на значение True
user2 = user.copy() # создаем аналогичный словарь
user2.update({"age": 55}) # Обновляем возраст
user2.update({"Username": "Polly"}) # Обновляем имя
print(user)
print(user2)