
a = int(input('Введите число: '))

factorial = 1

while a > 1:
    factorial *= a
    a -= 1

print(factorial)

# 2. Через метод for

a = int(input('Введите число: '))

factorial = 1

for a in range(2,a+1) :
    factorial *= a

print(factorial)

# 3. С помощью рекурсии

def fac(a):
    if a == 1:
        return 1
    return fac(a - 1) * a


print(fac())