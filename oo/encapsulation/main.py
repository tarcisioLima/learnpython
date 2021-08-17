'''
Encapsulamento serve para proteger e esconder certas partes do nosso código (métodos e atributos da classe)
Outras linguagens de programação usam modificadores de acesso,
ex: public, protected (apenas dentro da classe e das filhas da classe), private (só disponível dentro da classe)
'''

from database import Database

bd = Database()

bd.insert_customer(1, 'Otávio')
bd.insert_customer(2, 'Miranda')
bd.insert_customer(3, 'Rose')
bd.delete_customer(2)

# Neste caso ele cria um novo valor dentro da instancia da classe,
# msm que já exista um valor lá com dois underlines __data
bd.__data = 'other thing' # Quando esse valor é setado, ele não altera o original, mas cria outro.

print(bd.__data) # Valor recem criado
print(bd._Database__data) # Valor original

print(bd.data) # Pelo Getter
# bd.data = 'Vai lançar erro: cant set attribute pois não tem setter na classe'
bd.list_customers()
