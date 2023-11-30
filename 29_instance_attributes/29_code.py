#Instance Attributes

#Attributes are key value pairs that we can assign to any object (In our case, the object is an instance of a class)


#We can give different pieces of information to instances

class CreditCard:
    pass

my_card = CreditCard()
my_card.number = "1234567890123456"
my_card.limit = 5000
my_card.company = "xyz"

c2 = CreditCard()
c2.number = "9876543210123456"
c2.limit = 1000
c2.company = "xyz2"

#We can access their values by referring the same way that we created:

print(my_card.number)
print(my_card.limit)
print(my_card.company)

print(c2.number)
print(c2.limit)
print(c2.company)
