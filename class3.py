class BankAccount:

    # the self is used to represent the instance of the class
    # it is used to access variables that belong to the class
    def __init__(self, bal):
        self.__balance = bal

    def deposit(self, amount):
        # add to the balance
        self.__balance += amount

    def withdraw(self, amount):
        if self.__balance >= amount:
            # subtract the balance
            self.__balance -= amount
        else:
            print("error: insufficient funds")

    def get_balance(self):
        return self.__balance