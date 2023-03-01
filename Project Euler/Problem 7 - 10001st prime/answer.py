def is_prime(num):
    i = 0
    for i in range(2, (num+3)//2):
        if num % i == 0:
            return False
    return True

def nth_prime(limit):
    count = 2
    no_of_primes = 0
    prime = 0
    while no_of_primes < limit:
        if is_prime(count) == True:
            prime = count
            no_of_primes += 1
            yield prime
        count+= 1

value = 10001
print(list(nth_prime(value))[value-1])