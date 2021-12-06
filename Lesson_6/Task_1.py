import random
a_list = [random.randrange(1, 101, 1) for i in range(random.randrange(2, 11, 1))]
k = int(input(f"Введите индекс, меньше числа {len(a_list)} "))
if k < len(a_list):
    a_list = a_list[:k:] + a_list[k + 1::1]
    print(a_list)
else:
    print("Вы ввели неправильный индекс!")
