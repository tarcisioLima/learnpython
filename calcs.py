import math

PI = math.pi


def double_list(listx):
    return [x * 2 for x in listx]

# o if abaixo não executa caso esse módulo esteja sendo importado por outro. (prático muito comum de se ver)


if __name__ == '__main__':
    print('double list: ', double_list([1,2,3,4]))
