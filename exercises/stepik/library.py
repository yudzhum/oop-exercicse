class Library:

    def __init__(self, books: list):
        self.__books = books

    def __check_availability(self, book):
        if book in self.__books:
            return True
        return False
    
    def search_book(self, book):
        if self.__check_availability(book):
            return True
        return False
    
    def return_book(self, book):
        self.__books.append(book)

    def _checkout_book(self, book):
        if self.__check_availability(book):
            self.__books.remove(book)
            return True
        return False
    

library = Library(["War and Peace", "Moby-Dick", "Pride and Prejudice"])

assert library._Library__books == ["War and Peace", "Moby-Dick", "Pride and Prejudice"]
assert library.search_book("Moby-Dick") == True
assert library.search_book("Jane Air") == False

assert library._Library__check_availability("War and Peace") == True
assert library._checkout_book("Moby-Dick") == True
assert library._Library__books == ["War and Peace", "Pride and Prejudice"]

assert library.search_book("Moby-Dick") == False
assert library.return_book("Moby-Dick") is None
assert library._Library__books == ["War and Peace", "Pride and Prejudice", "Moby-Dick"]
assert library.search_book("Moby-Dick") == True
print('Good')