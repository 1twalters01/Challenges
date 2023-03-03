# Problem 3 - Longest Substring Without Repeating Characters
# O(n)
Create a blank set and a variable for the max length
Have two pointers
for each element in the array:
    if the character is new then add it to the set, check if the length of the set is the new max length and increase the rhs pointer
    if the character is in the set then remove it and increase the lhs pointer
once the rhs pointer is at the end 
