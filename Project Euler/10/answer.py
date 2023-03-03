def is_prime(num):
    i = 0
    for i in range(2, (num+3)//2):
        if num % i == 0:
            return False
    return True

def sum_primes_slow(limit):
    count = 2
    sumOfPrime = 0
    while count < limit:
        if is_prime(count) == True:
            sumOfPrime = sumOfPrime + count
        count+= 1
    return sumOfPrime


def sum_primes(limit):
    sumOfPrimes = 0
    sieve = [True] * limit
    for p in range(2, limit):
        if sieve[p] == True:
            sumOfPrimes += p
            for i in range(p*p, limit, p):
                sieve[i] = False
    return sumOfPrimes

value = 2000000
print(sum_primes(value))