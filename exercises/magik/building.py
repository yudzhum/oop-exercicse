class Building:
    """
    создавать здание определенной этажности 
    и уметь бронировать за компанией определенный этаж в здании.
    """
    
    def __init__(self, levels):
        self.levels = [None] * levels

    def __setitem__(self, key, value):
        if 0 <= key <= len(self.levels):
            self.levels[key] = value
        else:
            raise IndexError
        
    def __getitem__(self, item):
        if 0 <= item <= len(self.levels):
            return self.levels[item]
        else:
            raise IndexError
        
    def __delitem__(self, key):
        if 0 <= key <= len(self.levels):
            del self.levels[key]
        else: 
            raise IndexError


iron_building = Building(22)  # Создаем здание с 22 этажами
iron_building[0] = 'Reception'
iron_building[1] = 'Oscorp Industries'
iron_building[2] = 'Stark Industries'
print(iron_building[2])
del iron_building[2]
print(iron_building[2])