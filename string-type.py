nome = 'Daniel'
print(nome[0]) # D

# Há também a possibilidade de "fatiar" uma variável do tipo String, 
# retornando um "pedaço" dela.
print(nome[0:3]) # Dan

# Se começar com numero negativo, ele pega pelo fim da string.
print(nome[-1]) # e

# IMUTABILIDADE: Uma string no Python é uma sequência de caracteres imutável.
# Identidade no Python é o valor de referência do endereço de memória.

print(id(nome))

nome = 'Felipe'

print(id(nome))
print(nome)

# Também não é possível alterar o valor de uma determinada posição de uma string.
# nome[2] = 'a'  isso está errado!

nome_2 = 'Ana'
print(len(nome_2)) # 3

# Concatenação de Strings

sobrenome = 'Silva'

nome_completo = nome_2 + ' ' + sobrenome

print(nome_completo) # Ana Silva

# Comparação de Strings

n1 = 'Eduardo'
n2 = 'Eduardo'

if n1 == n2:
    print('iguais')
else:
    print('diferentes')

# Quando uma string é criada no Python, é aplicado o conceito de string interning.
# ela é armazenada num lugar da memória não sendo repetida em outro. 
# Todos os objetos que receberem o conteúdo dessa string apontarão para o mesmo 
# endereço de memória. Esse mecanismo diminui o consumo de memória.

if n1 is n2:
    print('iguais')
else:
    print('diferentes')

# Principais métodos de Strings
# Os métodos de string retornam novos valores, mas não alteram a string original.

mensagem = 'string no Java'

# Com o método find() podemos procurar uma substring 
# dentro de uma string e retornar a posição onde ela foi encontrada 

print(mensagem.find('Java')) # 10

# Com replace() é utilizado para substituir ocorrências de substrings 
# dentro de uma string
nova_mensagem = mensagem.replace('Java', 'Python')
print(nova_mensagem) # Quero aprender Python! Na DevMedia tem salas de Python para aprender essa linguagem

mensagem2 = 'Estou aprendendo Python na DevMedia'

lista_mensagem2 = mensagem2.split(' ')

print(type(lista_mensagem2)) # type 'list'
print(lista_mensagem2) # ['Estou', 'aprendendo', 'Python', 'na', 'DevMedia']

# outros métodos: upper, lower 

