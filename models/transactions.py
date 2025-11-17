from models.accounts import BankAccount, CreditCard
from datetime import date, datetime


class Transaction:
    def __init__(self, day, amount, description, trans_type, target):
        if isinstance(day, date):
            self.day = day
        elif isinstance(day, str):
            try:
                self.day = datetime.strptime(day, "%Y-%m-%d").date()
            except ValueError:
                raise ValueError('Invalid date format, expected YYYY-MM-DD')
        else:
            raise ValueError('Date format wrong')
        if (amount <= 0):
            raise ValueError('Amount must be more than zero')
        self.amount = amount
        self.description = description
        if trans_type not in ('income', 'expense', 'pay_credit'):
            raise ValueError('Please select a valid transaction type')
        self.trans_type = trans_type
        if (not isinstance(target, BankAccount) and not isinstance(target, CreditCard)):
            raise ValueError('Please select a valid account')
        self.target = target

    def apply(self):
        if self.trans_type == 'income' and isinstance(self.target, BankAccount):
            self.target.deposit(self.amount)
        elif self.trans_type == 'expense':
            if isinstance(self.target, BankAccount):
                self.target.withdraw(self.amount)
            if isinstance(self.target, CreditCard):
                self.target.purchase(self.amount)
        elif self.trans_type == 'pay_credit':
            if not isinstance(self.target, CreditCard):
                raise ValueError(
                    "pay_credit transactions require a CreditCard target")
            self.target.pay(self.amount)
        else:
            raise ValueError('Transaction invalid')


class RecurringTransaction:
    def __init__(self, day, amount, description, trans_type, target, frequency, start_date):
        if day < 1 or day > 28:
            raise ValueError('Day must be between 1 and 28')
        self.day = day
        if amount <= 0:
            raise ValueError('Amount must be more than zero')
        self.amount = amount
        self.description = description
        if trans_type not in ('income', 'expense', 'pay_credit'):
            raise ValueError('Please select a valid transaction type')
        self.trans_type = trans_type
        if not isinstance(target, (BankAccount, CreditCard)):
            raise ValueError('Please select a valid account')
        if trans_type == 'income' and not isinstance(target, BankAccount):
            raise ValueError(
                'Income recurring transactions must target a BankAccount')
        if trans_type == 'pay_credit' and not isinstance(target, CreditCard):
            raise ValueError(
                'pay_credit recurring transactions require a CreditCard target')
        self.target = target
        if frequency not in ('weekly', 'monthly'):
            raise ValueError('Frequency not valid')
        self.frequency = frequency
        if isinstance(start_date, date):
            self.start_day = start_date
        elif isinstance(start_date, str):
            try:
                self.start_date = datetime.strptime(
                    start_date, "%Y-%m-%d").date()
            except ValueError:
                raise ValueError('Invalid date format, expected YYYY-MM-DD')
        else:
            raise ValueError('Date format wrong')
