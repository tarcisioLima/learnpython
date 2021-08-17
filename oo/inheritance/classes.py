# Super class
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.classname = self.__class__.__name__

    def speak(self):
        print(f'{self.classname} is speaking')


# Sub class
class Customer(Person):
    def buy(self):
        print(f'{self.classname} is buying')


# Sub class
class Student(Person):
    def study(self):
        print(f'{self.classname} is studying')


