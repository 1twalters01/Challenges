def permutated_multiples(value):
    multiplied = [str(value), str(2*value), str(3*value), str(4*value), str(5*value), str(6*value)]
    
    it = iter(multiplied)
    the_len = next(it)
    if not all(len(l) == len(the_len) for l in it):
        return False
    sorted_list = [''.join(sorted(s)) for s in multiplied]

    it = iter(sorted_list)
    the_len = next(it)
    if not all(l == the_len for l in it):
        return False
    
    return True

def counter():
    count = 1
    while True:
        if permutated_multiples(count) == True:
            return count
        count += 1

print(counter())
