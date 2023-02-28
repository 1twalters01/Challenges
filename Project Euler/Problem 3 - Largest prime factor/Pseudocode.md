# Problem 3 - Largest prime factor
## O(n)
The largest prime factor will be lower than the square root of the number

for all prime numbers between 1 and the number/2 + 1:
    if the modulo is 0 then save the number in an array
    divide the limit by the number in question and start again
    return the highest number in the array