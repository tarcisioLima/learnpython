import sales.calc_price
from sales.formatter.price import real

''' Poderia importar assim também para reduzir o tamanho '''

# from sales import calc_price
# from sales.calc_price import increase

price = 49.90
percent = 15
price_incremented = sales.calc_price.increase(value=price, percent=percent, formatx=True)
price_decremented = sales.calc_price.decrease(value=price, percent=percent, formatx=True)

print(f'Valor {real(price)} incrementado em {percent}% fica: ', price_incremented)
print(f'Valor {real(price)} decrementado em {percent}% fica: ', price_decremented)