class Bed:

    def __init__(self, price):
        self.__price = price

    def get_price(self):
        return self.__price

    def set_price(self, new_price):
        if new_price > 0 and isinstance(new_price, float):
            self.__price = new_price
        else:
            print('Valor no valido')

    price = property(get_price, set_price)

class House:
    
    def __init__(self, price):
        self.__price = price

    @property
    def price(self):
        return self.__price

    @price.setter
    def set_price(self, new_price):
        if new_price > 0 and isinstance(new_price, float):
            self.__price = new_price
        else:
            print('Valor no valido')

    @price.deleter
    def del_price(self):
        del self.__price

bed = Bed(4000.0)
# bed.__price 
print(bed.price)
bed.price = 5000.0
print(bed.price)

house = House(4000.0)
print(house.price)
house.set_price = 5000.0
print(house.price)

