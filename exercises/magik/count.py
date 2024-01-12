class Countdown:
    """
    должен принимать начальное значение
    и вести обратный отсчет до нуля
    """

    # Start should be positive number
    def __init__(self, start):
        self.current = start if start > 0 else 0

    def __iter__(self):
        return self
    
    def __next__(self):
        if self.current >= 0:
            count = self.current
            self.current -= 1
            return count
        else:
            raise StopIteration


for i in Countdown(3):
    print(i)
