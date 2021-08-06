'''
Módulos padrão do Python: são arquivos .py (que contém código python) e servem para expandir
as funcionalidades padrão da linguagem. Veja todos os módulos padrão do Python em:
https://docs.python.org/3.11/py-modindex.html
'''

# import sys
'''importa o módulo inteiro'''

# from sys import platform
''' importa só uma coisa '''

from sys import platform as p
''' importa uma coisa com apelido '''

from random import randint

# from random import *
''' importa TUDO do módulo, mas é perigoso porque pode dar colisão muito facilmente '''
''' OBS: Tomar cuidado para não sobreescrever modulos padrão'''

# from random import randint, random
''' Para adicionar mais de módulo '''

print(p)

for i in range(10):
    print('Número aleatório entre 0 e 10: ', randint(0, 10))


# Importando modulo próprio, ao importa-lo, tudo que está dentro dele será executado
import calcs

'''
 O __name__ do arquivo que está sendo chamado sempre é "main".
'''
print('modules: ', __name__)
print('PI: ', calcs.PI)
