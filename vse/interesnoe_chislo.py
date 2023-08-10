n = int(input())

first = n // 100

second = n // 10
second = second - (first * 10)
third = n - second * 10 - first * 100

max_num = max(first, second, third)
min_num = min(first, second, third)

s = first + second + third
mid = (s - max_num) - min_num

if max_num - min_num == mid:
    print("Число интересное")
else:
    print("Число неинтересное")

