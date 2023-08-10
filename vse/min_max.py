a, b, c = int(input()), int(input()), int(input())

max_num = max(a, b, c)
min_num = min(a, b, c)

n = a + b + c
mid = (n - max_num) - min_num

print(max_num, mid, min_num, sep="\n")

