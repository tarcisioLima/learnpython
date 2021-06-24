"""
 Entrada de dados
"""

name = input("What's your name? ")
age = input("What's your age? ")

""" Always will return string type """
print("Name type ", type(name))

birth_date = 2021 - int(age)

print(f"{name} was born in {birth_date}")

n1 = int(input('Type a number: '))
n2 = int(input('Type other numer: '))

print(n1+n2)
