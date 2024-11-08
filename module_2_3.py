my_list = [42, 69, 322, 13, 0, 99, -5, 9, 8, 7, -6, 5]

a = 0

while a <= len(my_list):
    b = my_list[a]

    a += 1

    if b == 0 :
        continue

    elif b < 0 :
        break

    elif a == len(my_list) :
        break

    else:
        print(b)





