from datetime import datetime

class Person:
    current_year = int(datetime.strftime(datetime.now(), '%Y'))

    def __init__(self, name, age, eating=False, speaking=False):
        self.name = name
        self.age = age
        self.eating = eating
        self.speaking = speaking

    def to_speak(self, subject='anything'):
        if self.eating:
            print(f'{self.name} cannot speak while is eating')
            return
        if self.speaking:
            print(f'{self.name} is already speaking')
            return
        print(f'{self.name} is speaking about {subject}')
        self.speaking = True

    def stop_speaking(self):
        if not self.speaking:
            print(f'{self.name} is not speaking')
            return
        print(f'{self.name} stopped speaking')
        self.speaking = False

    def to_eat(self, food='apple'):
        if self.eating:
            print(f'{self.name} is already eating')
            return
        if self.speaking:
            print(f'{self.name} cannot eat while is speaking')

        print(f'{self.name} is eating {food}')
        self.eating = True

    def stop_eating(self):
        if not self.eating:
            print(f'{self.name} is not eating')
            return
        print(f'{self.name} stopped eating')
        self.eating = False

    def get_birth_year(self):
        return self.current_year - self.age
