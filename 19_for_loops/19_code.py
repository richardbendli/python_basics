# For Loops
# A for loop acts as an iterator in Python; it goes through items that are in a sequence or any other iterable item.

friends = ["Josh", "Ben", "John", "Michael"]


#print(f"{friends[0]} is my friend")
#print(f"{friends[1]} is my friend")
#print(f"{friends[2]} is my friend")
#print(f"{friends[3]} is my friend")

#For loops:
#A for loop is used for iterating over a sequence (in this case we have a list.)
#For loop template:

# for ____ in ______
#   new_var   iterable variable type
for my_friend in friends:
    print(f"{my_friend} is my friend")

# Examples

friends = ["Josh", "Ben", "John", "Michael", "Jim"]
best_friend = "Josh"
#Write a program that will check if our best_friend is in the friends list. If so, throw a special message.

#Solution 1:
if best_friend in friends:
    print(f"{best_friend} is in the list of friends!")

#Solution 2:
for friend in friends:
    if friend == best_friend:
        print(f"{best_friend} is inside the list!")
