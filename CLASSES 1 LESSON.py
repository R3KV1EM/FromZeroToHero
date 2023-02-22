# Let's make some classes
class Car:
    coupe = True  # статик для всех машин

    def __init__(self, name, engine, color, doors):
        self._name = name
        self._engine = engine
        self._color = color
        self._doors = doors


car1 = Car("Mustang", "V8", "Red", "Two")
car2 = Car("Chevrolet", "V12", "Blue", "Four")
print(car1)
print(car2)
print(car1._color)
