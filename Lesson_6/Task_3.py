import random

a = 0
b_list = [random.randrange(1, 20, 1) for i in
          range(random.randrange(2, 7, 1))]
print(b_list)
c_list = [random.randrange(1, 20, 1) for j in
          range(random.randrange(2, 7, 1))]
print(c_list)
a_list = b_list + c_list
# print(a_list)
for i in range(0, len(a_list), ):
    d_list = b_list + c_list
    del d_list[i]
    if a_list[i] not in d_list:
        a += 1
# a_list.sort()
# print(a_list)
print(f"Уникальных чисел {a}")
