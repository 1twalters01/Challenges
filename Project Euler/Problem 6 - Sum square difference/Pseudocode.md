# Sum square difference
## O(1)
Get the target number and do the sum equation -> Sum = n(n+1)/2
Take the sum and square it

Take the sum and multiply by (2n+1)/3
Derive this by doing:
    n^3 - (n-1)^3 = 3n^2 - 3n + 1
                  = 3*Sum2 - 3n + 1
    3*Sum2 = n^3 - (n-1)^3 + 3n -1
          = n(n+1)(2n+1)/2
    
    Sum2 = Sum*(2n+1)/3

Get the difference of these two values