def reverse(x):
    negative = None
    if x < 0:
        negative = True
        x = x*-1
    reverse = 0
    while x != 0:
        reverse = reverse*10+(x%10)
        x=int(x/10)
    if negative:
        print('hi')
        reverse = reverse*-1
    if reverse > 2**31 - 1 or reverse < -2**31:
       return 0
    return reverse

def reverse(self, x):
    negative = False
    if x != abs(x):
        negative = True
        x = abs(x)
    num = str(x)
    rev = int(num[::-1])
    if negative == True:
        rev = rev * -1
        if rev < -2**31:
            return 0
        return rev
    else:
        if rev > 2**31 - 1:
            return 0
            return rev
print(reverse(0))