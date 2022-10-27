# class Account:
#     """class definition of Account"""
#     ls = [1, 2, 3, 4, 5, 6, 7, 8, 9]
#     number = 10
#     coefficient = 5.5
#     s = "This is string"
#     flag = False
#
#
#     def tax(balance):
#         return balance * 0.16

import empty

from empty import Account
# from empty import A
# from empty import B

class SomeClass:

    def tax(account, Account):
        if isinstance(account, Account):
            return account.balance * 0.1


a = Account()
a.balance = 1000
print(SomeClass.tax(a))
print(a.tax())