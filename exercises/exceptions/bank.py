class NegativeDepositError(Exception):
    pass


class InsufficientFundsError(Exception):
    pass


class BankAccount:
    def __init__(self, balance):
        self.balance = balance

    def deposit(self, number):
        if number < 0:
            raise NegativeDepositError("Нельзя пополнить счет отрицательным значением")
        self.balance = self.balance + number

    def withdraw(self, number):
        if self.balance - number < 0:
            raise InsufficientFundsError("Недостаточно средств для снятия")
        self.balance = self.balance - number