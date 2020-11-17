import math

print('Введите желаемую точность е:')

e = float(input())

s = 0
summ = i = 1

#Считаем, что нужная точность достигнута,
#если очередное слагаемое оказалось по модулю меньше,
#чем e, поэтому это и все последующие слагаемые можно
#не учитывать.

while e < abs(summ):
    summ = (-1) ** (i + 1) / math.factorial(2 * i)
    s = s + summ
    i += 1
 
print(s)
