from person import Person

p1 = Person('Tarcísio', 24)
p2  = Person('Danielle', 21)

p1.to_speak('paçoca')
p2.to_speak('movies')

print(p1.get_birth_year())
print(p2.get_birth_year())