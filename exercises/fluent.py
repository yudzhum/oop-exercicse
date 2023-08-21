raw = [{'name': 'istambul', 'country': 'turkey'},
       {'name': 'Moscow ', 'country': ' Russia'},
       {'name': 'iStambul', 'country': 'tUrkey'},
       {'name': 'antalia', 'country': 'turkeY '},
       {'name': 'samarA', 'country': '  ruSsiA'}]


from functools import reduce as _reduce


class Collection:
    def __init__(self, iterable):
        self.iterable = iterable

    def map_(self, func):
        return Collection(list(map(func, self.iterable)))

    def filter_(self, func):
        return Collection(list(filter(func, self.iterable)))

    def reduce_(self, func, acc=None):
        return Collection([_reduce(func, self.iterable, acc)])

    # возвращает коллекцию с уникальными значениями
    def unique(self):
        tuples = set(tuple(sorted(d.items())) for d in self.iterable)
        return Collection(list(dict(t) for t in tuples))

    # группирует коллекцию по указаному ключу
    def group_by(self, func):
        def reducer(acc, val):
            key, value = func(val)
            if key not in acc:
                acc[key] = []
            acc[key].append(value)
            return acc
        result_dict = _reduce(reducer, self.iterable, {})
        return Collection([{k: v} for k, v in result_dict.items()])

    # сортирует колекцию по ключу
    def sort_by(self, func):
        return Collection(sorted(self.iterable, key=func))

    def print(self):
        print(self.iterable)
        return Collection(self.iterable)

    def all(self):
        return list(self.iterable)
    

def _normalise(row):
    return {'name': row['name'].lower().strip(), 'country': row['country'].lower().strip()}

def format(data):
    c = Collection(data)
    return c.map_(_normalise) \
        .unique() \
        .group_by(lambda row: (row['country'], row['name'])) \
        .map_(lambda row: {key: sorted(values) for key, values in row.items()}) \
        .print() \
        .sort_by(lambda row: list(row.keys())) \
        .all()
