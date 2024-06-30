class Student:
    def __init__(self, name, age, major):
        self.name = name
        self.age = age
        self.major = major

    def __repr__(self):
        return f"Student(name={self.name}, age={self.age}, major={self.major})"