import random
a_list = [random.randrange(1, 101, 1) for i in
          range(random.randrange(2, 11, 1))]
print(a_list)
k = input(f"Введите индекс от 0 до {len(a_list)-1} ")
c = input(f"Введите число ")
if k.isdigit() and len(a_list) > int(k) >= 0 and c.isdigit():
    a_list.append(0)
    for i in range(len(a_list) - 1, int(k), -1):
        a_list[i] = a_list[i - 1]
    a_list[int(k)] = int(c)
    print(a_list)
else:
    print("Вы ввели неправильный индекс или число!")
