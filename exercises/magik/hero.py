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
    
    def __add__(self, other):
        if type(other) is int:
            up_values = tuple(value + other for value in self.values)
            return __class__(*up_values)
        elif isinstance(other, Vector):
            if len(self.values) == len(other.values):
                new_values = [self.values[i] + other.values[i] for i in range(len(self.values))]
                return __class__(*new_values)
            return f'Сложение векторов разной длины недопустимо'
        else:
            print(f'Вектор нельзя сложить с {other}')
                    

    def __mul__(self, other):
        if type(other) is int:
            up_values = tuple(value * other for value in self.values)
            return __class__(*up_values)
        elif isinstance(other, Vector):
            if len(self.values) == len(other.values):
                new_values = [self.values[i] * other.values[i] for i in range(len(self.values))]
                return __class__(*new_values)
            return f'Умножение векторов разной длины недопустимо'
        else:
            print(f'Вектор нельзя умножать с {other}')
    
    


v1 = Vector(1,2,3)
print(v1) # печатает "Вектор(1, 2, 3)"

v2 = Vector(3,4,5)
print(v2) # печатает "Вектор(3, 4, 5)"
v3 = v1 + v2
print(v3) # печатает "Вектор(4, 6, 8)"
v4 = v3 + 5
print(v4) # печатает "Вектор(9, 11, 13)"
v5 = v1 * 2
print(v5) # печатает "Вектор(2, 4, 6)"
v5 + 'hi' # печатает "Вектор нельзя сложить с hi"