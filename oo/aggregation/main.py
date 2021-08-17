'''
 Uma classe usa outra classe e essa precisa da outra para funcionar direito.
 Um Carro pode exister sem as rodas, mas não funciona direito sem elas, isso seria um exemplo de associação.
'''

from classes import BuyCar, Product

carrinho = BuyCar()

p1 = Product('Shirt', 50)
p2 = Product('Notebook', 5000)
p3 = Product('Joystick', 30)

carrinho.insert_product(p1)
carrinho.insert_product(p1)
carrinho.insert_product(p2)
carrinho.insert_product(p3)

carrinho.list_product()
print('SOMA TOTAL: ', carrinho.total_sum())

