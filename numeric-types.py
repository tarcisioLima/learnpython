from decimal import Decimal

numero = 5 # Criação da variável numero

print(type(numero)) # Exibindo o tipo da variável
# que será int

altura = 1.79 # Declaração da variável altura

print(type(altura)) # Impressão do tipo da variável "altura"

dc = Decimal("0.1")
print(dc)

# Numeros complexos
comp = 1j * 1J

print('comp', type(comp))

var1 = True
var2 = False

print(type(var1))
print(type(var2))

# No Python, quando comparado com True o número 1 retorna true 
# e todos os demais retornam false
s = 1

if s == True:
    print("true")
else:
    print("false")