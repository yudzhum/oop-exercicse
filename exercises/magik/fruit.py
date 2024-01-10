class Fruit:

    def __init__(self, name, price):
        self.name = name
        self.price = price

    def __eq__(self, other):   
        other_price = self.get_price_or_number(other)
        return self.price == other_price
    
    def __lt__(self, other):
        other_price = self.get_price_or_number(other)
        return self.price < other_price
    
    def __le__(self, other):
        other_price = self.get_price_or_number(other)
        return self.price <= other_price
    
    def __gt__(self, other):
        other_price = self.get_price_or_number(other)
        return self.price > other_price
    
    def __ge__(self, other):
        other_price = self.get_price_or_number(other)
        return self.price >= other_price
        
    @staticmethod
    def get_price_or_number(other):
        if isinstance(other, Fruit):
            return other.price
        return other
    

apple = Fruit("Apple", 0.5)
orange = Fruit("Orange", 1)
banana = Fruit("Banana", 1.6)
lime = Fruit("Lime", 1.0)

assert (banana > 1.2) is True
assert (banana >= 1.2) is True
assert (banana == 1.2) is False
assert (banana != 1.2) is True
assert (banana < 1.2) is False
assert (banana <= 1.2) is False

assert (apple > orange) is False
assert (apple >= orange) is False
assert (apple == orange) is False
assert (apple != orange) is True
assert (apple < orange) is True
assert (apple <= orange) is True

assert (orange == lime) is True
assert (orange != lime) is False
assert (orange > lime) is False
assert (orange < lime) is False
assert (orange <= lime) is True
assert (orange >= lime) is True
print('Good')