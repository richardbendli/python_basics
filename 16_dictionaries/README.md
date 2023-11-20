# Dictionaries
## Dictionaries can allow us to store multiple key value pairs under one variable name.
```python
#Wrong practice:
friend_name = "Josh"
friend_age = 35
friend_gender = True
friend_weight = 84.5

#The better approach will be to create dictionary,
#Since the variables have something in common (Friend's attributes)
#And this could be noticed because we use a lot of times the prefix of friend when we create those variables

#We create dictionaries by using {} to variable assignment:

friend = {
#   "key" : "value"
    "name" : "Josh",
    "age" : 35,
    "is_male" : True,
    "weight" : 84.5
}
#See the value of some key:
print(friend["name"])
print(friend.get("name"))

#What will happen if we specify a non existing key ?
print(friend["is_female"]) # Will crash the program if you mismatched the key name
print(friend.get("is_female")) # Will try to find the key, and return the attached value, if does not find, will NOT crash your program, but will show - None

#Another example:

number_to_letter = {
    1 : "a",
    2 : "b",
    3 : "c"
}
print(number_to_letter[1])
```
