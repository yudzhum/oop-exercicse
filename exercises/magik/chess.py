class ChessPlayer:

    def __init__(self, name, surname, rating):
        self.name = name
        self.surname = surname
        self.rating = rating

    def __eq__(self, other):
        if self.is_number_or_rating(other):
            return self.rating == other
        return 'Невозможно выполнить сравнение'
    
    def __gt__(self, other):
        if self.is_number_or_rating(other):
            return self.rating > other
        return 'Невозможно выполнить сравнение'
    
    def __lt__(self, other):
        if self.is_number_or_rating(other):
            return self.rating < other
        return 'Невозможно выполнить сравнение'
    
    @staticmethod
    def is_number_or_rating(other):
        if isinstance(other, ChessPlayer):
            return True
        elif isinstance(other, int):
            return True
        return False