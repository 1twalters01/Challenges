# Problem 25 - 1000-digit Fibonacci number
## O(n)
Sum though the numbers storing them in variables
a, b = b, a+b with a starting at 0, 1

May need a holder variable in some languages:
holder = a
a = b
b = holder + b

while there are less than 1000 digits:
    increase the value
    increment


repeat while a < target number