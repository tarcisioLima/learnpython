''' 
Na linguagem Python temos a seguinte separação 
entre os diferentes tipos de operadores:

Operadores aritméticos
Operadores de atribuição
Operadores de comparação
Operadores lógicos
Operadores de identidade
Operadores de associação
A seguir veremos cada um deles.
''' 


# Operadores Aritiméticos


numero_1 = 5
numero_2 = 2

soma = numero_1 + numero_2
subtracao = numero_1 - numero_2
multiplicacao = numero_1 * numero_2
divisao = numero_1 / numero_2
divisao_inteira = numero_1 // numero_2
modulo = numero_1 % numero_2
exponenciacao = numero_1 ** numero_2

print(soma) # 7
print(subtracao) # 3
print(multiplicacao)  # 10
print(divisao) # 2.5
print(divisao_inteira) # 2
print(modulo)  # 1
print(exponenciacao) # 25

print((2 + 5) * 3) # O resultado será 21

'''
Operadores de atribuição
Os operadores de atribuição atribuem valor a uma variável. Na Tabela 2 temos uma lista desses operadores.

Operador	Exemplo	      Equivalente a
=	        x = 1	        x = 1
+=	      x += 1	      x = x + 1
-=	      x -= 1	      x = x - 1
*=	      x *= 1	      x = x * 1
/=	      x /= 1	      x = x / 1
%=	      x %= 1	      x = x % 1
'''

# Operadores de comparação em python são como as demais linguagens, a saber:

'''
Operador	             Conceito	                                          Exemplo
>(Maior que)	          Verifica se um valor é maior que outro	          x > 5
<(Menor que)	          Verifica se um valor é menor que outro	          x < 5
== (Igual a)	          Verifica se um valor é igual a outro	            x == 5
!= (Diferente de)	      Verifica se um valor é diferente de outro	        x != 5
>= (Maior ou igual a)	  Verifica se um valor é maior ou igual a outro	x   >= 5
<= (Menor ou igual a)	  Verifica se um valor é menor ou igual a outro	x   <= 5
'''
numero_1 = 2
numero_2 = 4

soma = numero_1 + numero_2

if soma < 10:
    print("soma não é maior que 10")
else:
    print("soma é maior ou igual a 10")


# Operadores lógicos
'''
Os operadores lógicos são usados para unir duas ou mais expressões 
condicionais. Isso é feito por meio de conectivos

Operador	    Conceito	                                                                            Exemplo
and	          Retorna True se todas as condições forem verdadeiras, caso contrário retorna False	  x > 1 and x < 5
or	          Retorna True se uma das condições for verdadeiras, caso contrário retorna False	      x > 1 or x < 5
not	          Inverte o resultado: se o resultado da expressão for True, o operador retorna false	  not(x > 1 and x < 5)

'''

idade_lucas = 21
idade_carolina = 19

# OPERADOR OR
if idade_lucas >= 18 or idade_carolina >= 18:
    print("Pelo menos um dos dois é maior de idade")
else:
    print("Lucas e Carolina não são maiores de idade")

# OPERADOR AND
if idade_lucas >= 18 and idade_carolina >= 18:
    print("Lucas e Carolina são maiores de idade")
else:
    print("Pelo menos um dos dois não é maior de idade")

# Operadores de identidade
'''
Os operadores de identidade servem para a comparação de objetos. 
Nessa comparação é verificado se eles ocupam a mesma posição na memória, 
o que significará que se trata do mesmo objeto

Operador	        Conceito	                                                          Exemplo
is	              Retorna True se as variáveis comparadas forem o mesmo objeto	      nome is ‘Marcos’
is not	          Retorna True se as variáveis comparadas não forem o mesmo objeto	  x is not ‘Python’
'''

time_carlos = 'Botafogo'
time_luciano = 'Flamengo'
time_fabricia = 'Botafogo'

if time_carlos is time_luciano:
    print("time_carlos - time_luciano = mesmo objeto")
else:
    print("time_carlos - time_luciano = objetos diferentes")

if time_carlos is time_fabricia:
    print("time_carlos - time_fabricia = mesmo objeto")
else:
    print("time_carlos - time_fabricia = objetos diferentes")

# Operadores de associação
'''
Os operadores de associação são utilizados para verificar se uma sequência 
contém um objeto.

Operador	    Conceito	                                                  Exemplo
in	          Retorna True caso o valor seja encontrado na sequência	    2 in x
not in	      Retorna True caso o valor não seja encontrado na sequência	2 not in x
'''
frutas = ["banana","laranja","uva","ameixa"]

fruta_1 = "ameixa"
fruta_2 = "melancia"

print(fruta_1 in frutas) # True
print(fruta_2 in frutas) # False
