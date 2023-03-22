import threading


class Account:
    def __init__(self):
        self.open = True
        self.balance = 0.0
        self.lock = threading.Lock()

    def open(self):
        if self.open:
            raise ValueError('Account already open')
        else:
            self.open = True
    def close(self):
        if not self.open:
            raise ValueError('Account already closed')
        else:
            self.open = False

    def get_balance(self):
        if not self.open:
            raise ValueError('Account is closed')
        else:
            print(self.balance)
    def deposit(self, amount):
        if not self.open:
            raise ValueError('Account is closed')
        else:
            with self.lock:
                self.balance += amount
    def withdraw(self, amount):
        if not self.open:
            raise ValueError('Account is closed')
        else:
            with self.lock:
                self.balance -= amount

my_account = Account()
my_account.deposit(55)
my_account.deposit(1234)
my_account.withdraw(1000)
my_account.get_balance()