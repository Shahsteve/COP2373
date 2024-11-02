class BankAcct:
    def __init__(self, name, account_number, amount, interest_rate):
        self.name = name
        self.account_number = account_number
        self.amount = amount
        self.interest_rate = interest_rate

    def deposit(self, amount):
        self.amount += amount

    def withdraw(self, amount):
        if amount <= self.amount:
            self.amount -= amount
        else:
            print("Insufficient funds!")

    def get_balance(self):
        return self.amount

    def adjust_interest_rate(self, new_rate):
        self.interest_rate = new_rate

    def calculate_interest(self, days):
        interest = (self.amount * self.interest_rate * days) / 365
        return interest

    def __str__(self):
        return f"Account Holder's Name: {self.name}\nAccount Number: {self.account_number}\nBalance: {self.amount}\nInterest Rate: {self.interest_rate}"


def test_bank_account():
    account = BankAcct("Steven Shah", 69875, 9856, 0.05)
    print(account)
    account.deposit(1000)
    print(account)
    account.withdraw(500)
    print(account)
    print("Interest for 30 days:", account.calculate_interest(30))
    account.adjust_interest_rate(0.09)
    print("New interest rate:", account.interest_rate)


if __name__ == "__main__":
    test_bank_account()