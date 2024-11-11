number = int(input("Введите число от 3 до 20:" ))
if 3 <= number <= 20:
    res = []

    for i in range(1, number):
        for j in range(i+1, number):
            if number % (i + j) == 0 and i != j:
                res.extend([i, j])

    res = ("".join(map(str, res)))
    print(f"{number} - {res}")

else:
    print("Число вне указанного диапазона")