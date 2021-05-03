
def __init__(self, first_name, last_name, account_num, balance=0):
    self.first_name = first_name
    self.last_name = last_name
    self.account_num = account_num
    self.balance = balance
    self.transactions = []
def deposit(self, amount):
    self.balance += amount
    self.transactions.append(+amount)
    return amount
def withdrawal(self, amount, limit=500):
    if self.balance - amount > 0 and amount <= limit:
        self.balance -= amount
        self.transactions.append(-amount)
        return amount
    else:
        return 'Your withdrawal amount is ${} which exceeds your account limit! You have:' \
                '\n${}. Your withdrawal limit is {}'.format(amount, self.balance, limit)
def get_first_name(self):
    return self.first_name
def get_last_name(self):
    return self.last_name
def get_account_num(self):
    return self.account_num
def get_balance(self):
    return self.balance
def recent_transactions(self):
    if len(self.transactions) < 1:
       return None
    else:
       return self.transactions.pop()
