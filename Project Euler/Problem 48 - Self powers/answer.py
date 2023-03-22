def obtain_sum(number):
    sum = 0
    for i in range(1, number+1):
        sum = sum + i**i
    return get_digits(sum)

def get_digits(number):
    return str(number)[-10:]

print(obtain_sum(10))
    