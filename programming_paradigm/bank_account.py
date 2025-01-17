class BankAccount:
    def __init__(self, initial_balance=0):
        """
        Initialize a new BankAccount instance.
        
        :param initial_balance: Initial amount in the account, default is 0.
        """
        self.__account_balance = initial_balance

    def deposit(self, amount):
        """
        Deposit money into the account.
        
        :param amount: The amount to deposit.
        """
        if amount > 0:
            self.__account_balance += amount
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount):
        """
        Withdraw money from the account if sufficient funds are available.
        
        :param amount: The amount to withdraw.
        :return: True if the withdrawal was successful, False otherwise.
        """
        if amount > self.__account_balance:
            return False
        elif amount > 0:
            self.__account_balance -= amount
            return True
        else:
            print("Withdrawal amount must be positive.")
            return False

    def display_balance(self):
        """
        Display the current account balance.
        """
        print(f"Current Balance: ${self.__account_balance:.2f}")