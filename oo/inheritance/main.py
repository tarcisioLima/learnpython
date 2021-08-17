
from classes import Customer, Person, Student

'''
Associação = Usa 
Agregação = Tem
Composição = É dono
Herança = É
'''

c1 = Customer('Danielle', 21)

s1 = Student('Otavio', 33)

p1 = Person('Gabriel', 24)

p1.speak()

c1.speak()
c1.buy()

s1.speak()
s1.study()

