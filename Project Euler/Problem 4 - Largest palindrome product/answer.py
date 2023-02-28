def is_palindrome(x):
    x = str(x)
    if x == x[::-1]:
        return True
    return False

def reversed_list(array):
    return sorted(array)[::-1]

# Could use matrix multiplication with numpy instead
# make a a column matrix and b a row matrix
def generate_array(left_no_digits, right_no_digit):
    left = int("9"*left_no_digits)
    right = int("9"*right_no_digit)
    array = [0]*left*right
    i = 0
    for a in range(1, left+1):
        for b in range(1,right+1):
            array[i] = a*b
            i += 1
    return array

def largest_palindrome_product(left_no_digits, right_no_digit):
    array = generate_array(left_no_digits, right_no_digit)
    array = reversed_list(array)
    for i in array:
        if is_palindrome(i) == True:
            return i

print(largest_palindrome_product(3,3))