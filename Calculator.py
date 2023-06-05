# (+, -, *, /),
a = int(input())
b = int(input())
znak = input()

if znak == '+':
    print(a + b)
elif znak == '-':
    print(a - b)
elif znak == '*':
    print(a * b)
elif znak == '/' and b == 0:
    print('На ноль делить нельзя!')
elif znak == '/':
    print(a / b)
else:
    print('Неверная операция')
