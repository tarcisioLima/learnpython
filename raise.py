'''
a palavra raise, lança a exceção a frente...
'''

def divide(n1, n2):
    try:
        return n1/n2
    except ZeroDivisionError as error:
        print('Log: ', error)
        raise
        return False

try:
    print(divide(5, 0))
except ZeroDivisionError as error:
    print('Erro: ', error)


'''
Caso de tratar exceção
'''

def divideImproved(n1, n2):
    if n2 == 0:
        raise ValueError("N2 não pode ser 0")
    return n1 / n2

try:
    print('Divide improved: ', divideImproved(5, 0))
except ValueError as error:
    print(error)

