from task_2 import modul_1 as first
from task_2 import modul_2 as second

print("Функция нахождения пары:")
first.pair_finding([1, 2, 3, 4, 1, 5, 6], 2)
print("\nФункция генератор простых чисел:")
for m in first.prime_generator(1, 100):
    print(m, end=" ")
print("\n\nФункция возвращающая список четных индексов:")
print(first.solve([1, 2, 3, 4, 5, 6, 7]))

# print(help(first))

print("\nФункция двух чисел необязательно стоящие рядом:")
second.two_digits()
print("\nФункция автоморфные числа:")
second.amorphous()
print("\nФункция двух чисел стоящие рядом:")
second.digits_next_to()
# print(help(second))
