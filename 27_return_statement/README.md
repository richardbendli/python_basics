# Return Statement

```python
#This case is going to return nothing, because we did not use return keyword
def square_my_number(num):
    print(num ** 2)

result = square_my_number(num=4)
print(result)

#So it is equivalent to this:
def square_my_number(num):
    print(num ** 2)
    return None

result = square_my_number(num=4)
print(result)

#But we could decide that we want to store within the result variable the value of 16

#Example:
def square_my_number(num):
    return num ** 2

result = square_my_number(num=4)
print(result)

```
