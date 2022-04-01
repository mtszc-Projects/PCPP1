"""
2.7.1.5 LAB
https://edube.org/learn/python-advanced-1/lab-2
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
