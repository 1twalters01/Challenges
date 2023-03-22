def distinct_powers(a, b):
    count = set()
    for i in range(2,a+1):
        for j in range(2,b+1):
            power = i**j
            count.add(power)
    return len(count)


a,b = 100, 100
print(distinct_powers(a,b))