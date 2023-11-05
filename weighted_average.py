from math import *
values = [
-9.631718184508847,
-9.807692307692307
]
errors = [
0.07374920079720412,
0.33670225101017276
]

def mean(wart, niep):
    licz, mian = 0,0
    for w,n in zip(wart, niep):
        licz += w/n**2
        mian += 1/n**2
    return licz/mian

def u_int(wart,niep):
    mian = 0
    for n in niep:
        mian += 1/(n)**2
    return 1/sqrt(mian)

def u_ext(wart,niep):
    summa = 0
    mean_val = mean(wart, niep)
    for w,n in zip(wart, niep):
        summa += ((w-mean_val)/n)**2
    return sqrt(((u_int(wart,niep)**2)/(len(wart)-1))  *  summa)

print('Mean: ',mean(values,errors))
print('U_int:',u_int(values,errors))
print('U_ext:',u_ext(values,errors))