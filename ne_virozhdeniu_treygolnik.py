#Напишите программу, которая принимает три положительных числа и определяет, существует ли невырожденный треугольник с такими сторонами.
#Формат входных данных
#На вход программе подаётся три положительных целых числа.

#Формат выходных данных
#Программа должна вывести «YES» или «NO» в соответствии с условием задачи.

#Примечание. Треугольник существует, если выполняется неравенство треугольника.
#Тестовые данные 🟢3
#Sample Input 1:
#5
#2
#3

#3
#4
#6

a = int(input())
b = int(input())
c = int(input())

if a + b > c and a + c > b and b + c > a:
    print('YES')
else:
    print('NO')