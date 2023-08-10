a = input()
b = input()
c = input()

number1 = int(len(a))
number2 = int(len(b))
number3 = int(len(c))

max = max(number1,number2,number3)
min = min(number1,number2,number3)
mid = (number3 + number2 + number1) - min - max
d = mid - min

if mid == min + d and max == min + d * 2:
    print("YES")
else:
    print("NO")
