#Class and Instance Attributes

#Class attribute is an attribute that is going to be global for the class only, usually we create those to have shared information among all the class instances
#Example:

class CreditCard:
    limit_raise_amount = 1.5 # That is a class attribute
    def __init__(self, number, limit):
        self.number = number
        self.limit = limit

#The way that we could access those kind of attributes:

print(CreditCard.limit_raise_amount) # will print 1.5

#However, we also can access those, from the instances.

c1 = CreditCard("9876543210123456", 1000)
print(c1.limit_raise_amount) # Will print 1.5

print(c1.limit_raise_amount) # will print 1.5


c2 = CreditCard("1234569876543210", limit=2000)
c2.limit_raise_amount = 2

print(c2.limit_raise_amount)

## method will raise the limit from what it is, by 50%
class CreditCard:
    limit_raise_amount = 1.5
    def __init__(self, number, limit):
        self.number = number
        self.limit = limit

    def hide(self):
        self.number = f"**** **** **** {self.number[-4:]}"

    def raise_limit(self):
        self.limit = CreditCard.limit_raise_amount * self.limit
        print(f"Congratulations! New limit has been set to {self.limit} for card number: {self.number}")

c1 = CreditCard(number="1234567890123456", limit=1000)
c1.raise_limit()
c2 = CreditCard(number="9876542310123456", limit=1000)
c2.raise_limit()
