class SequenceIterable:

    def __init__(self, some_list):
        self.some_list = some_list
        self.current = 0

    def __iter__(self):
        return self
    
    def __next__(self):
        item = None
        if self.current < len(self.some_list):
            item = self.some_list[self.current]
            self.current += 1
            return item
        else:
            raise StopIteration
        

container = SequenceIterable([1, 5, 4, 6, 43, True, 'hello'])
for i in container:
    print(i)
