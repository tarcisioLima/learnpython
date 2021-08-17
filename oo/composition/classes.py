
'''
É bom especializar a classe de endereços, criando uma classe especifica só para endereços.
No exemplo abaixo, usamos um endereço para compor um cliente. E no momento que o cliente é apagado da memória
todos os endereços são apagados também.
'''


class Customer:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.addresses = []

    def insert_address(self, city, state):
        self.addresses.append(Address(city, state))

    def list_addresses(self):
        for a in self.addresses:
            print(a.city, a.state)

    def __del__(self):
        print(f'{self.name} foi apagado')


class Address:
    def __init__(self, city, state):
        self.city = city
        self.state = state

    def __del__(self):
        print(f'{self.city}/{self.state} foi apagado')
