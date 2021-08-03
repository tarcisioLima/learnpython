# Três dentre as coleções mais utilizadas em Python, 
# que são as listas, tuplas e dicionários.

'''Listas: Lista é uma coleção de valores indexada, 
em que cada valor é identificado por um índice. 
O primeiro item na lista está no índice 0, 
o segundo no índice 1 e assim por diante.'''

programadores = ['Victor', 'Juliana', 'Samuel', 'Caio', 'Luana']
print(type(programadores)) # type ‘list’
print(len(programadores)) # 5
print(programadores[4]) # Luana
print(programadores)

programadores[1] = 'Carolina'
print(programadores) # ['Victor', 'Carolina', 'Samuel', 'Caio', 'Luana']

# append adiciona elementos no final de uma lista
programadores.append('Renato')
print(programadores)

programadores.insert(1, 'Rafael')

print(programadores)

'''remove() para a remoção pelo valor informado no parâmetro, 
e pop() para remoção pelo índice do elemento na lista'''
programadores.remove('Victor')

print(programadores)
programadores.insert(0, 'Victor')
programadores.pop(0)
print(programadores)

'''Outra característica das listas é que elas podem possuir diferentes tipos de 
elementos na sua composição. Isso quer dizer que 
podemos ter strings, booleanos, inteiros e outros tipos diferentes de 
objetos na mesma lista. '''

aluno = ['Murilo', 19, 1.79] # Nome, idade e altura
print(type(aluno)) # type 'list'


#Tuplas: Tupla é uma estrutura de dados semelhante a lista. 
# Porém, ela tem a característica de ser imutável, ou seja, 
# após uma tupla ser criada, ela não pode ser alterada.

times_rj = ('Botafogo', 'Flamengo', 'Fluminense', 'Vasco')
print(type(times_rj)) # class=’tuple’
print(times_rj) # ('Botafogo', 'Flamengo', 'Fluminense', 'Vasco')


'''
Uma observação a ser feita no uso de uma tupla é que se 
ela tiver um único item, é necessário colocar uma vírgula depois dele, 
pois caso contrário, o objeto que vamos obter é uma string, porque o valor 
do item é do tipo string;

lembre-se que as tuplas e as strings são sequências imutáveis
Tuplas devem ser usados para valores que não irão mudar, ex: dias da semana.
'''
objeto_string = ('tesoura')
objeto_tupla = ('tesoura',)

print(type(objeto_string)) # class 'str'
print(type(objeto_tupla)) # class 'tuple'

vogais = ('a', 'e', 'i', 'o', 'u')
print(vogais[1]) # e

# Funções para coleções: min() max(), sum(), len()
numeros = [15, 5, 0, 20, 10]
nomes = ['Caio', 'Alex', 'Renata', 'Patrícia', 'Bruno']
print(min(numeros)) # 0
print(max(numeros)) # 20
print(min(nomes)) # Alex
print(max(nomes)) # Renata

