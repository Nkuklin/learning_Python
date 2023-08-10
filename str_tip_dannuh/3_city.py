c1 = input()
c2 = input()
c3 = input()

lc1 = int(len(c1))
lc2 = int(len(c2))
lc3 = int(len(c3))

max = max(lc1, lc2, lc3)
min = min(lc1, lc2, lc3)

city = lc1 + lc2 + lc3
city = city - max - min

if min == lc1:
    print(c1)
elif min == lc2:
    print(c2)
else:
    print(c3)

if max == lc1:
    print(c1)
elif max == lc2:
    print(c2)
elif max == lc3:
    print(c3)