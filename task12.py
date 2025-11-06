class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def introduce(self):
        print(f"My name is {self.name}, I am {self.age} years old.")

class Student(Person):
    def __init__(self, name, age, grade):
        super().__init__(name, age)
        self.grade = grade

    def introduce(self):
        print(f"My name is {self.name}, I am {self.age}, grade {self.grade}.")

p = Person("Ali", 25)
s = Student("Vali", 17, 11)

p.introduce()
s.introduce()