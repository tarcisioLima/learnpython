"""
Motivo do uso: otimização de performance e escrever menos código.
"""

l1 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
l2 = [v for v in l1] # Jogando um valor novo para dentro da lista.

multiplied = l2 = [v * 2 for v in l1]
tuples = [(v, v2) for v in l1 for v2 in range(3)]

print('multiplied: ', multiplied)
print('tuples: ', tuples)

l3 = ['Gabriel', 'Maria', 'Danielle']
replace = [v.replace('a', '@') for v in l3]

tp = (
    ('key', 'value'),
    ('key2', 'value2'),
)

ex1 = [(v, k) for k, v in tp]
print('tp: ', dict(ex1))

l4 = list(range(100))
ex2 = [v for v in l4 if v % 2 == 0 if v % 8 == 0] # Filtrou a lista

print('ex2', ex2)

ex3 = [v if v % 3 == 0 else '_' for v in l4]

print('ex3', ex3)