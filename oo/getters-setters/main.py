from product import Product

p1 = Product('MACBOOK', 10000)
p1.discount(15)
print(f'{p1.name}:', p1.price)

p2 = Product('CANECA', 'R$30')
p2.discount(10)
print(f'{p2.name}:', p2.price)
