from person import Person

p1 = Person('Tarcísio', 24)
p2  = Person('Danielle', 21)

p1.to_speak('paçoca')
p2.to_speak('movies')

print('Acessando atributo da classe: ', Person.current_year)

print(p1.get_birth_year())
print(p2.get_birth_year())

# Class method que é um factory method (fabrica objetos)
p3 = Person.by_birth_date('Gabriel', 1997)
# p3 = Person('Gabriel', 1997)

print('P3: ', p3, p3.name, p3.age)

'''
Para saber se deve usar class method, 
é bom pensar se a classe se refere ao molde (instancia) ou a classe.
'''

print('STATIC: ', Person.generate_id())
