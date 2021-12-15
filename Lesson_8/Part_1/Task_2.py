import random
a_list = [random.randrange(1, 50, 1) for i in
          range(random.randrange(2, 20, 1))]
b_list = [random.randrange(1, 50, 1) for j in
          range(random.randrange(2, 20, 1))]
print(a_list)
print(b_list)
print(len(set(b_list) & set(a_list)))
