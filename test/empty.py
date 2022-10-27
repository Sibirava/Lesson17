class Account:
    def tax(self):
        return self.balance * 0.1


    def withdraw(self):
        pass

    def __str__(self):
        pass



a1 = Account()
a2 = Account()
a3 = Account()
a1.balance = 1000
a2.balance = 2000
a3.balance = 3000

print(a1.tax()) #--> Account.tax(a1)



a.balance = 1000
print(Account.tax(a))
print(a.tax()) #<--- объектно-ориентированный подход

print(Account.tax)
print(a.tax)


    # name = "no name"
    # balance = 100
    #
    # Account.name = "1234456"

class A:
    pass
class B:
    pass

# a1 = Account()
# a1.name = "hbdgkjgb"
# a2 = Account()
#
# print(a1.name)
# print(a2.name)
# print(a1.name)