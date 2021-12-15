import random
a_list = [random.randrange(1, 50, 1) for i in
          range(random.randrange(2, 20, 1))]
print(len(set(a_list)))
