from dataclasses import dataclass


@dataclass
class Klass:
    pass


# Реализуйте функцию to_Klass(), которая принимает на вход cловарь и возвращает объект типа Klass такой же структуры.
# В пайтоне классы созданные лишь для хранения значений принято оборачивать в декоратор @dataclass
# А чтобы не конфликтовать с зарезервированным именем class принято именовать через k
def to_Klass(data):

    klass = Klass()
    for key, value in data.items():
        setattr(klass, key, value)
    return klass


def test_to_Klass():
    data = {'key': 'value', 'key2': 'value2'}
    std = to_Klass(data)
    assert std.key == 'value'
    assert std.key2 == 'value2'
    print(std.key2)

    data2 = {'keysdd': 'vasdfalue', 'kasdfey2': 'asdvalue2'}
    std = to_Klass(data2)
    assert std.keysdd == 'vasdfalue'
    assert std.kasdfey2 == 'asdvalue2'

test_to_Klass()
