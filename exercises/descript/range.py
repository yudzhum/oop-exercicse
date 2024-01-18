class RangeValidator:
    
    def __init__(self, min_temp, max_temp):
        self.min_temp = min_temp
        self.max_temp = max_temp

    def __set_name__(self, owner, name):
        print(f'__set_name__ called: owner={owner}, attr_name={name}')
        self.attribute_name = name

    def __set__(self, instance, value):

        print(instance, value)
        if not isinstance(value, (int, float)):
            raise TypeError('Неправильный тип данных')
        if value < self.min_temp or value > self.max_temp:
            raise ValueError(f"Значение должно быть между {self.min_temp} и {self.max_temp}")
        instance.__dict__[self.attribute_name] = value

    def __get__(self, instance, owner_class):
        if instance is None:
            return self
        else:
            # f'calling __get__ for {self.attribute_name}')
            return instance.__dict__.get(self.attribute_name, None)



class Temperature:
    celsius = RangeValidator(-273.15, 1000)


temp = Temperature()
print('create exemp temp', temp.__dict__)
try:
    temp.celsius = [1, 2]
    print(temp.celsius)
except TypeError as ex:
    print(ex)