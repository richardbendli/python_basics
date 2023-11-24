#Value Decrement and Increment

#Value decrement and increment is the process of reassigning a value to an existing variable name.


#Example:
age = 24
#Besides using:
age = age + 1
#We could use:
age += 1
#Or besides using
age = age - 1
#We could use
age -= 1

budget = 100
sandwich_price = 5

#budget should decrease by 5 each time we print
#you bought a sandwich
for i in range(20):
    print("You bought a sandwich!")
    budget -= sandwich_price #Python Decrement
print(budget)

#We can use increment
#budget += 10 # Python Increment
