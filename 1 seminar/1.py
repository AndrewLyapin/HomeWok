'''Напишите программу, которая принимает на вход цифру, обозначающую день недели, и проверяет, является ли этот день выходным.

Пример:

- 6 -> да
- 7 -> да
- 1 -> нет
'''

find_day = int(input("Введите день недели(1-7) "))
if 1 <= find_day <= 5:
    print("Будний")
elif 6 <= find_day <=7:
    (print("Выходной"))
else:
    print("Таких дней нет")