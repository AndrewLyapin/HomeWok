'''Напишите программу, которая принимает на вход координаты точки (X и Y),
 причём X ≠ 0 и Y ≠ 0 и выдаёт номер четверти плоскости,
 в которой находится эта точка (или на какой оси она находится).

Пример:

- x=34; y=-30 -> 4
- x=2; y=4-> 1
- x=-34; y=-30 -> 3 '''


x = int(input("x = "))
y = int(input("y = "))


def find_point(x, y):
    if x == 0 and y == 0:
        print("х и у не может быть равен 0")
    if x > 0 and y > 0:
        print("x =", x, "; y =", y, " -> 1 четверть")
    if x < 0 and y > 0:
        print("x =", x, "; y =", y, " -> 2 четверть")
    if x < 0 and y < 0:
        print("x =", x, "; y =", y, " -> 3 четверть")
    if x > 0 and y < 0:
        print("x =", x, "; y =", y, " -> 4 четверть")


find_point(x, y)