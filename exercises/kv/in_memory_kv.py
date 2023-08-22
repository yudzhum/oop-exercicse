import copy


# InMemoryKV, который представляет собой in-memory key-value хранилище. 
# Данные внутри него хранятся в обычном словаре. 
# Интерфейс этого класса совпадает с FileKV за исключением __init__.py.
# Инициализатор InMemoryKV принимает на вход словарь, который становится начальным значением базы данных.
class InMemoryKV():

    def __init__(self, initial=None):
        if initial is None:
            self.map = {}
        self.map = copy.deepcopy(initial)

    def set_(self, key, value):
        self.map[key] = value

    def unset_(self, key):
        self.map.pop(key)

    def get_(self, key, default=None):
        return self.map.get(key, default)

    def to_dict(self):
        return copy.deepcopy(self.map)
