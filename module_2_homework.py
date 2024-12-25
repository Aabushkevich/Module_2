def sum_range(x, y):
    return sum(range(x, y + 1))


print(sum_range(8, 17))


def triangle(x, y, z):
    if (x + y) > z and (x + z) > y and (y + z) > x:
        print('Треугольник построен')
    else:
        print('Построение невозможно')


triangle(10, 5, 8)


def lucky(n):
    n = list(n)
    if n[0] + n[1] + n[2] == n[3] + n[4] + n[5]:
        print('Вам повезло!)')
    else:
        print('Попробуйте снова:(')


lucky([10, 2, 3, 4, 5, 6])


def len_(*n):
    n = str(n)
    for i in n:
        i = len(n)
    print(i)


len_('Anton', 'Andrey', 'Ivan')