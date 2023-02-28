def simplify(array):
    i = 0
    while i < len(array)-1:
        for n in range(i, len(array)):
            if array[n] % array[i] == 0 and n!= i:
                array[n] = int(array[n]/array[i])
        i+=1
    return array


def multiply(n):
    total = 1
    for i in n:
        total *= i
    return(total)

def smallest_multiple(value):
    array = list(range(1,value+1))
    array = simplify(array)
    total = multiply(array)
    print(total)
        

smallest_multiple(20)