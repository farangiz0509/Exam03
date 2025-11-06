class Bird:
    def speak(self):
        print("Chip Chip")

class Dog:
    def speak(self):
        print("Woof Woof")

animals = [Bird(), Dog()]
for a in animals:
    a.speak()