# Problem 29 - Distinct powers
## O(n2)
function input what a and b are
    create a set
    for all numbers between 2 and a
        for all numbers between 2 and b
            add a**b to the set
    get the length of the set