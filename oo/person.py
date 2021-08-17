from datetime import datetime
from random import randint

class Person:
    # Atributo da classe
    current_year = int(datetime.strftime(datetime.now(), '%Y'))

    # __ini__ e def (metodos) são métodos da instância, por isso se passa o self.
    # existe também class method que se refere a classe, não a instancia em si.
    # Deve usar o decorator @classmethod, daí acessamos como se fosse um método estatico, sem precisa instanciar.

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

    # Um método que fabrica objetos
    @classmethod
    def by_birth_date(cls, name, birth_date):
        age = cls.current_year - birth_date
        return cls(name, age)

    # Static method @staticmethod (não nada da classe nem da instancia)
    @staticmethod
    def generate_id():
        rand = randint(10000, 19999)
        return rand


