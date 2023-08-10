a1 = int(input())
b1 = int(input())
a2 = int(input())
b2 = int(input())

if b1 < a2 or b2 < a1:       # отрезки не пересекаются
    print("пустое множество")

if a1 < a2 and b1 == a2:   # отрезки пересекаються в одной точке b1 a2
    print(a2)

if b2 < b1 and b2 == a1:   # отрезки пересекаються в одной точке b2 a1
    print(b2)

if b1 == b2:
    if a1 < a2:
        print(a2, b1)
    else:
        print(a1, b1)

if a1 == a2:
    if b1 < b2:
        print(a1, b1)
    elif b2 < b1:
        print(a1, b2)

if a1 < a2 < b1 < b2:
    print(a2, b1)

if a2 < a1 < b2 < b1:
    print(a1, b2)

if a1 < a2 < b2 < b1:
    print(a2, b2)

if a2 < a1 < b1 < b2:
    print(a1, b1)
