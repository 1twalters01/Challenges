def fib(limit):
    a = 1
    b = 2
    while a < limit:
        yield a
        a, b = b, a+b

upper_bound = 4000000
fib_list = [i for i in fib(upper_bound) if i%2 == 0]
print(sum(fib_list))