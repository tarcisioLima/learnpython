# Getter obtem um valor
# Setter fixa um valor

# Eles são como uma proteção para o atributo.
class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def discount(self, percent):
        self.price = self.price - (self.price * (percent / 100))

    # Getter: por convenção usar um self._NOMEVARIAVEL para não dar problema
    @property
    def price(self):
        return self._price

    # Setter
    @price.setter
    def price(self, value):
        if isinstance(value, str):
            value = float(value.replace('R$', ''))
        self._price = value

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value.lower()
