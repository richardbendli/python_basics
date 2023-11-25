# Iterable or Not Iterable

```python
#Iterable - Means that you can run a for loop on it
#Non Iterable - Means that you can not run a for loop on it
num = 1 # Integer                          # Non Iterable
name = "Jim" # String                      # Iterable (On each character)
fl = 4.5 # Float                           # Non Iterable
is_male = True # Boolean                   # Non Iterable
friends = ['Josh', "Ben"] # List           # Iterable (On each element in list)
tpl = ('Josh', 'Ben') # Tuple              # Iterable (On each element in tuple)
info = {"name" : "Jim"} # Dictionary       # Iterable (On each key&value pair in dictionaries)

for r in info: #change the iterated value to test the others
    print(r)
```
