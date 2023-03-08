def fib(digits):
    a = 0
    b = 1
    while len(str(a)) < digits:
        a, b = b, a+b
        yield a

digits = 1000
fib_list = [i for i in fib(digits)]
print(len(fib_list))