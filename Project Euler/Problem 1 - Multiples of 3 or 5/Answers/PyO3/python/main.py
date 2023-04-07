from rust import limits_for_3_5_and_15, summations_for_3_5_and_15

limit3, limit5, limit15 = limits_for_3_5_and_15(1000)
summation3, summation5, summation15 = summations_for_3_5_and_15(limit3, limit5, limit15)
answer = summation3 + summation5 - summation15
print(answer)