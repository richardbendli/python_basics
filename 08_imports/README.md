# Imports
## There are tons of external libraries in Python that you can use them by calling it's name using the built-in keyword import.
```python
import math

#We want to perform some more complex math operations, than we can import the math library and use its additional functionalities:
a = 8.2
b = math.floor(a)
c = math.ceil(a)
print(b)
print(c)

#There are some more ways that we can import additional functionalities.
#We can refer to the specific function that we want to import from an external library.

from math import ceil

#And then use it like:

d = 8.2
e = ceil(d)
print(e)

#But that approach is less common, since Python will load the entire library anyway.
#We might think that importing specific function could improve the time run of our program, but this is not the case.
```
