from models.accounts import BankAccount, CreditCard
from models.transactions import Transaction


my_account = BankAccount('Andersson')
print(f'Create bank account with balance: {my_account.balance}')
my_credit_card = CreditCard(my_account, 'Mastercard', 8000, 0)
print(
    f'Create credit card with current debit: {my_credit_card.current_debt}, and limit: {my_credit_card.limit}')

transaction1 = Transaction('2025-11-10', 15000, 'Salary', 'income', my_account)
transaction1.apply()
print(f'Transaction 1 done. New balance: {my_account.balance}')
transaction2 = Transaction(
    '2025-11-14', 200, 'Netflix', 'expense', my_credit_card)
transaction2.apply()
print(f'Transaction 2 done. New debit: {my_credit_card.current_debt}')
transaction3 = Transaction('2025-11-13', 1200, 'Shoes', 'expense', my_account)
transaction3.apply()
print(f'Transaction 3 done. New balance :{my_account.balance}')
transaction4 = Transaction(
    '2025-11-25', 1200, 'Shoes', 'expense', my_credit_card)
transaction4.apply()
print(f'Transaction 4 done. New debit :{my_credit_card.current_debt}')
transaction5 = Transaction(
    '2025-11-30', 1400, 'Pay credit card', 'pay_credit', my_credit_card)
transaction5.apply()
print(
    f'Transaction 5 done. New debit :{my_credit_card.current_debt} & new balance: {my_account.balance}')
