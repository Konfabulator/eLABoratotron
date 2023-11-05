# Measurement arithmetic average and it's uncertainty

from math import sqrt
Values = [    # Values of measurement (multiple measurements of the same value)
    44.4,
    44.5,
]
Delta = 0.5   # Uncertainty of measurement

def mean(w):
    return sum(w)/len(w)
def U_mean(w,delta):
    summ = 0
    N = len(w)
    mean_w = mean(w)
    for i in w:
        summ += (i - mean_w)**2
    return sqrt(summ/(N*(N-1)) + (delta**2)/3)

print(mean(Values), '+-', U_mean(Values,Delta))