numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
primes = []
not_primes = []

numbers.remove(1)

for i in numbers:

    is_prime = True

    for j in numbers:

        if j == i:
            break

        if i % j == 0:
            is_prime = False
            break

    if is_prime:
        primes.append(i)
    else:
        not_primes.append(i)

print(f"Primes: {primes}\nNot Primes: {not_primes}")