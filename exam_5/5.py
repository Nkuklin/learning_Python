n = int(input())
n1 = None

if n % 2 == 1:
    print("YES")
elif 2 <= n <= 5:
    n1 = n
    if n % 2 == 0:
        print("NO")
elif 6 <= n <= 20:
    n1 = n
    if n % 2 == 0:
        print("YES")
elif n % 2 == 0 and n > 20:
    print("NO")