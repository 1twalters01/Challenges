def fib(limit):
    a = 1
    b = 2
    while a < limit:
        yield a
        a, b = b, a+b

fib_list = [i for i in fib(4000000) if i%2 == 0]
print(sum(fib_list))