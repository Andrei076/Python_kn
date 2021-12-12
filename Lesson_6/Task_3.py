import random
a_list = [random.randrange(1, 20, 1) for i in
          range(random.randrange(2, 5, 1))]
b_list = [random.randrange(1, 20, 1) for j in
          range(random.randrange(2, 5, 1))]
# print(a_list)
# print(b_list)
c=a_list+b_list
n=0
for d in c:
    if d in c[d+1::]:
        continue
else:
    n+=1
print(c)
print(n)

