import random
a_list = [random.randrange(1, 50, 1) for i in
          range(random.randrange(2, 20, 1))]
print(a_list)
b_list = []
for j in a_list:
    if a_list.count(j) == 1:
        b_list.append(j)
print(tuple(b_list[::-1]))
