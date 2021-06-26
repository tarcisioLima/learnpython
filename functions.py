"""
Functions
"""


def say_hi(msg='Hello', name='John'):
    print(msg, name)


say_hi()
say_hi('Olá', 'Dani')
say_hi(name='Ines', msg='Saint')


def division(n1, n2):
    if n2 > 0:
        return n1 / n2


print('Division: ', division(10, 2))
print('Division: ', division(10, 0))


def func(*args):
    args = list(args)
    args[0] = 20
    print(args)
    print(args[1])
    print(len(args))


lists = [1, 2, 3, 4, 5]

print(*lists, sep='-')

func(6, 7, 8, 9, 10)

list_1 = ['a', 'b', 'c']
list_2 = ['e', 'f', 'g']


def foo(*args, **kwargs):
    print(args)
    name = kwargs.get('name')

    if name is not None:
        print('name: ', name)
    else:
        print('name not informed')


"""
kwargs = get named args
"""
foo(*list_1, *list_2, name='Dani')
