from math import *

a = float(input())
b = float(input())
c = float(input())

d = b**2 - 4 * a * c

if d < 0:
    print('Нет корней')
elif d == 0:
    print((-b - sqrt(d))/(2 * a))
elif d > 0:
    x1 = ((-b - sqrt(d))/(2 * a))
    x2 = ((-b + sqrt(d))/(2 * a))
    if x1 > x2:
        print(x2)
        print(x1)
    elif x1 < x2:
        print(x1)
        print(x2)
