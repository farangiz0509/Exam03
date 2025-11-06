class Rectangle:
    def __init__(self, w, h):
        self.w = w
        self.h = h

    def area(self):
        return self.w * self.h

r1 = Rectangle(4, 5)
r2 = Rectangle(6, 3)

print(r1.area())
print(r2.area())