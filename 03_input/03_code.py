#Input built in function

#Input built-in function allows to receive input from the user while the program runs. Program won't resume until you put your input.


#We assign the input built-in function to a variable.
answer = input("How is the weather today")
print("The weather today is ", answer)

#You can force your inputs to receive specific types of variables:
current_year = 2023
answer = int(input("What is your age?")) # We could use any built-in conversion function here we'd like
print("Your year of birth is", current_year - answer)
