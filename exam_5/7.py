def is_knight_move(x1, y1, x2, y2):
    # Проверяем, что разница по вертикали и горизонтали составляет 2 и 1 поля соответственно
    if abs(x1 - x2) == 2 and abs(y1 - y2) == 1:
        return True
    # Проверяем, что разница по вертикали и горизонтали составляет 1 и 2 поля соответственно
    elif abs(x1 - x2) == 1 and abs(y1 - y2) == 2:
        return True
    else:
        return False

# Считываем входные данные
x1, y1, x2, y2 = map(int, input().split())

# Проверяем, может ли конь попасть из первой клетки во вторую одним ходом
if is_knight_move(x1, y1, x2, y2):
    print("YES")
else:
    print("NO")