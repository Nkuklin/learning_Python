x1 = int(input())
y1 = int(input())
x2 = int(input())
y2 = int(input())

color_1 = None
color_2 = None

# хоти определить цвет первой клетки
# определяем является ли 1 клетка белой
if x1 % 2 == 0 and y1 % 2 == 0:
    color_1 = "white"
elif x1 % 2 == 1 and y1 % 2 == 1:
    color_1 = "white"
# определяем является ли 1 клетка черной
if x1 % 2 == 0 and y1 % 2 == 1:
    color_1 = "black"
elif x1 % 2 == 1 and y1 % 2 == 0:
    color_1 = "black"

# определяем цвет второй клетки
# определяем является ли 2 клетка белой
if x2 % 2 == y2 % 2:
    color_2 = "white"
# определяем является ли 2 клетка черной
if x2 % 2 != y2 % 2:
    color_2 = "black"

if color_1 == color_2:
    print("YES")
else:
    print("NO")
