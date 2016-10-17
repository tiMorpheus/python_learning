class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def to_string(self):
        print(self.name, "is", self.age)


john = Person('John', 22)

lucy = Person('Lucy', 21)

john.to_string()
lucy.to_string()
