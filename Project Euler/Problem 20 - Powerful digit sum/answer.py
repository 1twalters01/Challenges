def summation(number):
    summation = 0
    while number > 0:
        summation = summation + number%10
        number = number//10
    return summation

def factorial(number):
    factorial = 1
    for i in range(1, number):
        factorial = factorial *i
    return summation(factorial)

number = 100
print(factorial(number))