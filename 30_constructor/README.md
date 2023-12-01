# Constructor / __init__()
## Constructor will help us to pass in unique info per instance when we initialize an instance
```python
class CreditCard:
    pass

c1 = CreditCard()
c1.number = "1234567890123456"
c1.limit = 5000
c1.company = "JimCompany"

c2 = CreditCard()
c2.number = "9876543210123456"
c2.limit = 2500
c2.company = "JohnCompany"

c3 = CreditCard()
c3.number = "1234567899876543"
c3.limit = 1000
c3.company = "JoshCompany"


class CreditCard:
    def __init__(self):
        print("I am created!")

c1 = CreditCard() # Will print 'I am created'

#The self keyword is a parameter convention name that will refer always to the instance of the class

class CreditCard:
    def __init__(self, number):
        self.number = number

c1 = CreditCard(number="1234567890123456")
c2 = CreditCard(number="1234567894567891")
c3 = CreditCard(number="9876543210123456")
c4 = CreditCard(number="1234567895645621")


print(c1.number)
print(c2.number)
print(c3.number)
print(c4.number)
```
