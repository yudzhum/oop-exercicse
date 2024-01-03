class Counter:

    def start_from(self, start=0):
        self.current = start

    def increment(self):
        self.current += 1

    def display(self):
        print(f'Текущее значение счетчика = {self.current}')

    def reset(self):
        self.current = 0


c1 = Counter()
c2 = Counter()

assert isinstance(c1, Counter)
assert isinstance(c2, Counter)
assert c1.__dict__ == {}
assert c2.__dict__ == {}

c1.start_from(45)
assert len(c1.__dict__) == 1
c1.increment()
c1.display()  # печатает 46
c1.increment()
c1.display()  # печатает 47