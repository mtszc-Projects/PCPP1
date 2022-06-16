"""
2.7.1.5 LAB
https://edube.org/learn/python-advanced-1/lab-2
Implement a class representing an account exception,
Implement a class representing a single bank account,
This class should control access to the account number and account balance attributes by implementing the properties:
    it should be possible to read the account number only, not change it. In case someone tries to change the account
    number, raise an alarm by raising an exception;
    it should not be possible to set a negative balance. In case someone tries to set a negative balance, raise an alarm
    by raising an exception;
    when the bank operation (deposit or withdrawal) is above 100.000, then additional message should be printed on the
    standard output (screen) for auditing purposes;
    it should not be possible to delete an account as long as the balance is not zero;
test your class behavior by:
    setting the balance to 1000;
    trying to set the balance to -200;
    trying to set a new value for the account number;
    trying to deposit 1.000.000;
    trying to delete the account attribute containing a non-zero balance.
"""


class AccountException(Exception):
    pass


class SingleBankAccount:
    def __init__(self, __account_number):
        self.__account_number = __account_number
        self.__account_balance = 0

    @property
    def account_number(self):
        return self.__account_number

    @account_number.setter
    def account_number(self, amount):
        raise AccountException('No permission to change account number.')

    @account_number.deleter
    def account_number(self):
        if self.__account_balance != 0:
            raise AccountException('Account balance must be 0.')
        else:
            del self.__account_number

    @property
    def account_balance(self):
        return self.__account_balance

    @account_balance.setter
    def account_balance(self, amount):
        if amount < 0:
            if abs(amount) > self.__account_balance:
                raise AccountException('Not enough balance.')
            else:
                self.__account_balance += amount
        elif 0 <= amount <= 100000:
            self.__account_balance += amount
        else:
            print('Auditing process needed.')
            self.__account_balance += amount

    @account_balance.deleter
    def account_balance(self):
        if self.__account_balance != 0:
            raise AccountException('Account balance must be 0.')
        else:
            del self.__account_balance


if __name__ == '__main__':
    account_1 = SingleBankAccount(123456789)
    account_1.account_balance = 1000
    account_1.account_balance = -1200
    account_1.account_number = 1234
    account_1.account_balance = 1000000
    account_1.account_balance = -1000
    del account_1.account_balance
    print(account_1.account_balance)
