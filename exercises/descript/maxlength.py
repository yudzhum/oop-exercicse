class MaxLengthAttribute:

    def __get__(self, instance, owner_class):
        if instance is None:
            return self
        else:
            return max(instance.__dict__, key=len, default=None)



class MyClass:
    max_length_attribute = MaxLengthAttribute()


obj = MyClass()
obj.name = "Vasiliy"
obj.city = "Saint Peterburg"
obj.country = "Rus"
print(obj.max_length_attribute)