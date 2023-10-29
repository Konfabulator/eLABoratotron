from math import sqrt
Values = [
    44.4,
    44.5

]
Delta = 0.5

def mean(w):
    return sum(w)/len(w)
def U_mean(w,delta):
    summ = 0
    N = len(w)
    mean_w = mean(w)
    for i in w:
        summ += (i - mean_w)**2
    return sqrt(summ/(N*(N-1)) + (delta**2)/3)
# print(mean(Values))
# print(U_mean(Values,Delta))
# for i in range(len(Values)//2):
#     # print(mean(w[2*i:2*i+2]))
#     print(U_mean(Values[2*i:2*i+2],Delta))
print(U_mean(Values,Delta))
# for i in range(len(Values)//3):
    # print(mean(w[2*i:2*i+2]))
    # print(U_mean(Values[3*i:3*i+3],Delta))