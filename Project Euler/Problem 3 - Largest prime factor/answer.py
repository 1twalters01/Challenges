def max_prime_factor(value):
    i = 2
    array = []
    while (2*i)+1 < value:
        while value % i == 0:
            value = value / i
            array.append(i)
        i += 1
    array.append(int(value))
    return max(array), array

limit = 600851475143
print(max_prime_factor(limit))
