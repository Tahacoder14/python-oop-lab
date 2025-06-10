"""
Task 12: Encapsulation - Protecting Your Object's Secrets
Concept:
Encapsulation bundles data and methods, restricting direct access to some components.
Experiment with a bank account: deposit and withdraw funds.
_protected (convention), __private (name mangling).
"""

class BankAccount:
    def __init__(self, account_holder, initial_balance=0):
        self.account_holder = account_holder  # Public
        self._balance = float(initial_balance) # Protected
        self.__transaction_id_counter = 0     # Private
        self.__transaction_log = []           # Private
        print(f"Account for {self.account_holder} created with balance: ${self._balance:.2f}")

    def _generate_transaction_id(self): # Protected method
        self.__transaction_id_counter += 1
        return f"TXN{self.__transaction_id_counter:04d}"

    def deposit(self, amount):
        amount = float(amount)
        if amount > 0:
            self._balance += amount
            txn_id = self._generate_transaction_id()
            self.__transaction_log.append(f"{txn_id}: Deposited ${amount:.2f}")
            print(f"Deposited ${amount:.2f}. New balance: ${self._balance:.2f}")
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount):
        amount = float(amount)
        if 0 < amount <= self._balance:
            self._balance -= amount
            txn_id = self._generate_transaction_id()
            self.__transaction_log.append(f"{txn_id}: Withdrew ${amount:.2f}")
            print(f"Withdrew ${amount:.2f}. New balance: ${self._balance:.2f}")
        elif amount > self._balance:
            print(f"Insufficient funds. Cannot withdraw ${amount:.2f} from ${self._balance:.2f}.")
        else:
            print("Withdrawal amount must be positive.")

    def get_balance(self):
        return self._balance

    def view_transaction_log(self):
        print("\n--- Transaction Log ---")
        if not self.__transaction_log:
            print("No transactions yet.")
        for entry in self.__transaction_log:
            print(entry)
        print("-----------------------")

def get_input_params():
    return [
        {"name": "holder_name", "label": "Account Holder Name:", "type": "text_input", "default": "Alice Wonderland"},
        {"name": "initial_deposit", "label": "Initial Deposit Amount:", "type": "number_input", "default": 1000.00, "min_value":0.0, "step":50.0, "format": "%.2f"},
        {"name": "deposit_amount", "label": "Amount to Deposit Now:", "type": "number_input", "default": 500.00, "min_value":0.0, "step":10.0, "format": "%.2f"},
        {"name": "withdraw_amount", "label": "Amount to Withdraw:", "type": "number_input", "default": 200.00, "min_value":0.0, "step":10.0, "format": "%.2f"},
    ]

def run_task(holder_name, initial_deposit, deposit_amount, withdraw_amount):
    my_account = BankAccount(holder_name, initial_deposit)

    print(f"\nAccount Holder (public): {my_account.account_holder}")

    print("\n--- Performing transactions with your inputs ---")
    my_account.deposit(deposit_amount)
    my_account.withdraw(withdraw_amount)
    my_account.withdraw(my_account.get_balance() + 100) # Attempt to overdraw

    print(f"\nFinal balance via public method: ${my_account.get_balance():.2f}")
    my_account.view_transaction_log()

    print("\n--- Notes on Encapsulation ---")
    print("`_balance` is 'protected' (by convention, accessible but shouldn't be modified directly).")
    print("`__transaction_id_counter` and `__transaction_log` are 'private' (name-mangled by Python).")
    print(f"Accessing mangled counter: my_account._BankAccount__transaction_id_counter = {my_account._BankAccount__transaction_id_counter}")

if __name__ == "__main__":
    run_task("Bob The Saver", 2000, 300, 150)