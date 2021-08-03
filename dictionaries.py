# Dicionários em python são como em javascript: { chave: 'valor' }
import copy

dados_cliente = {
    'Nome': 'Renan',
    'Endereco': 'Rua Cruzeiro do Sul',
    'Telefone': '982503645'
}

print(dados_cliente['Nome']) # Renan
print(dados_cliente)

# Nas listas e tuplas acessamos os dados por meio dos índices.
# Já nos dicionários, o acesso aos dados é feito por meio da chave associada a eles.

# Exemplo adição de nova chave
dados_cliente['Idade'] = 40
# ou
dados_cliente.update({ 'nkey': 1})

print(dados_cliente)

# Para remover um item do dicionário, podemos usar o método pop(), como vemos
dados_cliente.pop('Telefone', None)
print(dados_cliente)

# or
del dados_cliente['Idade']

print(dados_cliente)

# Outra forma de criar dicionários.
d1 = dict(key1='value', k2='val')

print('d1', d1)

d2 = {'key': 'v1', 'key': 'v2', 'key': 'valor real da chave', 1: 'Ae'}

print('d2', d2)

# Strings, números e tuplas podem ser usados como chave do dicionário
# a gente pode acessar um valor usando dicionario.get('chave')), caso não exista a chave, ele retorna None.

# Checar se existe a chave
print('key' in d2)

# Checar se existe o valor
print('Ae' in d2.values())

# Saber quantos pares de chave valor existem
print(len(d2))

# Interar no dicionário

d3 = {
    'k1': 'val1',
    'k2': 'val2',
    'k3': 'val3',
}

# Por padrão, ele pega a chave no iterador, por isso devemos usar .values() ou .items() para pegar o valor
for k in d3:
    print('HERE: ', k)

for v in d3.values():
    print(v)

for k, v in d3.items():
    print(k, v)

customers = {
    'customer1': {
        'name': 'Dani',
        'middlename': 'Oliver',
    },
    'customer2': {
        'name': 'Tarcisio',
        'middlename': 'Lima',
    }
}

for ck, cv in customers.items():
    print(f'Exibindo {ck}')
    for dk, dv in cv.items():
        print(f'{dk} = {dv}')


d4 = { 1: 'a', 2: 'b',  3: 'c', 'd': ['John', 'Patrick', 'Christian']}
v = d4

v[1] = 'Teste'

# O código acima irá alterar tanto v quanto d4
# Porque o sinal de igual não cria um novo objeto, apenas apontam para mesma localização.

print('d4', d4)
print('v', v)

# Para fazer uma cópia rasa (shallow: não é copiado todos os atributos):
v = d4.copy()

print('v', v)

v[1] = 'just me'
v['d'][0] = 'Walter'

print(v['d'][0])

print('d4', d4)
print('v', v)

print('############# NEW TEST #############')


# Para fazer uma cópia real é preciso usar o modulo copy
x = copy.deepcopy(d4)
x['d'][0] = 'Gospel'

print('d4',  d4)
print('deep copy', x)

# Funções de dicionario
d5 = {
    1: 2,
    2: 3,
    4: 5
}
# Remover específico
d5.pop(4)

# d5.popitem() <- deleta o último item sempre
print('d5', d5)

# concatenar dicionários
d5.update(d2)

print('concated d5 with d2', d5)