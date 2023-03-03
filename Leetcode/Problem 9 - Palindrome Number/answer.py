def isPalindrome(x):
    if str(x) == str(x)[::-1]:
        return True
    else:
        return False

def intIsPalindrome(x):
    if x < 0:
        return False
    copy = x
    reverse = 0
    while copy != 0:
        reverse = reverse*10 + copy%10
        copy = copy//10
    if reverse == x:
        return True
    else:
        return False
    
value = -12121
print(isPalindrome(value))
print(intIsPalindrome(value))