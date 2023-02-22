class Car():
    def __init__(self, model, engine, doors, color):
        self.model = model
        self.engine = engine
        self.doors = doors
        self. color = color

    def horn(self):
        print("Vroom-Vroom Muthafucka")

car1 = Car("Toyota", "V6", 4, "Blue")

class Truck(Car):
    def __init__(self, trunk_capacity, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.trunk_capacity = trunk_capacity

    def cho_cho(self):
        print("Choo Choo")



truck1 = Truck(50,"Volvo", "V12", 2, "White")
#truck1.cho_cho()
print(truck1.color)
