class FibonacciIterator:

    def __init__(self, n):
        self.n = n
        self.cur = 1
        self.fib1 = 0
        self.fib2 = 1

    def __iter__(self):
        return self
    
    def __next__(self):
        if self.cur <= self.n:
            fib = self.fib1
            self.fib1, self.fib2 = self.fib2, self.fib1 + self.fib2
            self.cur += 1
            return fib
        raise StopIteration


fibonacci_iter = FibonacciIterator(7)

for number in fibonacci_iter:
    print(number)
