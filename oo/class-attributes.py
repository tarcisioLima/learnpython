
class A:
    vc = 123

    # Inicializa logo quando instancia, caso não seja instanciado, não altera a variavel da classe.
    def __init__(self):
        self.vc = 111

a1 = A()
a2 = A()

# Muda para todas as instancias
A.vc = 321

# Muda apenas para a instancia
a1.vc = 9090

# R: {'vc': 9090}
print(a1.__dict__)
# R: {'vc': 111}
print(a2.__dict__)

'''
Primeiro o compilador do python vai procurar na instancia, 
se ele n encontra na instancia, ele procura na classe.
'''

print(A.__dict__)

print()

print(a1.vc)
print(a2.vc)
print(A.vc)