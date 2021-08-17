'''
O tipo de associação mais forte entre classes.
Uma classe vai ser dona de objetos de outra classe. Isso quer dizer que se uma classe principal for apagada
todos os objetos associados com ela vão ser apagados também.
'''

from classes import Customer

c1 = Customer('Luiz', 32)
print(c1.name)
c1.insert_address('Belo Horizonte', 'MG')
c1.list_addresses()
del c1
print()

c2 = Customer('Maria', 32)
print(c2.name)
c2.insert_address('Salvador', 'BH')
c2.insert_address('Rio de Janeiro', 'RJ')
c2.list_addresses()

print()

c3 = Customer('João', 19)
print(c3.name)
c3.insert_address('Santos', 'SP')
c3.list_addresses()

print('###########################')
'''
O garbage collector vai mostrar abaixo os itens apagados.
'''
