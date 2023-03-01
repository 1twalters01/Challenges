def sum_square_difference(limit):
    summation = limit*(limit+1)/2
    summation_squared = summation**2
    square_summed = summation * (2*limit+1)/3
    return int(summation_squared - square_summed)

print(sum_square_difference(100))