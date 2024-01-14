class Transport:

    def __init__(self, brand, max_speed, kind=None):
        self.brand = brand
        self.max_speed = max_speed
        self.kind = kind

    def __str__(self):
        return (f'Тип транспорта {self.kind} марки {self.brand}'
                f'может развить скорость {self.max_speed} км/ч')
    

class Car(Transport):

    def __init__(self, brand, max_speed, mileage, gasoline_residue):
        super().__init__(brand, max_speed, kind='Car')
        self.mileage = mileage
        self.__gasoline_residue = gasoline_residue

    @property
    def gasoline_residue(self):
        return f'Осталось бензина {self.__gasoline_residue} л'
    
    @gasoline_residue.setter
    def gasoline_residue(self, level):
        if not isinstance(level, int):
            print('Ошибка заправки автомобиля')
        

