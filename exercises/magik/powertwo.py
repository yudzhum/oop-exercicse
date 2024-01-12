class PowerTwo:

    def __init__(self, end_power):
        self.two = 2
        self.cur_power = 0
        self.end_power = end_power

    def __iter__(self):
        return self
    
    def __next__(self):
        if self.cur_power <= self.end_power:
            res = self.two ** self.cur_power
            self.cur_power += 1
            return res
        else:
            raise StopIteration
        

for i in PowerTwo(4): # итерируемся до 4й степени двойки
    print(i)

numbers = PowerTwo(2)

assert hasattr(numbers, '__next__') is True
assert hasattr(numbers, '__iter__') is True

iterator = iter(numbers)
print('Элементы итератора PowerTwo(2)')
print(next(iterator))
print(next(iterator))
print(next(iterator))
try:
    print(next(iterator))
    raise ValueError('Не реализовали StopIteration')
except StopIteration:
    pass

print('-' * 15) 
print('Элементы итератора PowerTwo(20)')
for i in PowerTwo(20):
    print(i)