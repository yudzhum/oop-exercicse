class AttributeChecker:

    def __contains__(self, attr):
        if attr in self.__dict__:
            return True
        return False


# Проверки для класса AttributeChecker

# Тест 1: Проверка наличия отсутствующего атрибута
check = AttributeChecker()
print(check.__dict__)
assert "name" not in check
assert "age" not in check
setattr(check, 'name', 'Russell')
check.age = 10
print(check.__dict__)

# Тест 2: Проверка добавления атрибутов
assert "name" in check
assert "age" in check

# Тест 3: Проверка атрибутов другого ЭК
check_2 = AttributeChecker()
assert "name" not in check_2
assert "age" not in check_2


# Тест 4: Проверка наличия атрибутов после удаления
delattr(check, "name")
assert "name" not in check
assert "age" in check

print("Good")