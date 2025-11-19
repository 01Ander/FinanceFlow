# -----------------------------------------------------------
# Clase BankAccount
# Representa una cuenta bancaria con operaciones básicas:
# - Control de saldo (encapsulado con propiedad balance)
# - Depósitos y retiros con validación de montos
# -----------------------------------------------------------


class BankAccount:
    def __init__(self, name=None, balance=0.0):
        # Atributo protegido para guardar el saldo real
        self._balance = 0.0
        # Se usa el setter de balance para validar el valor inicial
        self.balance = balance
        self.name = name

    # ---- Encapsulamiento del saldo ----
    @property
    def balance(self):
        # Getter: devuelve el saldo actual
        return self._balance

    @balance.setter
    def balance(self, amount):
        # Setter: valida que el saldo no sea negativo
        if amount < 0:
            raise ValueError('Balance cannot be negative')
        self._balance = amount

    # ---- Operaciones principales ----
    def deposit(self, amount):
        # Incrementa el saldo si el monto es positivo
        if amount <= 0:
            raise ValueError('Deposit amount must be positive')
        self.balance += amount

    def withdraw(self, amount):
        # Disminuye el saldo si hay fondos suficientes
        if amount <= 0:
            raise ValueError('Withdrawal amount must be positive')
        if amount > self.balance:
            raise ValueError('Insufficient funds')
        self.balance -= amount


# -----------------------------------------------------------
# 💳 Clase CreditCard
# Representa una tarjeta de crédito vinculada a una cuenta bancaria.
# - Maneja compras, pagos y límite de crédito
# - Requiere una BankAccount para pagar la deuda
# -----------------------------------------------------------

class CreditCard:
    def __init__(self, bank_account, name=None, limit=0.0, current_debt=0.0, due_day=None):
        self.name = name
        self.limit = limit
        self.current_debt = current_debt
        self.due_day = due_day

        # Se valida que la tarjeta esté asociada a una cuenta bancaria
        if bank_account is None:
            raise ValueError('Credit Card requires a linked Bank Account')
        self.bank_account = bank_account

    # ---- Operaciones principales ----
    def purchase(self, amount):
        # Registra una compra si hay crédito disponible
        if amount <= 0:
            raise ValueError('Purchase amount must be positive')

        available = self.limit - self.current_debt
        if amount > available:
            raise ValueError('Purchase exceeds available credit')

        self.current_debt += amount

    def pay(self, amount):
        # Paga parte o toda la deuda usando la cuenta bancaria asociada
        if amount <= 0:
            raise ValueError('Pay amount must be positive')

        # No se puede pagar más de lo que se debe
        if amount > self.current_debt:
            raise ValueError('Impossible to pay more than the debt')

        # Retira el monto de la cuenta bancaria y lo descuenta de la deuda
        self.bank_account.withdraw(amount)
        self.current_debt -= amount
