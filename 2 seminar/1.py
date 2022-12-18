def count_sum(m):
    sum = 0
    for el in m:
        if el.isdigit():
            el = int(el)
            sum +=el
    print(sum)

m = input("Введите число m = ")
count_sum(m)