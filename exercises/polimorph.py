class Node:
    def __init__(self, value, node=None):
        self.next = node
        self.value = value

    def get_next(self):
        return self.next

    def get_value(self):
        return self.value

    def __repr__(self):
        acc = []
        current = self
        while current is not None:
            acc.append(current.get_value())
            current = current.get_next()
        return str(tuple(acc))
    
    def reverse(self):
        acc = []
        current = self
        while current is not None:
            acc.append(current.get_value())
            current = current.get_next()
        return str(tuple(acc.reverse()))


def reverse(list):
    reversed_list = None
    current = list

    while current:
        reversed_list = Node(current.get_value(), reversed_list)
        current = current.get_next()

    return reversed_list
