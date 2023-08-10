ves = int(input())

if ves < 60:
    print('Легкий вес')
elif 60 <= ves < 64:
    print('Первый полусредний вес')
elif ves >= 64:
    print('Полусредний вес')
