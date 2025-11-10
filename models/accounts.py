class BankAccount:
    def __init__(self, name=None, balance=0.0):
        self._balance = 0.0
        self.balance = balance
        self.name = name

    @property
    def balance(self):
        return self._balance

    @balance.setter
    def balance(self, amount):
        if amount < 0:
            raise ValueError('Balance cannot be negative')
        self._balance = amount

    def deposit(self, amount):
        if amount <= 0:
            raise ValueError('Deposit amount must be positive')
        self.balance += amount

    def withdraw(self, amount):
        if amount <= 0:
            raise ValueError('Withdrawal amount must be positive')
        if amount > self.balance:
            raise ValueError('Insufficient funds')
        self.balance -= amount
