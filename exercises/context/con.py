# Context manager class
class ConManager:

    def __init__(self, some_string):
        self.some_string = some_string

    def __enter__(self):
        print('enter')
        return self.some_string

    def __exit__(self, exc_type, exc_val, exc_tb):
        print('exit')


some_string = 'hehe'


def get_manager(some_string):
    return ConManager(some_string)


with get_manager(some_string) as m:
    print('inside context')
    print(m)

# operator with looking for __enter__ and __exit__
# open function return TextIOWrapper object that has __enter__ and __exit__
with open('file.txt') as f:
    data = f.read()
