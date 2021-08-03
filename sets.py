"""
 Operações: add (adiciona), update (atualiza), clear, discard

 A maior diferença entre os sets e as listas ou tuplas é que o sets só suportam elementos únicos.
"""

# Muito semelhante aos dicionários, mas não têm chaves, só valores imutáveis.
s1 = {1, 2, 3, 4, 5}
# Ou
s2 = set()

s2.add('Python')
s2.add('CSS')
s2.add('Javascript')

s2.discard('CSS')

s2.update([1, 2, 3])

print('s1', s1)
print('s2', s2)

# A gente pode usar sets para eliminar elementos duplicados duma lista
l1 = [1, 2, 1, 1, 3, 4, 5, 6, 6, 6, 6, 7, 8, 9, 'Luiz', 'Luiz']
l1 = set(l1)
l1 = list(l1)

print('l1', l1)

"""
Funções legais de usar com sets:

union | = une
intersection & = (todos os elementos presentes nos dois sets)
difference - = (elementos apenas no set da esquerda)
symmetric_difference ^ = (Elementos que estão nos dois sets, mas não em ambos)
"""
set1 = {1, 2, 3, 4, 5, 7}
set2 = {1, 2, 3, 4, 5, 6}

s3 = set1 | set2
s4 = set1 & set2
s5 = set1 - set2 # Pega só da esquerda (um elemento que não esteja nos dois conjuntos, apenas no da esquerda)
s6 = set1 ^ set2
print('union ', s3)
print('intersection ', s4)
print('difference', s5)
print('symmetric_difference', s6)