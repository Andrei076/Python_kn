# вариант решения №1
import random
a_list = [random.randrange(1, 101, 1) for i in
          range(random.randrange(2, 11, 1))]
# print(a_list)
k = input(f"Введите индекс от 0 до {len(a_list)-1} ")
if k.isdigit() and len(a_list) > int(k) >= 0:
    for i in range(int(k) + 1, len(a_list)):
        a_list[i - 1] = a_list[i]
    a_list.pop()
    print(a_list)
else:
    print("Вы ввели неправильный индекс!")

# вариант решения №2
# import random
# a_list = [random.randrange(1, 101, 1) for i in
#           range(random.randrange(2, 11, 1))]
# print(a_list)
# k = input(f"Введите индекс от 0 до {len(a_list)-1} ")
# if k.isdigit() and len(a_list) > int(k) >= 0:
#     a_list = a_list[:int(k):] + a_list[int(k) + 1::1]
#     print(a_list)
# else:
#     print("Вы ввели неправильный индекс!")
