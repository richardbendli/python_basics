#Instance Methods

class Student:
    # constructor
    def __init__(self, name, age):
        # Instance variable
        self.name = name
        self.age = age

    # instance method access instance variable
    def show(self):
        print('Name:', self.name, 'Age:', self.age)

# create first object
print('First Student')
emma = Student("Amy", 24)
# call instance method
emma.show()

# create second object
print('Second Student')
kelly = Student("Emma", 26)
# call instance method
kelly.show()
