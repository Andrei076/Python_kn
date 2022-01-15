from modul_sort import *
import random

my_list = [random.randint(1, 50) for i in range(10)]
print(f"Список, который нужно отсортировать: {my_list}")
print(f"Сортировка методом пузырька: {babble_sort(my_list)}")
print(f"Сортировка методом камня: {babble_rock_sort(my_list)}")
print(f"Сортировка методом вставки: {insertion_sort(my_list)}")

# help("modul_sort")
