def multiples_of_3_and_5(limit):
    limit = limit-1
    limit3, limit5, limit15  = limits_for_3_5_and_15(limit)
    summation3, summation5, summation15 = summations_for_3_5_and_15(limit3, limit5, limit15)
    answer = summation3 + summation5 - summation15
    return int(answer)

def limits_for_3_5_and_15(limit):
    limit3, limit5, limit15  = limit//3, limit//5, limit//15
    print('limits: {}, {}, {}'.format(limit3, limit5, limit15))
    return limit3, limit5, limit15

def summations_for_3_5_and_15(limit3, limit5, limit15):
    summation3 = 0.5*(limit3**2 + limit3)*3
    print(limit3**2)
    summation5 = 0.5*(limit5**2 + limit5)*5
    summation15 = 0.5*(limit15**2 + limit15)*15
    print('limits: {}, {}, {}'.format(summation3, summation5, summation15))
    return summation3, summation5, summation15

value = int(input("Enter a number: "))
print(multiples_of_3_and_5(value))