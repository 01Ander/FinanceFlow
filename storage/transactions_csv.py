import csv
import os
from models.accounts import BankAccount, CreditCard
from models.transactions import Transaction

CSV_HEADER = ['date', 'amount', 'description',
              'trans_type', 'target_type', 'target_name']


def transaction_to_row(transaction: Transaction):
    date_value = transaction.day
    date_str = date_value.isoformat()
    amount = transaction.amount
    description = transaction.description
    trans_type = transaction.trans_type
    target = transaction.target
    if isinstance(target, BankAccount):
        target_type = "bank_account"
    elif isinstance(target, CreditCard):
        target_type = "credit_card"
    else:
        raise ValueError("Unsupported target type for transaction")
    target_name = getattr(target, 'name', '')
    return [date_str, amount, description, trans_type, target_type, target_name]


def save_transactions_to_csv(filepath: str, transactions: list[Transaction]):
    with open(filepath, mode='w', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerow(CSV_HEADER)
        for transaction in transactions:
            row = transaction_to_row(transaction)
            writer.writerow(row)


def append_transaction_to_csv(filepath: str, transaction: Transaction):
    file_exists = os.path.exists(filepath)
    with open(filepath, mode='a', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        if not file_exists:
            writer.writerow(CSV_HEADER)
        row = transaction_to_row(transaction)
        writer.writerow(row)
