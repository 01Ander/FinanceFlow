from models.accounts import BankAccount, CreditCard
from models.transactions import Transaction
from storage.transactions_csv import save_transactions_to_csv, append_transaction_to_csv


my_account = BankAccount('Andersson')
print(f'Create bank account with balance: {my_account.balance}')
my_credit_card = CreditCard(my_account, 'Mastercard', 8000, 0)
print(
    f'Create credit card with current debit: {my_credit_card.current_debt}, and limit: {my_credit_card.limit}')

t1 = Transaction('2025-11-10', 15000, 'Salary', 'income', my_account)
t1.apply()
print(f'Transaction 1 done. New balance: {my_account.balance}')
t2 = Transaction(
    '2025-11-14', 200, 'Netflix', 'expense', my_credit_card)
t2.apply()
print(f'Transaction 2 done. New debit: {my_credit_card.current_debt}')
t3 = Transaction('2025-11-13', 1200, 'Shoes', 'expense', my_account)
t3.apply()
print(f'Transaction 3 done. New balance :{my_account.balance}')
t4 = Transaction(
    '2025-11-25', 1200, 'Shoes', 'expense', my_credit_card)
t4.apply()
print(f'Transaction 4 done. New debit :{my_credit_card.current_debt}')
t5 = Transaction(
    '2025-11-30', 1400, 'Pay credit card', 'pay_credit', my_credit_card)
t5.apply()
print(
    f'Transaction 5 done. New debit :{my_credit_card.current_debt} & new balance: {my_account.balance}')


transactions_November = [t1, t2, t3, t4, t5]
save_transactions_to_csv('data/transactions.csv', transactions_November)

t6 = Transaction('2025-12-01', 200, 'Christmas tree',
                 'expense', my_credit_card)
t6.apply()
print('T6 apply')

append_transaction_to_csv('data/transactions.csv', t6)
