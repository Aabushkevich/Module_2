#Нашел в интернете, но понять сложно
# Метод while

fib1 = 1
fib2 = 1
n = input("Номер элемента ряда Фибоначчи:" )
n = int(n) - 2

while n > 0 :
    fib1, fib2 = fib2, fib1 + fib2
    n -= 1

print("Значение этого элемента:" ,fib2)

# Метод for

fib1 = fib2 = 1
n = int(input())
print(fib1, fib2, end=' ')

for i in range(2, n):
    fib1, fib2 = fib2, fib1 + fib2
    print(fib2, end=' ')

# Рекурсия
def fibonacci(n):
    if n in (1, 2):
        return 1
    return fibonacci(n - 1) + fibonacci(n - 2)


print(fibonacci(10))

