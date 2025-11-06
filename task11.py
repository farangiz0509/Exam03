class Vehicle:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def move(self):
        print("Vehicle is moving")

class Car(Vehicle):
    def move(self):
        print("Car is driving")

v = Vehicle("BMW", "X5")
c = Car("Tesla", "Model S")

v.move()
c.move()