# Problem 9 - Palindrome Number
## O(1)
Turn it into a string
if the reverse of the string is equal to the string return true
else return false

## O(1)
if the number is less than 0 return false
Create a varible equal to 0
create a copy of the number and a variable = 0
While the copy is not = 0:
    variable = variable * 10 + number modulo 10
    number = number floor divided by 10
if copy is equal to the original then return true
else return false