#Dictionary Methods

#   keys() - Will collect all the keys
#   values() - Will collect all the values
friend = {
    "name" : "Josh",
    "age" : 35,
    "is_male" : True,
    "weight" : 84.5
}
print(friend.keys())
print(friend.values())

#Those lines will return you a type of variable
#That it's name is dict_keys

#To make it more friendly, we can convert it to a list:

print(list(friend.keys()))
print(list(friend.values()))
