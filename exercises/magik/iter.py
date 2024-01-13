class SequenceIterable:

    def __init__(self, some_list):
        self.some_list = some_list
        self.index = 0
        self.sq = False

    def __iter__(self):
        return self       

    def __next__(self):
        if self.index >= len(self.some_list) and self.sq is True:
            self.index = 0 
            raise StopIteration
        item = self.some_list[self.index]
        self.index += 2
        return item

        

container = SequenceIterable([1, 5, 4, 6, 43, True, 'hello'])
for i in container:
    print(i)
