def summation(num):
    summed_digits = 0
    while num != 0:
        summed_digits = summed_digits + num%10
        num = num //10
    return summed_digits

def loop(a,b):
    max_number = 0
    for x in range(1,a):
        for y in range(1,b):
            calc = summation(x**y)
            if calc > max_number:
                max_number = calc
    return max_number

print(loop(100, 100))