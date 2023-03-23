def fib(limit):
    a, b = 1, 2
    while a < limit:
        a, b = b, a+b
        yield a

upper_bound = int(input('Enter the value of the upper bound: '))
fib_list = [i for i in fib(upper_bound) if i%2 == 0]
print(sum(fib_list))