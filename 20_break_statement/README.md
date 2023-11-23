# Break Statement
## Break keyword is available to use within loops, to immediately getting out of a for loop execution.
```python
#We should use break keyword when we want to get out of the associated for loop, usually we will do it to check some condition in each iteration, and once we hit true, then we will use break.
#This is useful to efficient our program, and to prevent from unnecessary executions.

#Example:
friends = ["Josh", "Ben", "John", "Michael", "Jim"]
best_friend = "Josh"

for friend in friends:
    if friend == best_friend:
        print(f"{best_friend} is inside the list!")
        break
    else:
        print(f"This is {friend}")

print("I am just a random line after the for loop")
```
