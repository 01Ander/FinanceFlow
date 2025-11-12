from models.accounts import BankAccount, CreditCard


class Transaction:
    def __init__(self, date, amount, description, trans_type, target):
        self.date = date
        if (amount < 0):
            raise ValueError('Amount must be more than zero')
        self.amount = amount
        self.description = description
        if (trans_type != 'Income' and trans_type != 'Expense'):
            raise ValueError('Please select a valid transaction type')
        self.trans_type = trans_type
        if (not isinstance(target, BankAccount) and not isinstance(target, CreditCard)):
            raise ValueError('Please select a valid account')
        self.target = target

    def apply(self):
        if self.trans_type is 'Income' and self.target is BankAccount:
