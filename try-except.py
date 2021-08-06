# Exceções são erros que param a executação do programa.

'''
Esse exemplo abaixo é a forma mais simples e ampla de tratar exceções: os devs costumam dizer
que não é uma boa prática de programação.
'''
try:
    print(a)
except:
    print('erro')

''' O ideal seria delimitar o tipo de exceção que estou querendo tratar '''

try:
    a = {}
    print(a[1])
except NameError as error:
    print('Erro: ', error)
except (IndexError, KeyError) as error: # Caso queira tratar duas exceções no mesmo except.
    print('Erro de índice ou chave: ', error)
except Exception as error:
    print('Ocorreu um erro inesperado: ', error)
else:
    print('O código foi executado com sucesso')
finally:
    print('Finalmente')
    a = None


''' O else é executado sempre que o bloco do try não lançar nenhuma execeção '''
''' O finally é executado sempre '''

# Podemos criar try e except dentro de outro try except sucessivamente.
# Porém daí ele não vai deixar propagar para o except de fora.

print('Bora continuar...', a)

# É possivel criar nossas próprias exceções.... veremos na parte de orientação a objetos.