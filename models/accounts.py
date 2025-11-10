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


class CreditCard:
    def __init__(self, name=None, limit=0.0, current_debt=0.0, due_day=None, bank_account=None):
        self.name = name
        self.limit = limit
        self.current_debt = current_debt
        self.due_day = due_day
        self.bank_account = bank_account

    def purchase(self, amount):
        if amount <= 0:
            raise ValueError('Purchase amount must be positive')
        available = self.limit - self.current_debt
        if amount > available:
            raise ValueError('Purchase exceeds available credit')
        self.current_debt += amount

    def pay(self, amount):
        if amount <= 0:
            raise ValueError('Pay amount must be positive')
        self.bank_account.balance -= amount
        self.current_debt -= amount


my_account = BankAccount('Andersson')
print(f'Create bank account with balance: {my_account.balance}')
my_account.deposit(1750)
print(f'Deposit done, new balance: {my_account.balance}')

my_credit_card = CreditCard('Mastercard', 8000, 0, bank_account=my_account)
print(
    f'Create credit card with current debit: {my_credit_card.current_debt}, and limit: {my_credit_card.limit}')
my_credit_card.purchase(1500)
print(
    f'Purchase 1 approve: new debit: {my_credit_card.current_debt}')
my_credit_card.pay(1500)
print(
    f'Pay done. New debit: {my_credit_card.current_debt}. Balance account: {my_account.balance}')
# my_credit_card.purchase(8500)
# print(
#     # fail successfully
#     f'Purchase 2 approve: new debit: {my_credit_card.current_debt}')
my_credit_card.purchase(7500)
print(
    f'Purchase 3 approve: new debit: {my_credit_card.current_debt}')
# my_credit_card.pay(7500)
# print(
#     f'Pay done. New debit: {my_credit_card.current_debt}, New balance: {my_account}') # fail successfully
my_account.deposit(10000)
print(f'Deposit 2 done, new balance: {my_account.balance}')
my_credit_card.pay(7500)
print(
    f'Pay 2 done. New debit: {my_credit_card.current_debt}, New balance: {my_account.balance}')
