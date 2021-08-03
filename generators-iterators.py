import sys
import time

list_a = [1, 2, 3, 4, 5]

''' 
Um iterável não é necessáriamente um iterador;
Os iteradores são iteráveis;

Para saber se é um iterável como listas e strings: '''
print(hasattr(list_a, '__iter__'))

# No for, é transformado a lista num iterador para fazer print por exemplo.
# O for faz a transformação da lista com o método iter(lista), daí ela passa a ser um iterador

''' Para saber se é um iterador '''
print(hasattr(list_a, '__next__'))

print('next: ', next(iter(list_a)))
print('next: ', next(iter(list_a)))
print('next: ', next(iter(list_a)))

''' 
Geradores são usados quando a gente precisa de usar valores que ocupam muita memoria ou tempo.
'''
list_b = [x for x in range(1000)]
list_b2 = (x for x in range(1000))

print(f'LIST NORMAL type: {type(list_b)} size: {sys.getsizeof(list_b)}')
print(f'LIST NORMAL type: {type(list_b2)} size: {sys.getsizeof(list_b2)}')

''' 
A lista consome o espaço de acordo com a quantidade de valores
se tiver um bilhão de items vai tentar armazernar tudo... nada performatico.

Em python, podemos usar geradores para contornar esse problema.
'''

def generateNoPerformance():
    r = []
    for n in range(100):
        r.append(n)
        time.sleep(0.1)

    return r

# g = generateNoPerformance()
# Tomaria muito tempo


'''
Caso eu queira usa a função geradora para gerar um elemento por vez, fariamos assim: 

A vantagem é que ela gera um valor por vez (é um iterável), sem esperar todos os valores.
Fazendo o que se chama lazy evaluation: avaliação preguiçosa.
'''

def generateWithPerformance():
    for n in range(100):
        yield n
        time.sleep(0.1)

g = generateWithPerformance()

for v in g:
    print(v)

print('iterador is iter', hasattr(g, '__iter__'))
print('iterador', hasattr(g, '__next__'))

