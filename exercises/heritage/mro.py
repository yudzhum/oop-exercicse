class First(object):
    def __init__(self):
        print("First(): entering")
        # go to the object class but MRO says it to early,
        # so before that, detour to the Second
        super(First, self).__init__()
        print("First(): exiting")


class Second(object):
    def __init__(self):
        print("Second(): entering")
        super(Second, self).__init__()
        print("Second(): exiting")


class Third(First, Second):
    def __init__(self):
        print("Third(): entering")
        #go to the First
        super(Third, self).__init__()
        print("Third(): exiting")

Third()
print(Third.__mro__)

# Third(): entering
# First(): entering
# Second(): entering
# Second(): exiting
# First(): exiting
# Third(): exiting