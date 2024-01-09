class Vector:

    def __init__(self, *args):
        values = []
        for value in args:
            # type because of bool values
            if type(value) == int:
                values.append(value)
        self.values = sorted(values)

    def __str__(self):
        if self.values:
            return f'Вектор{tuple(self.values)}'
        return 'Пустой вектор'
    

v1 = Vector(1, 2, 3)
print('v1', v1)
assert isinstance(v1, Vector)
assert str(v1) == 'Вектор(1, 2, 3)'

v2 = Vector()
assert isinstance(v2, Vector)
assert str(v2) == 'Пустой вектор'

v3 = Vector([4, 5], 'hello', 3, -1.5, 1, 2)
print('v3', v3)
assert isinstance(v3, Vector)
assert sorted(v3.values) == [1, 2, 3]
assert str(v3) == 'Вектор(1, 2, 3)'

v4 = Vector([4, 5], 'hello')
assert str(v2) == 'Пустой вектор'
assert v2.values == []

v5 = Vector(1, 2, True)
print(v5)
assert isinstance(v5, Vector)
assert str(v5) == 'Вектор(1, 2)'

print(v1)
print(v2)
print(v3)
print(v4)